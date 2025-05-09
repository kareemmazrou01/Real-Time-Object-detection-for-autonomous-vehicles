from flask import Flask, render_template, request, Response
import cv2
import numpy as np
from ultralytics import YOLO
import os
from datetime import datetime
import mlflow


app = Flask(__name__)

# Absolute upload path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CURRENT_VIDEO'] = None
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  

# Load YOLO model
model_path = os.path.join(BASE_DIR, 'best.pt')
model = YOLO(model_path)

def process_frame(frame):
    """Run YOLO detection and return annotated frame."""
    results = model(frame)
    return results[0].plot()

def generate_frames(video_path):
    """Yield processed video frames as MJPEG stream and log with MLflow."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[ERROR] Unable to open video: {video_path}")
        return

    frame_count = 0

    # Start MLflow run
    with mlflow.start_run():
        mlflow.log_param("model", "YOLOv8")
        mlflow.log_param("source_video", video_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            annotated_frame = process_frame(frame)

            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            if not ret:
                continue

            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        mlflow.log_metric("frames_processed", frame_count)
        mlflow.log_artifact(video_path)

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return 'No video file uploaded', 400

    video = request.files['video']
    if video.filename == '':
        return 'No video selected', 400

    # Save with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], f'video_{timestamp}.mp4')
    video.save(video_path)
    app.config['CURRENT_VIDEO'] = video_path

    return render_template('index.html', video_uploaded=True)

@app.route('/video_feed')
def video_feed():
    video_path = app.config.get('CURRENT_VIDEO')
    if not video_path or not os.path.exists(video_path):
        return 'No video available', 404

    return Response(generate_frames(video_path),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import tensorflow as tf
import cv2
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the path to your model
MODEL_PATH = 'D:\\Tejas\\Projects\\Integrated_motion_analysis\\Integrated-Motion-Analysis-main\\Integrated-Motion-Analysis-main\\Model.h5'

# Initialize the model variable
model = None

# Load the model
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    # Optionally, you can terminate the application if the model is critical
    raise SystemExit("Critical Error: Model could not be loaded. Terminating application.")

# Configure the upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check if the file has a valid extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to preprocess video and make predictions
def process_video_with_model(video_path):
    if model is None:
        raise ValueError("Model is not loaded. Cannot proceed with prediction.")
    
    IMAGE_HEIGHT, IMAGE_WIDTH = 64, 64
    SEQUENCE_LENGTH = 20

    video_reader = cv2.VideoCapture(video_path)
    frames_list = []
    video_frames_count = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))
    skip_frames_window = max(int(video_frames_count / SEQUENCE_LENGTH), 1)
 
    for frame_counter in range(SEQUENCE_LENGTH):
        video_reader.set(cv2.CAP_PROP_POS_FRAMES, frame_counter * skip_frames_window)
        success, frame = video_reader.read()

        if not success:
            break

        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
        normalized_frame = resized_frame / 255.0
        frames_list.append(normalized_frame)

    frames_array = np.array(frames_list)
    frames_array = np.expand_dims(frames_array, axis=0)
    predicted_labels_probabilities = model.predict(frames_array)[0]
    predicted_label = np.argmax(predicted_labels_probabilities)

    CLASSES_LIST = ["BenchPress", "CleanAndJerk", "Fencing", "HulaHoop", "JumpRope", "JumpingJack"]
    predicted_class = CLASSES_LIST[predicted_label]
    confidence = float(predicted_labels_probabilities[predicted_label])
    
    return predicted_class, confidence


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

import traceback

import traceback

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video file part"}), 400

    video = request.files['video']

    if video.filename == '':
        return jsonify({"error": "No selected video"}), 400

    if video and allowed_file(video.filename):
        filename = secure_filename(video.filename)
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video.save(video_path)

        try:
            print(f"Video saved at: {video_path}")
            result_class, confidence = process_video_with_model(video_path)
            print(f"Prediction: {result_class} with confidence {confidence}")
            return jsonify({
                "predicted_class": result_class,
                "confidence": confidence
            })
        except Exception as e:
            print(f"Error during video processing: {e}")
            traceback.print_exc()
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid file format"}), 400





if __name__ == '__main__':
    app.run(debug=True)

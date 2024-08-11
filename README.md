# Integrated Motion Analysis

Welcome to the **Integrated Motion Analysis** project! This application uses a deep learning model to predict the type of physical activity being performed in a video. The project is built with a Flask backend that handles video processing and model prediction, and a React frontend that allows users to upload videos and view prediction results.

## Features

- **Video Upload**: Users can upload a video file in formats like `.mp4`, `.avi`, or `.mov`.
- **Activity Prediction**: The backend processes the video and predicts the activity being performed using a trained deep learning model.
- **Confidence Score**: The prediction is accompanied by a confidence score, indicating the model's certainty.
- **Responsive Design**: The frontend is designed to be responsive and visually appealing.

## Project Structure

```plaintext
your-project-directory/
│
├── public/
│   └── index.html
│
├── src/
│   ├── components/
│   │   ├── Home.js
│   │   ├── UploadVideo.js
│   │   └── Result.js
│   ├── styles/
│   │   ├── global.css
│   │   ├── home.css
│   │   ├── uploadVideo.css
│   │   └── result.css
│   ├── App.js
│   ├── index.js
│   └── index.css
│
└── package.json


Backend (Flask)
Python: Handles video processing and prediction.
Flask: Web framework used to create API endpoints.
TensorFlow: Machine learning library used to load and execute the pre-trained model.
OpenCV: Used for video frame extraction and preprocessing.


Frontend (React)
React: JavaScript library for building user interfaces.
Axios: Used for making HTTP requests to the Flask API.
CSS: Custom styles for a modern and responsive design.

Installation
Prerequisites
Python 3.x
Node.js and npm
Git


Usage
Run the Flask backend server.
Run the React frontend.
Visit http://localhost:3000 in your browser.
Upload a video file using the provided interface.
View the predicted activity and confidence score.


Technologies Used
Flask
React
TensorFlow
OpenCV
Axios
CSS


Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.

Contact
For any inquiries or issues, please contact tejaxspatil@gmail.com

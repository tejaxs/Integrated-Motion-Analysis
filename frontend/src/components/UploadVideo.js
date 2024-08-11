import React, { useState } from 'react';
import axios from 'axios';

function UploadVideo({ setResult }) {
    const [video, setVideo] = useState(null);

    const handleVideoChange = (e) => {
        setVideo(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('video', video);
    
        try {
            const response = await axios.post('http://localhost:5000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
    
            const { predicted_class, confidence } = response.data;
            setResult({
                className: predicted_class,
                score: confidence
            });
        } catch (error) {
            console.error("Error details:", error.response ? error.response.data : error.message);
            setResult({
                className: null,
                score: null,
                error: "There was an error processing your request. Please try again."
            });
        }
    };
    

    return (
        <div>
            <input type="file" onChange={handleVideoChange} />
            <button onClick={handleUpload}>Upload Video</button>
        </div>
    );
}

export default UploadVideo;

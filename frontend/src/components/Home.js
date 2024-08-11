import React, { useState } from 'react';
import UploadVideo from './UploadVideo';
import Result from './Result';

function Home() {
    const [result, setResult] = useState(null);

    return (
        <div className="container">
            <div className="row justify-content-center mt-5">
                <div className="col-md-6">
                    <h1 className="text-center mb-4">Video Activity Prediction</h1>
                    <UploadVideo setResult={setResult} />
                    <Result result={result} />
                </div>
            </div>
        </div>
    );
}

export default Home;

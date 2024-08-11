import React from 'react';

function Result({ result }) {
    if (!result) return null;

    return (
        <div style={{ marginTop: '20px' }}>
            <h2>Prediction Result</h2>
            {result.error ? (
                <p>{result.error}</p>
            ) : (
                <p>Class: {result.className} with Confidence: {result.score.toFixed(4)}</p>
            )}
        </div>
    );
}

export default Result;

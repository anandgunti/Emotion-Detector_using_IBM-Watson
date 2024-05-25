"""
Emotion Detector Flask Application.

This module contains a Flask web application for detecting emotions in text.
It provides an endpoint for emotion analysis and serves an index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Endpoint to analyze the emotions of the given text.
    
    This endpoint expects a 'textToAnalyze' parameter in the query string.
    It processes the text using the emotion_detector function and returns
    a formatted response with the detected emotions and the dominant emotion.
    
    Returns:
        str: A formatted string with the emotion analysis results, or an
             error message if the input text is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    if response['dominant_emotion'] is not None:
        return formatted_response
    return "Invalid text! Please try again."


@app.route("/")
def render_index_page():
    """
    Renders the index page.

    This endpoint serves the main page of the application, which is 
    the 'index.html' template.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

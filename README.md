# Emotion Detection Application

## Introduction
Welcome to the Emotion Detection Application project! This repository showcases a powerful tool built using IBM Watson's Natural Language Processing (NLP) service. Our application goes beyond simple sentiment analysis by identifying specific emotions such as joy, sadness, anger, and more from textual inputs. This capability can be highly beneficial for AI-based recommendation systems, automated chatbots, and various other applications.

The application is developed using **Flask**, making it accessible as a web service. We have implemented **unit tests** to ensure reliability, followed PEP 8 coding guidelines (checked using the **Pylint library**), and incorporated robust error handling

![Emotion](https://github.com/anandgunti/Emotion-Detector/assets/25959661/63f0e362-a83f-4dff-bcf3-40d73243e43e)


## Project Overview
Throughout this project, we follow a structured approach to develop, test, and deploy our emotion detection application as a web service. Below is a step-by-step guide on how we accomplished this.

### Task 1: Clone the Project Repository
We start by cloning the project repository to our local machine using Git. This sets up the foundation for our project.

### Task 2: Create the Emotion Detection Function
Using the Watson NLP library, we create a function that analyzes emotions in given text. By authenticating with the Watson NLP API, we ensure our application can leverage the powerful AI capabilities provided by IBM.
```bash
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
```
### Task 3: Format the Output
To make the output more user-friendly, we format the detected emotions into a readable format. This ensures that the results are easily understandable.


### Task 4: Package the Application
We organize our code into modules and create a `EmotionDetection.py` file for packaging. This allows for easy distribution and installation of our application.

To use package use the following code
```bash
from EmotionDetection.emotion_detection import emotion_detector
```


### Task 5: Run Unit Tests
To ensure the reliability of our application, we write and run unit tests for our emotion detection function using the `unittest` framework.

### Task 6: Deploy as a Web Application Using Flask
We create a simple Flask web application to serve our emotion detection functionality, making it accessible via a web interface.


### Task 7: Incorporate Error Handling
We enhance our Flask app with error handling to manage invalid inputs and API errors gracefully, ensuring a robust application.


### Task 8: Run Static Code Analysis and Write a README
Finally, we run static code analysis using `pylint` to maintain code quality and write a comprehensive README file to document the project setup, usage, and testing instructions.


## Usage
Send a POST request to `/detect_emotions` with a JSON payload containing the text.

## Testing
Run unit tests:
```bash
python -m test_emotion_detection.py
```

### Conclusion
By following these steps, we have successfully created and deployed an emotion detection application that can analyze and interpret emotions from text using IBM Watson's powerful NLP capabilities. This project not only demonstrates the application of AI in emotion detection but also highlights the importance of proper development, testing, and deployment practices in creating robust web applications.

#### To use the application run the `server.py`  file. 

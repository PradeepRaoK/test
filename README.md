# Real-time Voice Transcription App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-username/real-time-voice-transcription-app/main/app.py)

This is a real-time voice transcription app built using Streamlit. The app allows users to transcribe their speech in real-time by clicking a microphone button and speaking.

## Problem Statement

The objective of this project is to develop a web application that provides real-time speech transcription functionality. Users can simply click a button to start the transcription and see their speech automatically transcribed as they speak.

## Installation

To run the app locally, you need to have Python and the required dependencies installed. Follow these steps:

1. Clone this repository:
```
git clone https://github.com/PradeepRaoK/test.git`
```


2. Navigate to the project directory:
```
cd test
```


3. Install the dependencies:
```
pip install streamlit
pip install SpeechRecognition
pip install PyAudio
```

4. Run the Streamlit app:
```
streamlit run app.py
```


5. Access the app in your browser at `http://localhost:8501`.

## Usage

Once the app is running, follow these steps to transcribe your speech in real-time:

1. Click the "Start Transcription" button.

2. Speak into your microphone, and your speech will be transcribed and displayed in real-time.

3. To stop the transcription, press `Ctrl+C` in the terminal or command prompt.

## Dependencies

The following libraries are used in this project:

- Streamlit
- SpeechRecognition
- PyAudio

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Streamlit community for providing a user-friendly framework for building web apps.
- The SpeechRecognition library for speech-to-text functionality.

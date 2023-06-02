import streamlit as st
import speech_recognition as sr

def main():
    st.title("Real-time Voice Transcription App")
    st.write("Click the 'Start Transcription' button and speak to see the real-time transcription.")
    
    # Create a button to start the transcription
    if st.button("Start Transcription"):
        # Create a recognizer object
        r = sr.Recognizer()
        
        # Open the microphone for audio input
        with sr.Microphone() as source:
            st.write("Listening...")
            
            # Continuously listen for speech and transcribe it in real-time
            while True:
                try:
                    # Read the audio data from the default microphone
                    audio = r.listen(source)
                    
                    # Convert speech to text
                    text = r.recognize_google(audio)
                    
                    # Display the transcribed text
                    st.write("Transcription: ", text)
                    
                except sr.UnknownValueError:
                    # Speech cannot be recognized
                    st.write("Speech not recognized")
                
                except sr.RequestError as e:
                    # Error occurred
                    st.write(f"Error: {e}")
                    
                except KeyboardInterrupt:
                    # Stop transcription on keyboard interrupt
                    break

if __name__ == "__main__":
    main()
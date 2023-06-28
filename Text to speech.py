import pyttsx3

def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

# Example usage
text = "Hello, Is this Manvi?"
text_to_speech(text)
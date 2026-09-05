import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening... Speak now!")
        audio = recognizer.listen(source)

    try:
        print("Converting speech to text...")
        text = recognizer.recognize_google(audio)

        print("\nYour speech:")
        print(text)

        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")

    except sr.RequestError:
        print("Could not connect to the speech recognition service.")


if __name__ == "__main__":
    speech_to_text()


# Converts text to speech using Google TTS and saves as .mp3

from gtts import gTTS
import os

def generate_audio(summary_text: str, output_path: str = "results/summary.mp3", lang: str = "en") -> None:
    """
    Converts summary text to an audio file using gTTS.

    Args:
        summary_text (str): The text to be converted to audio.
        output_path (str): Path to save the output audio file.
        lang (str): Language code (default is English).
    """
    if not summary_text.strip():
        print("AudioAgent: Empty summary text. Skipping audio generation.")
        return

    try:
        tts = gTTS(text=summary_text, lang=lang)
        tts.save(output_path)
        print(f"Audio saved to {output_path}")
    except Exception as e:
        print(f"AudioAgent: Error during audio generation: {e}")

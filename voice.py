import streamlit as st
from gtts import gTTS
import io
import base64
from streamlit_mic_recorder import speech_to_text


def record_voice(language="en"):
    # https://github.com/B4PT0R/streamlit-mic-recorder?tab=readme-ov-file#example

    state = st.session_state

    if "text_received" not in state:
        state.text_received = []

    text = speech_to_text(
        start_prompt="🎤 Click and speak to ask question",
        stop_prompt="⚠️Stop recording🚨",
        language=language,
        use_container_width=True,
        just_once=True,
    )

    if text:
        state.text_received.append(text)

    result = ""
    for text in state.text_received:
        result += text

    state.text_received = []

    return result if result else None

def text_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    speech_bytes = io.BytesIO()
    tts.write_to_fp(speech_bytes)
    speech_bytes.seek(0)

    # Convert speech to base64 encoding
    speech_base64 = base64.b64encode(speech_bytes.read()).decode('utf-8')
    return speech_base64
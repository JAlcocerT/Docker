#import streamlit as st
from streamlit_webrtc import webrtc_streamer
import streamlit as st


audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)
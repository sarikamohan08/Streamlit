import streamlit as st

# Adding audio 
audio_file = open('audio.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

# video 

video_file = open('Introduction Video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
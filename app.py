import streamlit as st
import google.generativeai as genai

f = open("keys/.gemini.txt")
OPENAI_API_KEY = f.read()

genai.configure(api_key=OPENAI_API_KEY)

st.title("😍💕Well-come to my code debuger app😍💕")


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

promt = st.text_input("Enter your python code")

if st.button("Generate") == True:
    st.balloons()
    convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": promt
    }
    ])
    convo.send_message(promt)
    st.write(convo.last.text)



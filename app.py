import streamlit as st
import google.generativeai as genai

f = open("keys/.gemini.txt")
OPENAI_API_KEY = f.read()

genai.configure(api_key=OPENAI_API_KEY)

st.title("😍💕Well-come to my code debuger app😍💕")


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = " you are bug fixer app. handel all error user given code and re- write that code without bug "

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)
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



import dotenv
dotenv.load_dotenv()
import streamlit as st
import google.generativeai as genai
import os

# Load Gemini API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="CareMate – AI Health Assistant", page_icon="🩺")
st.title("🤖 CareMate – Your AI Health Companion")
st.write("Helping you stay healthy with a friendly AI-powered assistant.")

option = st.selectbox("Choose a service:", ["🩺 Symptom Checker", "🧠 Mental Health Check-In"])

def query_llm(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-002")  # Use the latest Gemini Flash 2.0 model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

if option == "🩺 Symptom Checker":
    st.subheader("Describe your symptoms")
    symptoms = st.text_area("Enter symptoms in English or Hinglish")
    if st.button("Analyze Symptoms"):
        with st.spinner("Analyzing..."):
            prompt = (
                "You are CareMate, a friendly AI health assistant. Given the user's symptoms, "
                "suggest possible common issues (like cold, stress, etc).\n"
                "Respond in Hinglish, keep the tone friendly. Add a disclaimer like 'This is not medical advice.'\n"
                f"User: {symptoms}"
            )
            response = query_llm(prompt)
            st.success(response)

elif option == "🧠 Mental Health Check-In":
    st.subheader("How are you feeling today?")
    mood = st.text_area("Describe your emotions")
    if st.button("Check Mental State"):
        with st.spinner("Analyzing..."):
            prompt = (
                "You are CareMate, a warm and supportive AI. Based on the user's message, give them emotional support.\n"
                "Respond in Hinglish with empathy and encouragement.\n"
                f"User: {mood}"
            )
            response = query_llm(prompt)
            st.success(response)

st.markdown("---")
st.markdown("Made with ❤️ for Code for Bharat Season 2")
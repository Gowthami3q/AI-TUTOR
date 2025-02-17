import streamlit as st
import openai

# Set OpenAI API Key (Replace 'your-api-key' with your actual API key)
openai.api_key = "AIzaSyB8T1RGCiWHSO94TEJuThtQ3mSoFuwAuGQ"

def review_code(code):
    """Function to review code using OpenAI API."""
    prompt = f"Review the following Python code for bugs and suggest fixes:\n\n{code}\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

# Streamlit UI
st.title("📝 An AI Code Reviewer")
st.write("Enter your Python code below and get an AI-generated review.")

# User Input
code_input = st.text_area("Enter Python code here:", height=200)

if st.button("Generate Review"):
    if code_input.strip():
        with st.spinner("Reviewing code..."):
            review = review_code(code_input)
            st.subheader("Code Review")
            st.text_area("AI Feedback", review, height=300)
    else:
        st.warning("Please enter some Python code.")
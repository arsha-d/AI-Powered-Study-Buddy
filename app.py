import streamlit as st
from groq import Groq

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI-Powered Study Buddy",
    page_icon="📘",
    layout="centered"
)

st.title("📘 AI-Powered Study Buddy")
st.write("Explain topics, summarize notes, and generate quizzes using online AI (Groq).")

# ---------------- GROQ SETUP ----------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ---------------- HELPER FUNCTION ----------------
def get_ai_response(prompt):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=500
    )
    return completion.choices[0].message.content

# ---------------- UI ----------------
option = st.sidebar.selectbox(
    "Choose a feature",
    ["Explain a Topic", "Summarize Notes", "Generate Quiz"]
)

# ---------------- FEATURE 1 ----------------
if option == "Explain a Topic":
    st.header("📖 Explain a Topic")
    topic = st.text_input("Enter a topic:")

    if st.button("Explain"):
        if topic:
            prompt = f"Explain {topic} in very simple terms with an example."
            output = get_ai_response(prompt)
            st.success("Explanation:")
            st.write(output)
        else:
            st.warning("Please enter a topic.")

# ---------------- FEATURE 2 ----------------
elif option == "Summarize Notes":
    st.header("📝 Summarize Notes")
    notes = st.text_area("Paste your study notes:")

    if st.button("Summarize"):
        if notes:
            prompt = f"Summarize the following notes into clear bullet points:\n{notes}"
            output = get_ai_response(prompt)
            st.success("Summary:")
            st.write(output)
        else:
            st.warning("Please paste some notes.")

# ---------------- FEATURE 3 ----------------
elif option == "Generate Quiz":
    st.header("❓ Generate Quiz")
    content = st.text_area("Enter topic or notes:")

    if st.button("Generate Quiz"):
        if content:
            prompt = (
                "Create 5 multiple-choice questions with 4 options each "
                "and clearly mention the correct answer.\n\n"
                f"Content:\n{content}"
            )
            output = get_ai_response(prompt)
            st.success("Quiz:")
            st.write(output)
        else:
            st.warning("Please enter content.")

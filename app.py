import os
import streamlit as st
from groq import Groq

# Load the environment variable for the API key
os.environ["GROQ_API_KEY"] = "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"  # Replace with your actual key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Function to get feedback from the model
def get_feedback(user_essay, level):
    system_prompt = """
        You are an expert academic writer with 40 years of experience in providing concise but effective feedback. 
        Instead of asking the student to do this and that, you just say replace this with this to improve in a concise manner. 
        You provide concise grammar mistakes saying replace this with this along with the mistake type. 
        You also provide specific replacement sentences for cohesion and abstraction, and you point out all the vocab saying 
        replace this word with this. Analyze the writing for grammar, cohesion, sentence structure, vocabulary, and the use 
        of simple, complex, and compound sentences, as well as the effectiveness of abstraction. Provide detailed feedback 
        on any mistakes and present an improved version of writing. Don't use words such as dive, discover, uncover, 
        delve, tailor, equipped, navigate, landscape, magic, comprehensive embrace, well equipped, unleash, cutting edge, 
        harness that give an AI-generated look. Strictly follow academic style in writing. If the user is of A1 level, 
        return the output for beginners; A2 for average; and A3 for advanced; and you can go till C1 level.
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{system_prompt}\nEssay:\n{user_essay}\nLevel: {level}"
            }
        ],
        model="llama3-8b-8192"
    )

    feedback = response.choices[0].message.content
    return feedback

# Streamlit UI
st.title("Writing Assistant for IELTS/TOEFL Preparation")

st.write("""
    This Writing Assistant app is designed to help students prepare for IELTS and TOEFL exams by providing detailed feedback on their essays. 
    Simply write your essay on the given topic, select your proficiency level, and submit it for analysis.
    The app will assess your writing for grammar, cohesion, sentence structure, vocabulary, and overall effectiveness.
""")
# Sidebar with Plan Selection
st.sidebar.title("Select Your Writing Plan")
plan = st.sidebar.radio("Choose a Plan", ("30 Days Plan", "45 Days Plan", "60 Days Plan"))

# Show Plan Details
if plan == "30 Days Plan":
    st.sidebar.write("Write every day for 30 days and get daily feedback on your essays.")
elif plan == "45 Days Plan":
    st.sidebar.write("Write every day for 45 days and improve your writing progressively.")
else:
    st.sidebar.write("A comprehensive 60 days writing improvement plan for advanced learners.")

# Input Section
st.subheader(f"Day 1 of {plan}")
# st.write("Topic: Discuss a recent technological advancement and its impact on society.")

# Textbox for user input
user_essay = st.text_area("Write your essay here:", height=300)

# Dropdown to select proficiency level
level = st.selectbox("Select your proficiency level:", ["A1 (Beginner)", "A2 (Average)", "B1", "B2", "C1 (Advanced)"])

# Button to submit essay
if st.button("Submit for Feedback"):
    if user_essay.strip():
        st.write("Analyzing your essay...")

        # Get feedback from the model
        feedback = get_feedback(user_essay, level)

        # Display feedback
        st.subheader("Feedback on your essay:")
        st.write(feedback)
    else:
        st.warning("Please write your essay before submitting!")

# Add LinkedIn handle
st.sidebar.subheader("Connect with Me")
st.sidebar.write("[Muhammad Adnan Tariq-LinkedIn](https://www.linkedin.com/in/adnaantariq/)")

st.sidebar.write("[Adnan Tariq-Instagram](https://www.instagram.com/adnaan_tariq/)")
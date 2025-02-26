import streamlit as st

# Page Configuration: 
st.set_page_config(page_title="Growth Mindset Project", page_icon="📈")

# add css for making it attractive
st.markdown("""
    <style>
        body {
            background-color: #f4f4f9;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: rgb(38, 100, 110);
            color: #ffffff;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: rgb(30, 139, 158);
            color: #ffffff;
            border: rgb(38, 100, 110);
        }
        .stTextInput input, .stTextArea textarea {
            background-color: #ffffff;
            border: 2px solid #BDC3C7;
            border-radius: 5px;
            padding: 10px;
            color: #34495E;
        }
        .stTextInput input:focus, .stTextArea textarea:focus {
            border-color: rgb(38, 100, 110);
            box-shadow: 0 0 5px rgb(70, 101, 105);
        }
        

        .stSuccess {
            background-color: #27AE60;
            color: white;
        }
        .stWarning {
            background-color: #E74C3C;
            color: white;
        }
        .stInfo {
            background-color: #3498DB;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Intro:
st.title("Growth Mindset Challenge 💡")
st.header("Welcome to Your Personal Growth Journey!")
st.write("""
    Building a growth mindset takes patience, resilience, and reflection. 
    This app is designed to help you face challenges, learn from them, and celebrate every step forward.
""")

# Motivational Quote 
st.header("Quote of the Day 💬")
quote = '&#34;It always seems impossible until it&#39;s done.&#34; &#45; Nelson Mandela'
st.write(f"**{quote}**")

# Challenge Section
st.header("What Challenge Are You Overcoming Today?")
challenge_input = st.text_input("Describe the challenge you&#39;re tackling today:")

if challenge_input:
    st.success(f"You&#39;re facing: *{challenge_input}*. Keep pushing forward. Every challenge is an opportunity to grow.")
else:
    st.warning("Please share your challenge to get started.")

# Reflection Section
st.header("Reflect on Your Growth 🌱 ")
reflection_input = st.text_area("Think about a past challenge you overcame. What did you learn from it?")

if reflection_input:
    st.success(f"Great reflection! Your insight: {reflection_input}")
else:
    st.info("Reflection helps you grow! Share your learning experience.")

# Achievement Section
st.header("Your Recent Achievement🎯 ")
achievement_input = st.text_input("What&#39;s one thing you&#39;ve accomplished recently that you&#39;re proud of?")

if achievement_input:
    st.success(f"Well done! You achieved: {achievement_input}. Keep up the great work!")
else:
    st.info("Celebrate your wins, no matter how small. What&#39;s your recent accomplishment?")

# Growth Mindset Quiz Section
st.header("Quick Growth Mindset Quiz")
st.write("""
    Answer the following questions to gauge your growth mindset. 
    Choose the option that best describes you.
""")

quiz_questions = [
    {
        "question": "When you face a challenge, you...",
        "options": ["Give up easily", "Try different strategies to solve it", "Avoid challenges"],
        "answer": "Try different strategies to solve it"
    },
    {
        "question": "How do you feel when you fail at something?",
        "options": ["It&#39;s the end of the world", "I look for lessons and try again", "I ignore it and move on"],
        "answer": "I look for lessons and try again"
    },
    {
        "question": "Do you believe abilities can be improved over time?",
        "options": ["No, it&#39;s fixed", "Yes, with effort and learning", "Maybe, but it&#39;s hard to believe"],
        "answer": "Yes, with effort and learning"
    },
    {
        "question": "How do you handle criticism?",
        "options": ["I take it personally and get upset", "I view it as feedback and use it to improve", "I ignore it completely"],
        "answer": "I view it as feedback and use it to improve"
    }
]

# Collect answers
user_answers = []
for i, question in enumerate(quiz_questions):
    answer = st.radio(question["question"], question["options"], key=i)
    user_answers.append(answer)

# Button to submit quiz 
if st.button("Submit Quiz"):
    score = 0
    for i, answer in enumerate(user_answers):
        if answer == quiz_questions[i]["answer"]:
            score += 1
    
    # Display the result based on score
    st.write(f"Your Growth Mindset Score: {score}/{len(quiz_questions)}")
    if score == len(quiz_questions):
        st.write("Fantastic! You have a strong growth mindset. Keep embracing challenges!")
    elif score >= len(quiz_questions) // 2:
        st.write("Good job! You&#39;re on the right track. Keep developing your growth mindset!")
    else:
        st.write("No worries! Developing a growth mindset is a journey. Keep learning and growing!")

# Footer
st.write("---")
st.write("Remember, growth is a continuous journey. Stay committed and keep learning.")
st.write("**&copy; 2025 Created by Rida Fatima**")

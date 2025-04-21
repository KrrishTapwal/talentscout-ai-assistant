import streamlit as st
import cohere

# Set your Cohere API key
COHERE_API_KEY = "k6MCq7D8oBiMSDc5OT2BVr05HCllpoliV01xCbZc"
co = cohere.Client(COHERE_API_KEY)

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "questions" not in st.session_state:
    st.session_state.questions = []
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []
if "info" not in st.session_state:
    st.session_state.info = {}
if "trigger_generate" not in st.session_state:
    st.session_state.trigger_generate = False

st.title("🤖 TalentScout AI Hiring Assistant")

# Step 1: Collect user info
if st.session_state.step == 1:
    st.markdown("Welcome to the TalentScout AI Hiring Assistant. This tool will help us assess your technical skills by asking a few questions based on your tech stack. Let's get started!")

    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position")
        location = st.text_input("Current Location")
        tech_stack = st.text_input("Tech Stack (e.g., Python, Django, SQL)")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not all([name, email, phone, experience, position, location, tech_stack]):
                st.warning("⚠️ Please fill all fields.")
            else:
                # This information will only exist during the session and will not persist.
                st.session_state.info = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "experience": experience,
                    "position": position,
                    "location": location,
                    "tech_stack": tech_stack,
                }
                st.session_state.trigger_generate = True
                st.rerun()

# Step 1.5: Generate questions after submission
if st.session_state.trigger_generate:
    try:
        prompt = f"""
        Generate exactly 3 technical interview questions for a candidate applying for a {st.session_state.info['position']} role
        with {st.session_state.info['experience']} years of experience. Their tech stack includes: {st.session_state.info['tech_stack']}.
        Only return the questions as a numbered list, no explanation, no extra text.
        """
        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7
        )
        questions = response.generations[0].text.strip().split("\n")
        st.session_state.questions = [q.strip() for q in questions if q.strip()]
        st.session_state.step = 2
        st.session_state.trigger_generate = False
        st.rerun()
    except Exception as e:
        st.error(f"Error generating questions: {e}")
        st.session_state.trigger_generate = False

# Step 2: Show questions and collect answers
if st.session_state.step == 2 and not st.session_state.user_answers:
    st.subheader("📋 Generated Technical Questions:")
    with st.form("answer_form"):
        answers = []
        for i, question in enumerate(st.session_state.questions):
            st.markdown(f"**{question}**")
            answer = st.text_area(f"Your Answer to Q{i+1}", key=f"answer_{i}")
            answers.append(answer)
        answer_submit = st.form_submit_button("Submit Answers")
        if answer_submit:
            st.session_state.user_answers = answers
            st.session_state.step = 3
            st.rerun()

# Step 3: Show summary
if st.session_state.step == 3:
    st.success("✅ Thank you for your submission! Our team will review your responses and get back to you soon.")

    st.markdown("### 📄 Your Submitted Information:")
    info = st.session_state.info
    st.markdown(f"""
    - **Full Name:** {info['name']}  
    - **Email:** {info['email']}  
    - **Phone:** {info['phone']}  
    - **Experience:** {info['experience']} years  
    - **Position:** {info['position']}  
    - **Location:** {info['location']}  
    - **Tech Stack:** {info['tech_stack']}  
    """)

    st.markdown("### ✍️ Your Answers:")
    for i, answer in enumerate(st.session_state.user_answers, 1):
        st.markdown(f"**Q{i} Answer:** {answer}")


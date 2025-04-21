:

🤖 TalentScout AI Hiring Assistant
TalentScout AI Hiring Assistant is an intelligent chatbot built with Streamlit and powered by Cohere's LLMs. It assists in the initial screening of candidates for tech roles by gathering essential information and generating tailored technical questions based on the candidate's tech stack.

📌 Features
Clean, user-friendly UI using Streamlit

Collects key candidate information:

Full Name

Email Address

Phone Number

Years of Experience

Desired Position

Current Location

Tech Stack

Uses Cohere’s command-r-plus model to:

Generate 3 custom technical questions based on the declared tech stack

Maintains conversation flow using session state

Final summary page showing submitted info and candidate responses

Graceful submission and completion behavior


🛠️ Tech Stack
Python

Streamlit (Frontend UI)

Cohere LLM (for generating technical questions)

🧠 Prompt Engineering
We used carefully crafted prompts to instruct the Cohere model to generate technical questions based on:

Candidate’s position

Years of experience

Tech stack (languages, frameworks, tools)

Prompt Example:

pgsql
Copy
Edit
Generate exactly 3 technical interview questions for a candidate applying for a {position} role
with {experience} years of experience. Their tech stack includes: {tech_stack}.
Only return the questions as a numbered list, no explanation, no extra text.
🏗️ Project Structure
bash
Copy
Edit
ai_hiring_assistant/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
📥 Installation & Usage
Prerequisites:
Python 3.7+

Streamlit

Cohere API key (get one from https://dashboard.cohere.com)

1. Clone the Repo:
bash
Copy
Edit
git clone https://github.com/your-username/talentscout-ai-assistant.git
cd talentscout-ai-assistant
2. Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Add Your Cohere API Key:
In app.py, set:

python
Copy
Edit
COHERE_API_KEY = "your-cohere-api-key"
4. Run the App:
bash
Copy
Edit
streamlit run app.py
🔒 Data Privacy
This app does not persist or store any user data. All session information is handled in memory and is cleared when the app restarts, aligning with GDPR-compliant best practices.

⚙️ Future Enhancements
Multilingual support

Sentiment analysis

Cloud deployment (AWS/GCP)

Persistent data storage with anonymization

🙋‍♀️ Challenges Faced
Ensuring context retention across steps using st.session_state

Making the form submission work with a single click

Prompt tuning for accurate and concise question generation

📌 License
This project is for educational/demo purposes only

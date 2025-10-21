
# TalentScout Hiring Assistant Chatbot

## Overview
TalentScout is an AI-powered Hiring Assistant chatbot developed as an assignment for the AI/ML Intern role. It simulates an intelligent recruiter that gathers candidate information and generates technical questions based on their declared tech stack.

This chatbot utilizes **Streamlit** for UI and integrates with an **LLM (GPT-3.5 or Llama)** to generate dynamic interview questions.

---

## Features
- Candidate data collection (Name, Contact Info, Experience, etc.)
- Dynamic generation of 3–5 technical questions per tech stack
- Seamless conversation flow with contextual memory
- Fallback mechanism and graceful exit handling
- Local anonymized data storage (optional)
- Modular and well-documented Python code

---

## Installation Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/TalentScout-Chatbot.git
cd TalentScout-Chatbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Set OpenAI API Key
```bash
export OPENAI_API_KEY="your_api_key_here"
```

### 5. Run the Application
```bash
streamlit run app.py
```

---

## Project Structure
```
Project_Root/
│
├── app.py
├── bot_logic/
│   ├── prompt_manager.py
│   ├── llm_handler.py
│   └── context_manager.py
├── data/
│   └── candidate_data.json
├── requirements.txt
└── README.md
```

---

## Prompt Design
- **Greeting Prompt:** Welcomes candidate and introduces the chatbot purpose.
- **Tech Stack Prompt:** Generates tailored technical questions for declared skills.
- **Fallback Prompt:** Ensures relevant context continuation.

Example:
> "Generate 3–5 unique technical questions for a candidate skilled in Python and Django."

---

## Challenges & Solutions
- **Handling multiple tech stacks:** Implemented per-stack question generation.
- **Maintaining context:** Session memory in Streamlit retains prior responses.
- **Data security:** Uses only anonymized simulated candidate data.

---

## Demo
A short Loom walkthrough can be recorded showing candidate flow and responses.

---

## Technologies Used
- Python 3.9+
- Streamlit
- OpenAI GPT-3.5 / Llama
- JSON & LangChain (optional)

---

## Author
Developed by [Your Name]

Assignment: AI/ML Intern – PGAGI

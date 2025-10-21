
import streamlit as st
import json
from bot_logic.prompt_manager import get_greeting_prompt, get_tech_questions_prompt
from bot_logic.llm_handler import generate_response
from bot_logic.context_manager import update_context, check_exit

# Initialize session state if not available
if 'context' not in st.session_state:
    st.session_state.context = {}

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

st.title('🤖 TalentScout Hiring Assistant Chatbot')
st.write('Welcome to TalentScout! I am your AI Hiring Assistant. I will help gather your details and ask relevant technical questions based on your tech stack.')

# Collect candidate basic info
with st.form('candidate_form'):
    full_name = st.text_input('Full Name')
    email = st.text_input('Email Address')
    phone = st.text_input('Phone Number')
    experience = st.number_input('Years of Experience', min_value=0, max_value=50, step=1)
    position = st.text_input('Desired Position(s)')
    location = st.text_input('Current Location')
    tech_stack = st.text_area('Tech Stack (e.g., Python, Django, React)')
    submitted = st.form_submit_button('Start Conversation')

if submitted:
    st.session_state.context = {
        'name': full_name,
        'email': email,
        'phone': phone,
        'experience': experience,
        'position': position,
        'location': location,
        'tech_stack': tech_stack,
        'stage': 'greeting'
    }
    greeting_prompt = get_greeting_prompt(full_name)
    greeting = generate_response(greeting_prompt)
    st.session_state.conversation.append(('bot', greeting))

# Chat section
st.subheader('Chat Window')
user_input = st.text_input('You:')

if st.button('Send') and user_input:
    if check_exit(user_input):
        st.write('Thank you for your time! TalentScout will contact you soon.')
        st.stop()

    st.session_state.conversation.append(('user', user_input))
    context = update_context(st.session_state.context, user_input)

    if context.get('stage') == 'tech_questions':
        prompt = get_tech_questions_prompt(context['tech_stack'])
    else:
        prompt = f"User said: {user_input}. Continue conversation."

    bot_reply = generate_response(prompt)
    st.session_state.conversation.append(('bot', bot_reply))

for role, message in st.session_state.conversation:
    if role == 'user':
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**TalentScout:** {message}")

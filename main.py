# import streamlit as st
# import requests
# from openai import OpenAI
# from io import BytesIO

# # Set page configuration
# st.set_page_config(
#     page_title="CodeAgent",
#     page_icon="🤖",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # CSS styling
# st.markdown("""
# <style>
# :root {
#     --primary: #2A2F4F;
#     --secondary: #917FB3;
#     --background: #FDE2F3;
#     --text: #2A2F4F;
# }

# .stChatInput textarea {
#     border: 2px solid var(--primary) !important;
# }

# .stButton button {
#     background: var(--primary) !important;
#     color: white !important;
#     border: none !important;
#     transition: transform 0.2s !important;
# }

# .stButton button:hover {
#     transform: scale(1.05) !important;
# }

# [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
#     background: white;
#     border-radius: 15px;
#     padding: 1rem;
#     margin: 0.5rem 0;
#     box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
# }

# .user-message {
#     background: var(--secondary);
#     color: white;
#     border-radius: 10px;
#     padding: 0.75rem;
#     margin-left: auto;
#     max-width: 80%;
# }

# .bot-message {
#     background: #E5BEEC;
#     border-radius: 10px;
#     padding: 0.75rem;
#     margin-right: auto;
#     max-width: 80%;
# }
# </style>
# """, unsafe_allow_html=True)

# # Initialize session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # API Keys (should use st.secrets in production)
# GROQ_API_KEY = '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'
# HF_API_KEY = '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'

# # Configure OpenAI client for Groq
# groq_client = OpenAI(
#     api_key=GROQ_API_KEY,
#     base_url="https://api.groq.com/openai/v1"
# )

# def groq_chat(prompt):
#     try:
#         completion = groq_client.chat.completions.create(
#             model="mixtral-8x7b-32768",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7
#         )
#         return completion.choices[0].message.content
#     except Exception as e:
#         return f"Error: {str(e)}"

# def generate_image(prompt):
#     try:
#         response = requests.post(
#             "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
#             headers={"Authorization": f"Bearer {HF_API_KEY}"},
#             json={"inputs": prompt}
#         )
#         image = BytesIO(response.content)
#         return image
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Header
# st.title("CodeAgent")
# model = st.selectbox(
#     "Select Model",
#     ("Groq (Text)", "HuggingFace (Image)"),
#     label_visibility="collapsed"
# )

# # Display chat messages
# for message in st.session_state.messages:
#     if message["type"] == "text":
#         if message["is_user"]:
#             st.markdown(f'<div class="user-message">{message["content"]}</div>', 
#                        unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="bot-message">{message["content"]}</div>', 
#                        unsafe_allow_html=True)
#     elif message["type"] == "image":
#         st.image(message["content"], caption=message["prompt"])

# # Chat input
# with st.form("chat_input_form"):
#     user_input = st.text_input("Enter your message...", key="user_input", 
#                               label_visibility="collapsed")
#     submitted = st.form_submit_button("Send")

# if submitted and user_input.strip():
#     # Add user message
#     st.session_state.messages.append({
#         "type": "text",
#         "content": user_input,
#         "is_user": True
#     })
    
#     # Generate response
#     if "Groq" in model:
#         response = groq_chat(user_input)
#         st.session_state.messages.append({
#             "type": "text",
#             "content": response,
#             "is_user": False
#         })
#     else:
#         image = generate_image(user_input)
#         if isinstance(image, BytesIO):
#             st.session_state.messages.append({
#                 "type": "image",
#                 "content": image,
#                 "prompt": user_input
#             })
#         else:
#             st.session_state.messages.append({
#                 "type": "text",
#                 "content": image,
#                 "is_user": False
#             })
    
#     # Rerun to update messages
#     st.rerun()

import streamlit as st
import requests
from openai import OpenAI
from io import BytesIO
from duckduckgo_search import DDGS

# Set page configuration
st.set_page_config(
    page_title="CodeAgent",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS styling
st.markdown("""
<style>
:root {
    --primary: #2A2F4F;
    --secondary: #917FB3;
    --background: #FDE2F3;
    --text: #2A2F4F;
}
.stChatInput textarea {
    border: 2px solid var(--primary) !important;
}
.stButton button {
    background: var(--primary) !important;
    color: white !important;
    border: none !important;
    transition: transform 0.2s !important;
}
.stButton button:hover {
    transform: scale(1.05) !important;
}
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
    background: white;
    border-radius: 15px;
    padding: 1rem;
    margin: 0.5rem 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.user-message {
    background: var(--secondary);
    color: white;
    border-radius: 10px;
    padding: 0.75rem;
    margin-left: auto;
    max-width: 80%;
}
.bot-message {
    background: #E5BEEC;
    border-radius: 10px;
    padding: 0.75rem;
    margin-right: auto;
    max-width: 80%;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# API Keys (should use st.secrets in production)
GROQ_API_KEY = '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'
HF_API_KEY = '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'

# Configure OpenAI client for Groq
groq_client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def groq_chat(prompt):
    try:
        completion = groq_client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception:
        return None

def duckduckgo_search(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=1))
            return results[0]["body"] if results else "No results found."
    except Exception:
        return "Search failed."

def generate_image(prompt):
    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
            headers={"Authorization": f"Bearer {HF_API_KEY}"},
            json={"inputs": prompt}
        )
        image = BytesIO(response.content)
        return image
    except Exception:
        return None

# Header
st.title("CodeAgent")
model = st.selectbox(
    "Select Model",
    ("Groq (Text)", "HuggingFace (Image)"),
    label_visibility="collapsed"
)

# Display chat messages
for message in st.session_state.messages:
    if message["type"] == "text":
        style = "user-message" if message["is_user"] else "bot-message"
        st.markdown(f'<div class="{style}">{message["content"]}</div>', unsafe_allow_html=True)
    elif message["type"] == "image":
        st.image(message["content"], caption=message["prompt"])

# Chat input
with st.form("chat_input_form"):
    user_input = st.text_input("Enter your message...", key="user_input", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    # Add user message
    st.session_state.messages.append({
        "type": "text",
        "content": user_input,
        "is_user": True
    })
    
    # Generate response
    response = groq_chat(user_input)
    if not response:
        response = duckduckgo_search(user_input)
    
    st.session_state.messages.append({
        "type": "text",
        "content": response,
        "is_user": False
    })
    
    # Rerun to update messages
    st.rerun()
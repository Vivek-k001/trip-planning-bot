import os
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError
import streamlit as st

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the key.")
    st.stop()

client = OpenAI(api_key=api_key)

initial_message = [
    {
        "role": "system",
        "content": "You are a travel assistant. Provide detailed and helpful trip planning advice, including recommendations for destinations, activities, accommodations, and travel tips. You are able to guide users to plan their vacations or business trips. Respond professionally, keeping responses concise (under 200 words). Always ask questions to understand user preferences and help them plan their trip effectively. Conclude with a day-wise itinerary."
    },
    {
        "role": "assistant",
        "content": "Hello! I'm your travel assistant. I can help you plan your trip, suggest destinations, activities, and accommodations. How can I assist you today?"
    }
]

def get_response_from_bot(messages):
    try:
        bot_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return bot_response.choices[0].message.content

    except RateLimitError as e:
        st.error("Quota exceeded. Please check your OpenAI usage or billing settings.")
        return None
    
    except Exception as e:
        st.error(f"An error occurred: {e[0].message}")
        return None
    
    
if "messages" not in st.session_state:
    st.session_state.messages = initial_message

st.title("Travel Assistant Chatbot")

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_input = st.chat_input("Enter your message here...")

if user_input:
    user_message = {
        "role": "user",
        "content": user_input
    }

    st.session_state.messages.append(user_message)

    with st.chat_message(user_message["role"]):
        st.markdown(user_message["content"])

    with st.spinner("Thinking..."):
        bot_response = get_response_from_bot(st.session_state.messages)

    if bot_response:
        bot_message = {
            "role": "assistant",
            "content": bot_response
        }

        st.session_state.messages.append(bot_message)

        with st.chat_message(bot_message["role"]):
            st.markdown(bot_message["content"])
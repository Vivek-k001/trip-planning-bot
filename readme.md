# 🧭 Trip Planning Bot

A simple chatbot interface powered by OpenAI's API to assist users in planning trips or answering travel-related queries.

---

## 🚀 Setup Instructions

Follow these steps to get started:

1. **Create an OpenAI API Account**  
   - Visit [OpenAI's website](https://platform.openai.com/signup) and sign up for an API account.

2. **Generate Your API Key**  
   - After logging in, go to the API section and generate a new key.

3. **Create a Secure `.env` File**  
   - In your project root, create a `.env` file to store sensitive credentials.

4. **Store Your API Key**  
   - Add the following line to your `.env` file:  
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

5. **Refer to OpenAI Documentation**  
   - Review [OpenAI's API documentation](https://platform.openai.com/docs) for endpoint usage, rate limits, and best practices.

---

## 🛠️ Implementation Plan

This bot is built with a simple UI and backend logic to interact with OpenAI's API:

1. **Display Chat Messages**  
   - Render a scrollable message window showing user and bot interactions.

2. **Textbox for User Input**  
   - Provide an input field for users to type their queries.

3. **Send Input to OpenAI**  
   - On submit, send the user's message to OpenAI's API using the stored key.

4. **Store and Display Responses**  
   - Save the response in a message list and update the UI to show the bot's reply.

---

## 📦 Project Structure


# Local-LLM_Chatbot

## Overview
This project implements a free-to-use, locally running, privacy-aware chatbot using Streamlit and GPT4All. The chatbot does not require a GPU or an internet connection, ensuring privacy and accessibility. The application allows users to interact with different language models, manage chat sessions, and maintain chat histories, all within a user-friendly Streamlit interface.

## Features
- **Local Execution**: Runs entirely on your local machine, ensuring full control over your data and conversations. No need for internet connectivity.
- **Privacy-Aware**: As the chatbot operates offline, your data remains private and secure.
- **Streamlit Interface**: Provides an intuitive and interactive web interface for chatting and managing sessions.
- **Multiple Model Support**: Choose from a variety of language models to tailor the chatbot's responses to your needs.
- **Session Management**: Easily create, switch, and manage multiple chat sessions.
- **Chat History**: Automatically saves chat history to a CSV file, allowing for easy retrieval and review of past conversations.

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Mrx-Sachin/Local-LLM_Chatbot.git
   ```

2. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**:
   ```sh
   streamlit run chat.py --server.port  8080
   ```

## Usage
1. **Select a Model**: From the sidebar, choose a language model to download and use. The selected model will be cached and used for generating responses.
2. **Manage Sessions**:
   - **Create New Session**: Use the "New Chat Session" button to start a new conversation. Each session is uniquely identified and stored.
   - **Switch Sessions**: Select a session from the dropdown to load and continue previous conversations.
3. **Chat**: Type your messages and interact with the chatbot. The conversation history is displayed in the main panel.
4. **Chat History**: All chat sessions are saved in `chat_history.csv` for easy access and review.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements
- **Streamlit**: For providing a fantastic framework for building interactive web applications.
- **GPT4All**: For making powerful language models accessible without requiring GPUs.

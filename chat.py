import streamlit as st
import pandas as pd
import time
from gpt4all import GPT4All

st.title("Simple Chat")
st.sidebar.title("Chat History")

CSV_FILE = "chat_history.csv"

# Load chat history from CSV
try:
    chat_history_df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    chat_history_df = pd.DataFrame(columns=["ChatID", "Role", "Content"])

# Model selection and download
model_options = [
    "wizardlm-13b-v1.2.Q4_0.gguf",
    "mistral-7b-openorca.Q4_0.gguf",
    "gpt4all-falcon-newbpe-q4_0.gguf",
    "orca-mini-3b-gguf2-q4_0.gguf",
    "gpt4all-13b-snoozy-q4_0.gguf",
    "replit-code-v1_5-3b-newbpe-q4_0.gguf"
]

modelname = st.sidebar.selectbox("Select model to download:", model_options)

# Save the selected model to a file
with open("model.txt", "w") as f:
    f.write(modelname)

@st.cache_resource
def load_model(model_name):
    return GPT4All(model_name=model_name)

# Invalidate the cache if the model is changed
if 'cached_model_name' not in st.session_state or st.session_state.cached_model_name != modelname:
    if 'model' in st.session_state:
        del st.session_state['model']
    st.session_state.cached_model_name = modelname
    st.session_state.model = load_model(modelname)
else:
    st.session_state.model = st.session_state.model

model = st.session_state.model

# Sidebar - Chat History with new session button
if "chat_names" not in st.session_state:
    st.session_state.chat_names = ["Session 1"]

if "selected_chat" not in st.session_state:
    st.session_state.selected_chat = st.session_state.chat_names[0]

def new_chat_session():
    new_name = f"Session {len(st.session_state.chat_names) + 1}"
    st.session_state.chat_names.append(new_name)
    st.session_state.selected_chat = new_name
    st.session_state.messages = []

st.sidebar.text("Chat Sessions:")
st.session_state.selected_chat = st.sidebar.selectbox(
    "Select a chat session:",
    st.session_state.chat_names
)

if st.sidebar.button("New Chat Session"):
    new_chat_session()

# Load messages for the selected chat session
st.session_state.messages = chat_history_df[chat_history_df.ChatID == st.session_state.selected_chat].to_dict('records')

with model.chat_session():
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["Role"]):
            st.markdown(message["Content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"ChatID": st.session_state.selected_chat, "Role": "user", "Content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = model.generate(prompt=prompt, temp=0)
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"ChatID": st.session_state.selected_chat, "Role": "assistant", "Content": full_response})

        # Save chat history to CSV
        updated_chat_history_df = pd.DataFrame(st.session_state.messages)
        chat_history_df = pd.concat([chat_history_df, updated_chat_history_df]).drop_duplicates().reset_index(drop=True)
        chat_history_df.to_csv(CSV_FILE, index=False)




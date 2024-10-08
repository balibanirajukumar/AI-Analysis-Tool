from chatbot_chain import get_chatbot_chain
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Placeholder for storing user session state
if "authentication_status" not in st.session_state:
    st.session_state.authentication_status = None

# User credentials (in real apps, store them securely in a DB)
hashed_passwords = stauth.Hasher(["abc", "def"]).generate()

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)

name, authentication_status, username = authenticator.login()

if authentication_status:
    authenticator.logout("Logout", "main")
    if username == "raju":
        st.write(f"Welcome *{name}*")
    elif username == "rbriggs":
        st.write(f"Welcome *{name}*")  
    chain = get_chatbot_chain()
    
elif authentication_status == False:
    st.error("Username/password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password") 

 
# URL for the logo of the assistant bot
# We need it as a separate variable because it's used in multiple places
bot_logo = 'https://pbs.twimg.com/profile_images/1739538983112048640/4NzIg1h6_400x400.jpg'

# We use st.session_state and fill in the st.session_state.messages list
# It's empty in the beginning, so we add the first message from the bot
st.divider()
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "bot",
                                     "content": "Hello, how can I help?"}]
 
# Then we show all the chat messages in Markdown format
for message in st.session_state['messages']:
    if message["role"] == 'bot':
        with st.chat_message(message["role"], avatar=bot_logo):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# We ask for the user's question, append it to the messages and show below
if query := st.chat_input("Please ask your question here:"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
 
    # We create a new chat message and launch the "chain" for the answer
    with st.chat_message("assistant", avatar=bot_logo):
        message_placeholder = st.empty()
        result = chain.invoke({"question": query})
        message_placeholder.markdown(result['answer'])
 
    # We also add the answer to the messages history
    st.session_state.messages.append({"role": "bot", "content": result['answer']})

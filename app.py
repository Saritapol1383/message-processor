import streamlit as st

st.title("Message Processor")

message = st.text_input("Enter your message")

if st.button("Process Message"):
    st.write("you entered a message")
    st.write(message)
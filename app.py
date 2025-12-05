import streamlit as st
from textblob import TextBlob


st.title("Sentiment Analysis App")

st.write(" 🧠Enter a sentence to analyze its sentiment.")


user_input = st.text_input("Enter your sentence:")

if user_input:
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity


    if sentiment > 0:
        st.write("Sentiment Positive:) ")
    
    elif sentiment < 0:
        st.write("Sentiment Negastive :(")
    else:
        st.write("Sentiment Neutral :I")
    
    st.write(f"Sentiment Score : {sentiment}")




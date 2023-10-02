import streamlit as st


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Technical Researcher Bot - Documentation",
    page_icon="🤖",
    menu_items={
        'Report a bug': "https://github.com/Pranomvignesh/Technical-Researcher-Bot/issues"
    }
)
st.title("Documentation")

st.markdown("""
**This is a technical preview of the Technical Researcher bot**

- This application works by fetching technical papers from the topic provided using Metaphor's search API
- The PDF of the technical paper is fetched and extracted
- This extracted content forms the memory of the chatbot
- ConversationalRetrievalChain from LangChain is used to build the bot

**Author** - Vignesh Prakash - [LinkedIn](https://www.linkedin.com/in/pranomvignesh/)
""")


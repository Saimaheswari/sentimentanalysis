import streamlit as st
import streamlit.components.v1 as components


# Set page title
st.set_page_config(
    page_title="Sentiment Analysis on Social Media...",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
img{border-radius: 10px;}
</style> """, unsafe_allow_html=True)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)



st.markdown("## Sentiment Analysis on Social media ")
st.write("Sentiment analysis on Twitter involves analyzing tweets to determine the emotional tone expressed by users. Natural Language Processing (NLP) algorithms classify tweets as positive, negative, or neutral based on language cues. This process helps businesses gauge public opinion, track brand perception, and identify emerging trends. Challenges include handling sarcasm, slang, and context nuances, making it crucial for models to continuously adapt to evolving language use. Overall, Twitter sentiment analysis plays a pivotal role in understanding the dynamic and real-time sentiments of a diverse online community.")

import streamlit as st
import streamlit.components.v1 as components

# Set page title
st.set_page_config(
    page_title="Sentiment Analysis on Social Media",
    initial_sidebar_state="expanded",
)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,blue,Lime);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">Lung Cancer Detection</p>
    """,
    height=69,
)



def page_layout():
   
    st.write("Machine Learning Based Sentimental Analysis For Assessing Effectiveness Of Social Media Posts.")
    st.write("Developed By SVEC Students")
    st.markdown("## Benefits:")
    st.write("- Twitter sentiment analysis allows businesses to quickly identify and address negative sentiments, helping in the proactive management of their online reputation.")
    st.write("- Strategic Decision-Making: By gauging public opinion in real-time, companies can make informed strategic decisions, adapt marketing strategies, and stay ahead of market trends, contributing to overall business success.")
    
    st.markdown("## Use:")
    st.write("- Brand Monitoring")
    st.write("- Twitter sentiment analysis is primarily used for real-time brand reputation management and strategic decision-making, allowing businesses to promptly address customer concerns and stay ahead of market trends.")
# Render page layout
page_layout()

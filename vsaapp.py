import streamlit as st
from audio_recorder_streamlit import audio_recorder

# st.set_page_config(initial_sidebar_state="home")
# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "home"

opt = st.sidebar.radio("select page", options=("home", "login", "implementation"))

if opt == "home":
    st.markdown(
        """<h1 style='text-align: center'>Voice Sentiment Analysis Project</h1>
        <style>
        .stDeployButton{
        display: None
        }
        .st-emotion-cache-6q9sum.ef3psqc4{
            display: None
        }
        .st-emotion-cache-cio0dv.ea3mdgi1{
            display: None
        }
        </style>""", unsafe_allow_html=True)
    st.image("image 2.png", width=400)
    st.markdown(
        """
        <style>
        div[data-testid="stImage"] img {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.text("Welcome to the Voice Sentiment Analysis project! This web application allows you to\nrecord your voice and scores it to predict its sentiment")
elif opt == "login":
    st.markdown(
            """<h1 style='text-align: center'>Register Here</h1>
            <style>
            .stDeployButton{
            display: None
            }
            .st-emotion-cache-6q9sum.ef3psqc4{
                display: None
            }
            .st-emotion-cache-cio0dv.ea3mdgi1{
                display: None
            }
            </style>""", unsafe_allow_html=True)
    with st.form("Form",clear_on_submit=True): 
        col1,col2=st.columns(2)
        f_name=col1.text_input("First Name")
        l_name=col2.text_input("Last Name")
        contact=st.text_input("Contact")
        day,month,year=st.columns(3)
        # day.text_input("Day")
        d=day.selectbox("Day",options=range(1,32))
        # month.text_input("Month")
        m=month.selectbox("Month",options=range(1,13))
        # year.text_input("Year")
        y=year.selectbox("Year",options=range(2000,2024))
        email=st.text_input("E-Mail Address")
        pw=st.text_input("Password",type='password')
        pwc=st.text_input("Confirm Password",type='password')
        s_state=st.form_submit_button("Submit")
        if s_state:
            if f_name=="" and l_name=="" and email=="" and pw=="" and pwc=="":
                st.warning("Please fill above fields")
            else:
                st.success("Submitted Successfully")
            if pw!=pwc:
                st.warning("Passwords do not match")

elif opt == "implementation":
    st.markdown(
        """<h1 style='text-align: center'>Implementation</h1>
        <style>
        .stDeployButton{
        display: None
        }
        .st-emotion-cache-6q9sum.ef3psqc4{
            display: None
        }
        .st-emotion-cache-cio0dv.ea3mdgi1{
            display: None
        }
        </style>""", unsafe_allow_html=True)
    st.markdown("""
            ### Tips:
            * Click the "Record Audio" button to start recording your voice.
            * Speak clearly to get accurate sentiment analysis results.
            * Analyzed sentiment results will be displayed below.""")
    st.markdown("---")
    audio_placeholder = st.empty()

    box=st.radio("how do you want to give audio sample",options=["upload audio","record audio"])

    if box=="record audio":
        sample = audio_recorder(text="Click to record",icon_size="0.5x",sample_rate=44100)
        st.audio(sample, format='audio/wav')
    else:
        sample=st.file_uploader("upload audio file",type=["wav","mp3"])
        st.audio(sample)

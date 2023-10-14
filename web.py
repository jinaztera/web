import streamlit as st
import numpy as np
import time
import os




tab1, tab2 = st.tabs(["문제", "해설"])
tab2.write("해설")

st.sidebar.header("기출문제 조회")
with st.sidebar:    
    year = st.slider("연도", 2006, 2023)
    grade = st.sidebar.selectbox(
    "학년",
    ("고1", "고2", "고3")
    )
    if grade == "고3":
        month = st.sidebar.selectbox(
        "월",
        ("3월", "6월", "6월", "7월", "9월", "10월", "수능")
        )
    else:
        month = st.sidebar.selectbox(
        "월",
        ("3월", "6월", "9월", "11월")
        )
    
    if grade == "고1":
        subject = "수학"
    
    if grade == "고2":
        if year < 2012 or (year > 2015 and year < 2020):
            subject = st.sidebar.selectbox(
            "과목",
            ("수학가형", "수학나형")
            )
        elif year > 2011 and year <2016:
            subject = st.sidebar.selectbox(
            "과목",
            ("수학A", "수학B")
            )
        else:
            subject = "수학"
            # st.text("과목")
            # st.title("수학")
            # subject = "수학"
    
    if grade == "고3":
        if year < 2011:
            subject = st.sidebar.selectbox(
            "과목",
            ("수학가형", "수학나형", "수리가형-이산수학", "수리가형-확률과통계")
            )
        if year > 2010 and year < 2021:
            subject = st.sidebar.selectbox(
            "과목",
            ("수학가형", "수학나형")
            )
        if year > 2012 and year < 2016:
            subject = st.sidebar.selectbox(
            "과목",
            ("수학A", "수학B")
            )
        if year > 2020:
            subject = st.sidebar.selectbox(
            "과목",
            ("미적분", "확률과통계", "기하")
            )
        
    number = st.number_input("문제번호", 1, 30)

    if month == "수능":
        even_odd = st.radio("홀짝", ["홀", "짝"])

    if month == "수능":        
        file_name = f"{year}_{grade}_{month}_{subject}_{even_odd}_{number}"
    else:
        file_name = f"{year}_{grade}_{month}_{subject}_{number}"
    
    # if st.button('조회'):
if file_name + ".png" not in os.listdir("image"):
    tab1.title("준비중입니다")
else:
    tab1.image("image/" + file_name + ".png")

# print(file_name)   
# hello world
# st.chat_input("준비중입니다")
print(file_name + ".png")

  
 

# 2023_고2_6월_수학_13.png
# tab1.image("image/" + file_name + ".png")


# st.button("Reset", type="primary")
# if st.slider.button('조회'):
#     tab1.image("image/" + file_name + ".png")
    


# with st.chat_message("user"):
    # st.write("Hello 👋")
    # st.line_chart(np.random.randn(30, 3))
  
# st.chat_input("Say something")


# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
# a = st.radio('Select one:', [1, 2])

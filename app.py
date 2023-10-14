
import streamlit as st
import numpy as np
import time

# st.write("Hello, world!")
# st.text('Fixed width text')
# st.markdown('_Markdown_') # see *
# #라텍스 문자
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.write('Most objects') # df, err, func, keras!
# st.write(['st', 'is <', 3]) # see *
# #타이틀
# st.title('My title')
# #제목
# st.header('My header')
# #부제목
# st.subheader('My sub')
# ## 코드
# st.code('for i in range(8): foo()')


st.sidebar.write("hello")
with st.sidebar:
    st.write('hello, world')
    st.write('Hello')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
a = st.radio('Select one:', [1, 2])



with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

# # Or use "with" notation:
# with st.sidebar:
#     st.radio('Select one:', [1, 2])
# st.text(a)
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab2", "Tab3"])

tab1.write("this is tab 1")
tab2.write("this is tab 2")
tab3.write("this is tab 2")
tab1.latex(r''' e^{i\pi} + 1 = 0 ''')

# # Stop execution immediately:
# st.stop()
# # Rerun script immediately:
# st.rerun()

with st.form(key='my_form'):
   username = st.text_input('Username')
   password = st.text_input('Password')
   st.form_submit_button('Login')

# print(username)
# print(password)

st.button("Click me")
# st.download_button("Download file", data)
# st.link_button("Go to gallery", url)
# st.data_editor("Edit data", data)
st.checkbox("I agree")
st.toggle("Enable")
st.radio("Pick one", ["cats", "dogs"])
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
# st.camera_input("Take a picture")
st.color_picker("Pick a color")

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
    st.write("hi")

with st.chat_message("assignment"):
    st.write("hello")

st.chat_input("Say something")

# st.balloons()
# st.snow()
st.toast('Warming up...')
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
# st.exception(e)

# def foo(bar):
#     return data
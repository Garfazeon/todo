import streamlit as st
import functions

todos = functions.get_todos()

st.title('My to-do App')
st.subheader('This is my todo app')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='',placeholder='Add a new todo...')
import streamlit as st
from streamlit import text_input

import functions
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title('My to-do App')
st.subheader('This is my todo app')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='',placeholder='Add a new todo...',
              on_change=add_todo,key='new_todo')


import streamlit as st
import pandas as pd

# normal way with st.write 
st.write("Hello **world**!")

# magic commands 
"Hello **world**!"

# Text elements

# st.header 
st.header('This is a header')

# st.subheader 

st.subheader('This is a subheader')

# st.caption

st.caption('This is a string that explains something above.')

# st.code 

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')

# st.text 

st.text('This is some text.')

# st.latex 

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

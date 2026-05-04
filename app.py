import streamlit as st

st.title("Cloud IDE")

code = st.text_area("Write code")

if st.button("Run"):
    try:
        exec(code)
        st.success("Success")
    except Exception as e:
        st.error(str(e))

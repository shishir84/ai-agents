import streamlit as st
from flows.dev_team_flow import run_dev_team

st.title("👨‍💻 AI Dev Team")

query = st.text_area("Enter requirement")

if st.button("Build"):
    result = run_dev_team(query)
    st.write(result)
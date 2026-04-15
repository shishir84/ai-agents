import streamlit as st
from services.orchestrator import route_request

st.title("📞 Support Agent")

ticket = st.text_area("Enter support issue")

if st.button("Analyze"):
    result = route_request("support", ticket)
    st.write(result)
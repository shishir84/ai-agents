import streamlit as st
from services.orchestrator import route_request

st.title("🧑‍💼 Hiring Assistant")

resume = st.text_area("Paste Resume")

if st.button("Evaluate"):
    result = route_request("hiring", resume)
    st.write(result)
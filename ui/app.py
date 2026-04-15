import streamlit as st

st.set_page_config(page_title="AI Agents", layout="wide")

st.title("🤖 Agentic AI System")

pages = {
    "Dev Team": "dev_team",
    "Hiring Assistant": "hiring",
    "Support Agent": "support"
}

for name, page in pages.items():
    if st.button(name):
        st.switch_page(f"pages/{page}.py")
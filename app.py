import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Imuta",
    page_icon="📚",
    layout="wide"
)

# Application heading
st.title("📚 Imuta")
st.subheader("Learn smarter. Grow further.")

st.write(
    "Welcome to Imuta, your intelligent "
    "study management companion."
)

st.divider()

# Dashboard
st.header("Your Learning Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Subjects", 0)

with col2:
    st.metric("Topics Completed", 0)

with col3:
    st.metric("Study Hours", 0)

st.info("Your academic journey starts here!")
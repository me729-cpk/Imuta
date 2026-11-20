import streamlit as st

from models.subject import Subject
from models.topic import Topic
from core.study_manager import StudyManager
from models.study_session import StudySession
from datetime import datetime, date


# Page configuration
st.set_page_config(
    page_title="Imuta",
    page_icon="📚",
    layout="wide"
)

#Initialise Imuta
if "manager" not in st.session_state:
    st.session_state.manager = StudyManager()
    math = Subject("Mathematics")
    physics = Subject("Physics")
    chemistry = Subject("Chemistry")

    #Add topics

    math.add_topic(Topic("Algebra", "Hard"))
    math.add_topic(Topic("Geometry", "Easy"))

    physics.add_topic(Topic("Motion", "Medium"))
    physics.add_topic(Topic("Energy", "Hard"))

    chemistry.add_topic(Topic("Atomic Structure", "Medium"))

    #Add subjects to manager

    st.session_state.manager.add_subject(math)
    st.session_state.manager.add_subject(physics)
    st.session_state.manager.add_subject(chemistry)

manager = st.session_state.manager


# Interface
st.title("📚 Imuta")
st.subheader("Learn smarter. Grow further.")

st.write(
    "Welcome to Imuta, your intelligent "
    "study management companion."
)

st.divider()

# Dashboard
st.header("Your Learning Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Subjects", manager.total_number_of_subjects())

with col2:
    st.metric("Topics Completed", manager.total_completed())

with col3:
    st.metric("Overall Progress", f"{manager.overall_progress()}%")

with col4:
    st.metric("Study Time", f"{manager.total_study_hrs():.2f} hrs")


st.divider()

st.header("Your Subjects")

for subject in manager.subjects:
    st.subheader(subject.name)

    st.progress(subject.calculate_progress() / 100)

    st.caption(f"{subject.completed_number()} of {subject.total()} topics completed")

st.divider()

st.header("📖 Record a Study Session")

subject_names = [subject.name for subject in manager.subjects]


selected_subject = st.selectbox(
    "Choose a subject",
    subject_names
)

selected_subject_object = next(
    subject for subject in manager.subjects
    if subject.name == selected_subject
)

topic_names = [topic.name for topic in selected_subject_object.topics]

selected_topic_name = st.selectbox(
    "What topic did you study",
    topic_names
)

selected_topic_object = next(
    topic for topic in selected_subject_object.topics
    if topic.name == selected_topic_name
)

start_time = st.time_input("Study start time")
end_time = st.time_input("Study end time")

start_datetime = None
end_datetime = None

if start_time is not None and end_time is not None:
    start_datetime = datetime.combine(date.today(), start_time)
    end_datetime = datetime.combine(date.today(), end_time)

if st.button("Record Study Session"):
    if not selected_topic_name.strip():
        st.warning("Please enter a topic")

    elif start_datetime is None or end_datetime is None:
        st.warning("Please select both times")

    elif start_datetime >= end_datetime:
        st.error("End time must be later than start time.")

    else:
        session = StudySession(selected_subject, selected_topic_name, start_datetime, end_datetime)

        manager.add_sessions(session)

        st.success("Study session recorded successfully")

        st.rerun()

st.divider()

st.header("📚 Your Study Sessions")

for session in manager.sessions:
    st.write(f"**Subject:**  {session.subject}")
    st.write(f"**Topic:**  {session.topic}")
    st.write(f"**Duration:**  {int(session.duration)} minutes")
    st.divider()
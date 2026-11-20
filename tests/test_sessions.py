from datetime import datetime

from models.subject import Subject
from models.topic import Topic
from models.study_session import StudySession
from core.study_manager import StudyManager


manager = StudyManager()

# Create subjects
physics = Subject("Physics")
math = Subject("Mathematics")
chemistry = Subject("Chemistry")

# Create topics
motion = Topic("Motion", "Medium")
algebra = Topic("Algebra", "Hard")
acids = Topic("Acids", "Easy")

# Connect topics to their subjects
physics.add_topic(motion)
math.add_topic(algebra)
chemistry.add_topic(acids)

# Create study sessions
session1 = StudySession(
    physics,
    motion,
    datetime(2026, 11, 20, 9, 0),
    datetime(2026, 11, 20, 9, 45)
)

session2 = StudySession(
    math,
    algebra,
    datetime(2026, 11, 20, 10, 0),
    datetime(2026, 11, 20, 11, 0)
)

session3 = StudySession(
    chemistry,
    acids,
    datetime(2026, 11, 20, 12, 0),
    datetime(2026, 11, 20, 12, 30)
)

# Add sessions to the manager
manager.add_sessions(session1)
manager.add_sessions(session2)
manager.add_sessions(session3)

print(f"Total study time: {int(manager.total_study_time())} minutes")
print(f"Total study hours: {manager.total_study_hrs()} hrs")
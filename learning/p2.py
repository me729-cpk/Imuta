from models.topic import Topic
from models.subject import Subject
# from abc import ABC, abstractmethod

#
#
# class LearningActivity(ABC):
#     def __init__(self, name, duration):
#         self.name = name
#         self.duration = duration
#
#     @abstractmethod
#     def display_details(self):
#         print(f"Session: {self.name}")
#         print(f"Duration: {self.duration} minutes")
#
# class StudySession(LearningActivity):
#     def __init__(self, name, duration, subject):
#         super().__init__(name, duration)
#         self.subject = subject
#
#     def display_details(self):
#         super().display_details()
#         print(f"Subject: {self.subject}")
#
# class RevisionSession(LearningActivity):
#     def __init__(self, name, duration, topic):
#         super().__init__(name, duration)
#         self.topic = topic
#
#     def display_details(self):
#         super().display_details()
#         print(f"Topic: {self.topic}")
#
#
# # revision1 = StudySession("Evening Session", 45, "Mathematics")
# # revision2 = RevisionSession("Evening Session", 45, "Algebra")
# #
# # revision1.display_details()
# # print("\n")
# # revision2.display_details()
#
#
# activities = [
#
#     StudySession("Morning Session", 60, "Physics"),
#     RevisionSession("Evening Session", 45, "Algebra"),
#     StudySession("Afternoon Study", 30, "Chemistry")
#
# ]
#
# for session in activities:
#     session.display_details()
#     print()




# class StudySession:
#     def __init__(self, name, duration):
#         self.name = name
#         self.duration = duration
#
# class StudyPlanner:
#     def __init__(self, ):
#         self.sessions = []
#
#     def add_session(self, session):
#         self.sessions.append(session)
#
#     def display_sessions(self):
#         for session in self.sessions:
#             print(f"Subject: {session.name}")
#             print(f"Duration: {session.duration} minutes")
#             print()
#
# math = StudySession("Mathematics", 60)
# physics = StudySession("Physics", 45)
# chemistry = StudySession("Chemistry", 50)
#
# sp = StudyPlanner()
# sp.add_session(math)
# sp.add_session(physics)
# sp.add_session(chemistry)
#
# sp.display_sessions()


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.subjects = []
#
#     def add_subject(self,subject):
#         self.subjects.append(subject)
#
#     def return_list(self):
#         return self.subjects
#
# class StudyGroup:
#     def __init__(self, students):
#         self.students = students
#
#     def display_names(self):
#         for student in self.students:
#             print(student.name)
#
#
# student1 = Student("Mia")
# student2 = Student("Paul")
# student3 = Student("Shai")
#
# student1.add_subject("Mathematics")
# student1.add_subject("English")
# student1.add_subject("E-ICT")
#
# student2.add_subject("CAD")
# student2.add_subject("Social Studies")
# student2.add_subject("French")
#
# student3.add_subject("Lingustics")
# student3.add_subject("Critical Thinking")
# student3.add_subject("Totomatics")
#
#
#
# SG = StudyGroup([student1, student2, student3])
#
# SG.display_names()










# manager = StudyManager()
#
# math = Subject("Mathematics")
# physics = Subject("Physics")
# chemistry = Subject("Chemistry")
#
# manager.add_subject(math)
# manager.add_subject(physics)
# manager.add_subject(chemistry)
#
# math.add_topic(Topic("Algebra", "Hard"))
# math.add_topic(Topic("Geometry", "Easy"))
#
# physics.add_topic(Topic("Motion", "Medium"))
# physics.add_topic(Topic("Electricity", "Hard"))
#
# chemistry.add_topic(Topic("Acids", "Easy"))
#

# math.topics[0].mark_completed()
# print(math.topics[0].completed)
# physics.topics[0].mark_incompleted()
# print(f"{physics.topics[0].completed}\n")
#
# print(f"Completed: {manager.total_completed()}")
# print(f"Total topics: {manager.overall_total()}")
# print(f"Overall progress: {manager.overall_progress()}%")
#
# topic1 = Topic("Algebra", "Hard")
#
# print(topic1.completed)  # False
#
# topic1.completed = True
#
# print(topic1.completed)
#
# topic1.completed = False

# for topic_content in topic_list:
#     try:
#         topic = Topic(
#             topic_content["name"],
#             topic_content["difficulty"]
#         )
#
#         math.add_topic(topic)
#
#     except ValueError as error:
#         print(error)
#
# math.topics[0].completed = True
# math.summary()
#
# math.display_topics_status()
# math.summary()



# topic1 = Topic("Algebra", "Hard")
# topic2= Topic("Calculus", "Very Hard")
# topic3 = Topic("Word Problem", "Easy")
#
# math = Subject("Mathematics")
#
# topic2.completed = True
# topic3.completed = True
#
#
# math.add_topic(topic1)
# math.add_topic(topic2)
# math.add_topic(topic3)

# for topic in math.topics:
#     try:
#         math.display_topics_status()
#         progress = math.calculate_progress()
#         print(f"\nProgress Percentage: {round(progress, 2)}")
#
#     except ValueError as error:
#         print(error)

math = Subject("Mathematics")

topic1 = Topic("Algebra", "Hard")
topic2 = Topic("Geometry", "Easy")

math.add_topic(topic1)
math.add_topic(topic2)

math.topics[0].mark_completed()

math.summary()
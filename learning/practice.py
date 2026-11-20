# import streamlit as st
#
# st.set_page_config(
#     page_title ="Imuta",
#     page_icon = ""
# )
#
# subjectsList = ["Mathematics","Physics","Chemistry","English","E-ICT"]
#
# total_topics = 50
# completed_topics = 32
# previous_completed = 25
#
# total_number_of_subjects = len(subjectsList)
#
# number_of_remaining_topics = total_topics - completed_topics
#
# completed_percentage = (completed_topics/total_topics) * 100
#
# relative_change_of_completed_to_previous = completed_topics - previous_completed
#
# st.title("Imuta")
#
# st.subheader("Student Dashboard")
#
# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.metric("Number Of Subjects", total_number_of_subjects)
#
# with col2:
#     st.metric("Topics Completed", completed_topics, delta = relative_change_of_completed_to_previous)
#
#
# with col3:
#     st.metric("Topics Remaining", number_of_remaining_topics)
#
# if completed_percentage < 40:
#     st.warning("More Work Needed")
# elif 75 > completed_percentage >= 40:
#     st.info("Good Progress")
# elif 100 > completed_percentage >= 75:
#     st.info("Almost There")
# elif completed_percentage == 100:
#     st.success("Syllabus Completed")
#
# subjectsList.append("Biology")
#
# for subject in subjectsList:
#     st.write(subject)





# subjects = [
#
#     {
#         "name" : "Mathematics",
#        "progress" : {"total_topics" : 15,
#         "completed_topics" : 8}
#
#     },
#
#     {
#             "name" : "Physics",
#             "progress" : {"total_topics" : 20,
#             "completed_topics" : 12}
#         }
#
# ]






#
# new_subject1, new_subject2, new_subject3= {"name": "Chemistry","total_topics": 18,"completed_topics": 0},{"name" : "English","total_topics" : 12,"completed_topics" : 3},{"name" : "E-ICT","total_topics" : 10,"completed_topics" : 0}
#
#
#
# subjects.append(new_subject1)
# subjects.append(new_subject2)
# subjects.append(new_subject3)
#
# for subject in subjects:
#     print(f"{subject["name"]} - {subject["completed_topics"]} completed")







# def calculate_percentage(completed, total):
#
#     if total < 0:
#         raise ValueError("Total Topics Cannot Be Negative '-'")
#
#     if completed < 0:
#         raise ValueError("Completed Topics Cannot Be Negative '-'")
#
#     if completed > total:
#         raise ValueError("Completed Topics Cannot Be Greater Than Total Topics")
#
#     if total == 0:
#         return 0
#
#     return (completed/total) * 100
#
#
# def overall_percentage(subject_list):
#     completed_total = 0
#     total_total = 0
#     for subject in subject_list:
#         completed_total += subject["progress"]["completed_topics"]
#         total_total += subject["progress"]["total_topics"]
#
#     total_percent =calculate_percentage(completed_total, total_total)
#
#     return round(total_percent, 2)
#
# def calculate_all_subjects_progress(subjectList):
#
#     progress_list = [{subject["name"] : round(calculate_percentage(subject["progress"]["completed_topics"], subject["progress"]["total_topics"]), 2)} for subject in subjectList]
#
#     return progress_list




#
#
#
# math_percentage = calculate_percentage(8,15)
# physics_percentage = calculate_percentage(12, 20)
#
# print(math_percentage)
# print(physics_percentage)
#
# print(calculate_percentage(0, 0))
#
# new_list1, new_list2 = [subject["name"] for subject in subjects], [subject["progress"]["completed_topics"] for subject in subjects]
# print(new_list1)
# print(new_list2)
#
# print(calculate_all_subjects_progress(subjects))
# print(f"Overall Completion: {overall_percentage(subjects)}")





# numbers = [5, 10, 15, 20, 25, 30]
#
# result = list(map(lambda y : 2 * y,filter(lambda x: x > 15, numbers)))
#
# print(result)



# subject = [
#
#     {"name" : "Mathematics", "percentage" : 35},
#     {"name" : "Physics", "percentage" : 60},
#     {"name" : "Chemistry", "percentage" : 80},
#     {"name" : "English", "percentage" : 25}
#
# ]


# below_50 = list(
#     filter(
#         lambda x : x["percentage"] < 50, subject
#     )
# )
#
# print(below_50)





# below_50 = list(filter(lambda x : x["percentage"] < 50, subject))
#
# sorted_below_50 = sorted(below_50, key = lambda y : y["percentage"])
#
# print(below_50)
# print(sorted_below_50)



# subjects = ["Mathematics", "Physics", "Chemistry", "English"]
# percentages = [35, 60, 80, 25]
#
#
# for subject, percentage in zip(subjects, percentages):
#     if percentage < 50:
#         print(subject, percentage)
#
#     else:
#         continue




# from progress import calculate_percentage as cp
#
# result = cp(8,15)
# print(result)



# from progress import student_details as sd
# sd(name = "Bruno", age = 17, school = "Imuta")
#
#
# from progress import display_name as dn
# dn(name="Mathematics", percentage = 75)
#
# from progress import display_percent as dp
# dp(name="Physics", percentage = "60", difficulty = "Hard")



# from progress import example as e
# e()
# from progress import example2 as e2
# e2()


# file = open("student.txt", "w")
# file.write("Bruno is a big boy, e ya e ya ooooo")
# file.close()
# with open("imuta.txt", "w") as file1:
#     file1.write("Welcome To Imuta")
#
# with open("subjects.txt", "w") as file:
#     file.write("Mathematics\nPhysics")
#
# with open("subjects.txt", "a") as file1:
#     file1.write("\nChemistry")
#
# with open("subjects.txt", "r") as file2:
#     content = file2.read()
#
# print(content)


import json as js

# subject_data = {
#
#     "name" : "Mathematics",
#     "total_topics" : 20,
#     "completed_topics" : 12,
#     "difficulty" : "hard"
#
# }
#
#
# with open("subject.json", "w") as file:
#     js.dump(subject_data, file, indent=4)
#
# with open("subject.json", "r") as file:
#     final_file = js.load(file)
#
#     print(f"{final_file["name"]} | {final_file["completed_topics"]}")

# with open("subject.json", "r") as file:
#     content = js.load(file)
#
# content["completed_topics"] += 2
# content["difficulty"] = "medium"
#
# with  open("subject.json", "w") as file:
#     js.dump(content, file, indent=4)
#
# print(content)


subjects = [

    {"name" : "Mathematics", "total_topics" : 20, "completed_topics" : 12},
    {"name" : "Physics", "total_topics" : 15, "completed_topics" : 8},
    {"name" : "Chemistry", "total_topics" : 18, "completed_topics" : 5 }

]

# with open("subjects.json", "w") as file:
#     js.dump(subjects, file, indent=4)

with open("subjects.json", "r") as file:
    saved_subjects = js.load(file)
#
#
# saved_subjects[0]["completed_topics"] += 2

# with open("subjects.json", "w") as file:
#     js.dump(saved_subjects, file, indent=4)


# for subject in saved_subjects:
#     if subject["name"] == "Mathematics":
#         subject["completed_topics"] += 2
#         break
#
#
# with open("subjects.json", "w") as file:
#     js.dump(saved_subjects, file, indent=4)


# try:
#     number = int("hello")
#
# except ValueError:
#     print("Invalid")
#
# else:
#     print("Success")
#
# finally:
#     print("Finished")
#
#
# try:
#     result = 10/0
#
# except ZeroDivisionError:
#     print("Cannot divide by Zero")
#
# finally:
#     print("Calculation complete")






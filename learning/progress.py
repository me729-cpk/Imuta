def calculate_percentage(completed, total):
    if total == 0:
        return 0

    return round((completed/total) * 100, 2)



def student_details(**details):
    print(details)



def display_name(**data):
    print(data["name"])
def display_percent(**data):
    print(data["percentage"])



def example(*args):
    print(type(args))

def example2(**kwargs):
    print(type(kwargs))



def update_progress(subject, amount):
    if amount < 0:
        raise ValueError("Amount cannot br negative")

    try:
        subject["completed_topics"] += amount

    except KeyError:
        print("Subject data is missing a required field")

    except TypeError:
        print("Invalid progress value.")

class Book:
    def __init__(self, title):
        self.title = title

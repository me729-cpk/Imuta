

class StudySession:
    def __init__(self, subject, topic, start_time,end_time):
        if end_time <= start_time:
            raise ValueError("End time must be later than start time")

        self.subject = subject
        self.topic = topic
        self.start_time = start_time
        self.end_time = end_time


        self.duration = (end_time - start_time).total_seconds() / 60


    def display_session(self):
        print(f"Subject: {self.subject.name}")
        print(f"Topic: {self.topic.name}")
        print(f"Start: {self.start_time.strftime('%I:%M %p')}")
        print(f"End: {self.end_time.strftime('%I:%M %p')}")
        print(f"Duration: {int(self.duration)} minutes")



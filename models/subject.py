from .topic import Topic

class Subject:
    def __init__(self, name):
        self.name = name
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def display_topics_status(self):
        print(f"Subject: {self.name}")
        print("Topics:")

        for topic in self.topics:
            print(
                f"{topic.name} | {topic.difficulty} | "
                f"Completed: {topic.completed}"
            )


    def total(self):
        return len(self.topics)

    def completed_number(self):
        number = 0
        for item in self.topics:
            if item.completed:
                number +=1

        return number

    def remaining_topics(self):
        return self.total() - self.completed_number()


    def calculate_progress(self):
        if self.total() == 0:
            return 0
        return round((self.completed_number() / self.total()) * 100, 2)

    def summary(self):
        print(f"Subject: {self.name}")
        print(f"Number of total topics: {self.total()}")
        print(f"Number of completed topics: {self.completed_number()}")
        print(f"Number of topics remaining: {self.remaining_topics()}")
        print(f"Progress Percentage: {self.calculate_progress()}%")

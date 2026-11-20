from progress import calculate_percentage as cp

class Subject:
    subject_type = "Academic Subject"

    def __init__(self, name, total_topics, completed_topics):
        if total_topics < 0:
            raise ValueError("Total topics cannot be negative")

        if completed_topics < 0 or completed_topics > total_topics:
            raise ValueError("Invalid input for the completed topics")

        self.name = name
        self.total_topics = total_topics
        self.__completed_topics = completed_topics

    #Getter
    @property
    def completed_topics(self):
        return self.__completed_topics

    #Setter
    @completed_topics.setter
    def completed_topics(self, new_value):
        if new_value > self.total_topics or new_value < 0:
            raise ValueError("Invalid completed topics input")

        self.__completed_topics = new_value

    def calculate_progress(self):
        if self.total_topics == 0:
            return 0

        return (self.__completed_topics / self.total_topics) * 100

    def complete_topic(self):
        if self.__completed_topics >= self.total_topics:
            return False

        self.__completed_topics += 1
        return True

    def display_details(self):
        print(self.name)
        print(f"The total number of topics you have to study is {self.total_topics}")
        print(f"The number of completed topics is {self.__completed_topics}")
        print(f"Your progress percentage is {self.calculate_progress()}%")

    @classmethod
    def new_entry(cls, name, total_topics):
        return cls(name, total_topics, 0)

    @staticmethod
    def is_good_percentage(percentage):
        return percentage >= 75


math = Subject("Mathematics", 20, 12)
physics = Subject("Physics", 15, 8)
chemistry = Subject("Chemistry", 18, 5)


subjects = [math, physics, chemistry]

completed_sum = sum([subject.completed_topics for subject in subjects])

total_sum = sum([subject.total_topics for subject in subjects])

print(f"The overall total number of topics is {total_sum}")
print(f"The overall number of completed topics is {completed_sum}")

print(f"The overall progress percentage is {cp(completed_sum, total_sum)}%")
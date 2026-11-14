class Topic:
    def __init__(self, name, difficulty, ):
        if difficulty.lower() not in ["hard", "medium", "easy"]:
                raise ValueError("Invalid Difficulty")

        self.name = name
        self.difficulty = difficulty.lower()
        self.__completed = False

    def display_topic(self):
        print(f"Topic: {self.name}")

    @property
    def completed(self):
        return self.__completed

    @completed.setter
    def completed(self, value):
        if not isinstance(value,bool):
            raise ValueError("Completed must be True or False")

        self.__completed = value

    def mark_completed(self):
        self.completed = True

    def mark_incompleted(self):
        self.completed = False




class StudyManager:
    def __init__(self):
        self.subjects = []
        self.sessions = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def total_number_of_subjects(self):
        return len(self.subjects)

    def display_subject(self):

        for subject in self.subjects:
            print(subject.name)

    def total_completed(self):
        completed = 0
        for subject in self.subjects:
            completed += subject.completed_number()

        return completed

    def overall_total(self):
        total = 0
        for subject in self.subjects:
            total += subject.total()

        return total

    def overall_progress(self):
        if self.overall_total() == 0:
            return 0
        return round(self.total_completed() / self.overall_total(), 1) * 100

    def add_sessions(self,session):
        self.sessions.append(session)

    def total_study_time(self):
        total = 0

        for session in self.sessions:
            total += session.duration

        return total

    def total_study_hrs(self):
        return self.total_study_time() / 60
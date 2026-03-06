from datetime import date, datetime


class Trainee:
    """Structure for the main class for trainee"""

    def __init__(self, name: str, email: str, dob: date):
        self.name = name
        self.email = email
        self.date_of_birth = dob
        self.assessments = []

    def get_age(self) -> int:
        """calculates and returns the age of someone"""
        age = 0
        age = date.today().year - self.date_of_birth.year - ((date.today().month,
                                                              date.today().day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """adds a assessment to the assessment list"""
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Looks to see if an assessment is in a list using its name"""
        for assessments in self.assessments:
            if assessments.name == name:
                return assessments
        return None


class Assessment:
    def __init__(self, name: str, type: str, score: int):
        self.name = name
        self.type = type
        self.score = score
        self.valid_types = ['multiple-choice', 'technical', 'presentation']
        if self.type.lower() not in self.valid_types:
            raise ValueError("That type is not a assessment type")
        if self.score < 0 or self.score > 100:
            raise ValueError("That percentage is not possible")


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))

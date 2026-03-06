from datetime import date


class Trainee:
    """Structure for the main class for trainee"""

    def __init__(self, name: str, email: str, dob: date):
        """initialise all the values"""
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
        if isinstance(assessment, Assessment) == False:
            raise TypeError("That is not an Assessment")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Looks to see if an assessment is in a list using its name"""
        for assessments in self.assessments:
            if assessments.name == name:
                return assessments
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """collects all the assessments that are present in the list"""
        list_of_a_type = []
        for assessment in self.assessments:
            if assessment.type == type:
                list_of_a_type.append(assessment)
        return list_of_a_type


class Assessment:
    """Created the structure for all assessments"""

    def __init__(self, name: str, type: str, score: int):
        """initialise all the values"""
        self.name = name
        self.type = type
        self.score = score
        self.valid_types = ['multiple-choice', 'technical', 'presentation']
        if self.type.lower() not in self.valid_types:
            raise ValueError("That type is not a assessment type")
        if self.score < 0 or self.score > 100:
            raise ValueError("That percentage is not possible")


class MultipleChoiceAssessment(Assessment):
    """Creates Variant for only Multi choice"""

    def __init__(self, name, score):
        """initialise all the values"""
        self.name = name
        self.score = score
        self.type = 'multiple-choice'

    def calculate_score(self) -> float:
        """calculates the specific Bias score"""
        return (self.score * 0.7)


class TechnicalAssessment(Assessment):
    """Creates Variant for only Technical"""

    def __init__(self, name, score):
        """initialise all the values"""
        self.name = name
        self.score = score
        self.type = 'technical'

    def calculate_score(self) -> float:
        """calculates the specific Bias score"""
        return self.score


class PresentationAssessment(Assessment):
    """Creates Variant for only presentation"""

    def __init__(self, name, score):
        """initialise all the values"""
        self.name = name
        self.score = score
        self.type = 'presentation'

    def calculate_score(self) -> float:
        """calculates the specific Bias score"""
        return (self.score * 0.6)


class Question:
    """Creates each question and hold the correct answer and the answer the user inputed"""

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        """initialise all the values"""
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """Compiles all the questions into one list, and give the quiz a name and type"""

    def __init__(self, questions: list, name: str, type: str):
        """initialise all the values"""
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    """Marks the quizzes and returns a percentage score"""

    def __init__(self, quiz: Quiz) -> None:
        """initialise all the values"""
        self._quiz = quiz

    def mark(self) -> int:
        """returns the calculated score for each assessment as a whole number"""
        if len(self._quiz.questions) < 1:
            return 0
        number_of_questions = 0
        questions_got_correct = 0

        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                questions_got_correct += 1
            number_of_questions += 1

        return round((questions_got_correct/number_of_questions)*100)

    def generate_assessment(self) -> Assessment:
        """creates an assessment instance of appropriate type, based on the type in quiz"""
        if self._quiz.type == 'multiple-choice':
            assessment = MultipleChoiceAssessment(self._quiz.name, self.mark())
        elif self._quiz.type == 'technical':
            assessment = TechnicalAssessment(self._quiz.name, self.mark())
        elif self._quiz.type == 'presentation':
            assessment = PresentationAssessment(self._quiz.name, self.mark())
        else:
            raise TypeError("Invalid type of test")

        return assessment


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code

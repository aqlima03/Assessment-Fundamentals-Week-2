"""Marking the assessments"""
from datetime import date


class Assessment:
    """An assessment taken by a trainee"""
    valid_types = {"multiple-choice", "technical", "presentation"}

    def __init__(self, name: str, type: str, score: float):
        """Creates an assessment with a name, type, and score"""
        if type not in self.valid_types:
            raise ValueError("Invalid assessment type")

        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")

        self.name = name
        self.type = type
        self.score = score

    def calculate_score(self):
        """Return the assessment score"""
        return float(self.score)


class MultipleChoiceAssessment(Assessment):
    """Multiple-choice assessment weighed at 70%"""

    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self) -> float:
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """Technical Assessment weighed at 100%"""

    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self) -> float:
        return float(self.score)


class PresentationAssessment(Assessment):
    """Presentation assessment weighed at 60%"""

    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self):
        return self.score * 0.6


class Trainee:
    """A trainee and their completed assessments"""

    valid_types = {"multiple-choice", "technical", "presentation"}

    def __init__(self, name: str, email: str, dob: date,
                 assessments: list[Assessment] | None = None,):
        """A trainee with personal details and assessments"""
        self.name = name
        self.email = email
        self.date_of_birth = dob
        self.assessments = []

        if assessments is not None:
            for assessment in assessments:
                self.add_assessment(assessment)

    def get_age(self) -> float:
        """Calculate and return the trainee's age in years"""
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return float(age)

    def add_assessment(self, assessment: Assessment) -> None:
        """Add the assessment to the the trainee's assessment list"""
        if not isinstance(assessment, Assessment):
            raise TypeError("assessment must be an Assessment object")

        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """The first assessment matching a given name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment

        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """Return all the assessments of a type"""

        if type not in self.valid_types:
            raise ValueError("Invalid assessment type")
        return [assessment
                for assessment in self.assessments
                if assessment.type == type]


class Question:
    """A quiz question and its answers"""

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """A quiz containing questions"""

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self) -> int:
        """Percentage of correctly answered questions"""
        questions = self._quiz.questions

        if not questions:
            return 0

        correct_answers = 0

        for question in questions:
            if question.chosen_answer == question.correct_answer:
                correct_answers += 1

        return round((correct_answers / len(questions)) * 100)

    def generate_assessment(self) -> Assessment:
        """An assessment matching the quiz type"""

        score = self.mark()
        quiz_name = self._quiz.name
        quiz_type = self._quiz.type

        assessment_classes = {"multiple-choice": MultipleChoiceAssessment,
                              "technical": TechnicalAssessment,
                              "presentation": PresentationAssessment}

        assessment_class = assessment_classes.get(quiz_type)

        if assessment_class is None:
            raise ValueError("Invalid assessment type")

        return assessment_class(quiz_name, score)


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

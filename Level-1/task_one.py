"""An assessment platform for trainees"""
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


class Trainee:
    """A trainee and their completed assessments"""

    def __init__(self, name: str, email: str, dob: date,
                 assessments: list[Assessment] | None = None,):
        """A trainee with personal details and assessments"""
        self.name = name
        self.email = email
        self.date_of_birth = dob
        self.assessments = assessments if assessments is not None else []

    def get_age(self) -> float:
        """Calculate and return the trainee's age in years"""
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return float(age)

    def add_assessment(self, assessment: Assessment) -> None:
        """Add the assessment to the the trainee's assessment list"""
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Find an assessment name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment

        return None


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

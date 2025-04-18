import unittest
from creational_patterns.simple_factory import AssessmentFactory, QuizAssessment, WrittenAssessment

class TestSimpleFactory(unittest.TestCase):
    def test_quiz_assessment_creation(self):
        factory = AssessmentFactory()
        assessment = factory.create_assessment("quiz")
        self.assertIsInstance(assessment, QuizAssessment)
        self.assertEqual(assessment.display(), "Quiz Assessment")

    def test_written_assessment_creation(self):
        factory = AssessmentFactory()
        assessment = factory.create_assessment("written")
        self.assertIsInstance(assessment, WrittenAssessment)
        self.assertEqual(assessment.display(), "Written Assessment")

    def test_invalid_assessment_creation(self):
        factory = AssessmentFactory()
        with self.assertRaises(ValueError):
            factory.create_assessment("invalid")

    

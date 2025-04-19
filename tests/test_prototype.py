import unittest
from creational_patterns.prototype import AssessmentTemplate

class TestPrototype(unittest.TestCase):
    def test_assessment_template_clone(self):
        template = AssessmentTemplate("Math Quiz", "Solve all questions")
        clone = template.clone()
        self.assertIsNot(template, clone)
        self.assertEqual(template.title, clone.title)
        self.assertEqual(template.instructions, clone.instructions)

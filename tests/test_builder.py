import unittest
from creational_patterns.builder import ReportBuilder

class TestBuilder(unittest.TestCase):
    def test_report_builder(self):
        builder = ReportBuilder()
        report = builder.add_top_performers().add_average_scores().build()
        self.assertEqual(report.show(), ["Top Performers", "Average Scores"])

    def test_empty_report(self):
        builder = ReportBuilder()
        report = builder.build()
        self.assertEqual(report.show(), [])


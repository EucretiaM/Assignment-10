class Report:
    def __init__(self):
        self.sections = []

    def show(self):
        return self.sections

class ReportBuilder:
    def __init__(self):
        self.report = Report()

    def add_top_performers(self):
        self.report.sections.append("Top Performers")
        return self

    def add_average_scores(self):
        self.report.sections.append("Average Scores")
        return self

    def build(self):
        return self.report

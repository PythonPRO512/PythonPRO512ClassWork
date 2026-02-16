"""
Задание 2. Создание абстрактного класса для генерации отчётов

Ситуация: мы находимся в отделе разработки консалтинговой фирмы.
Нам необходимо создать интерфейс для генерации и сохранения отчётов.

Задача — написать программу, которая реализует абстрактный класс ReportGenerator,
определяющий интерфейс для генерации и сохранения отчётов.
Подклассы должны реализовать методы для создания отчётов в различных форматах
(PDF, Excel, HTML) и их сохранения.
"""
from abc import ABC, abstractmethod


class ReportGenerator(ABC):

    @abstractmethod
    def generate_report(self, data):
        pass


class PDFReportGenerator(ReportGenerator):

    def __init__(self):
        self.data = None

    def generate_report(self, data):
        self.data = data
        return f'PDF Report Content: {data}'

    def save_report(self, filename):
        print(f'Saving PDF {self.data} report to {filename}.pdf')


class ExcelReportGenerator(ReportGenerator):

    def __init__(self):
        self.data = None

    def generate_report(self, data):
        self.data = data
        return f'Excel Report Content: {data}'

    def save_report(self, filename):
        print(f'Saving Excel {self.data} report to {filename}.xlsx')


class HTMLReportGenerator(ReportGenerator):

    def __init__(self):
        self.data = None

    def generate_report(self, data):
        self.data = f'<html><body>{data}</body></html>'
        return f'<html><body>{data}</body></html>'

    def save_report(self, filename):
        print(f'Saving HTML {self.data} report to {filename}.html')
        with open('data.html', 'w', encoding='utf-8') as file:
            file.write(self.data)


if __name__ == '__main__':
    pdf_gen = PDFReportGenerator()
    pdf_content = pdf_gen.generate_report("Sales Data")
    pdf_gen.save_report("sales_report")

    excel_gen = ExcelReportGenerator()
    excel_content = excel_gen.generate_report("Inventory List")
    excel_gen.save_report("inventory_report")

    html_gen = HTMLReportGenerator()
    html_content = html_gen.generate_report("User Statistics")
    html_gen.save_report("user_stats")

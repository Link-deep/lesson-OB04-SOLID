# принцип открытости/закрытости (Open closed Principle);

# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f" Сформирован отчет {self.title} с содержанием {self.content}")

# Создаем абстрактный класс для возможности расширения функционала к примеру добавить
# варианты вывода в определенный формат данных

from abc import ABC, abstractmethod
# модуль для работы с абстрактными классами


class Formatted(ABC):
    @abstractmethod  # ДЕКОРАТОР
    def format(self, report):
        pass


class TextFormatted(Formatted):
    def format(self, report):
       print(report.title)
       print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")


class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)


# report = Report('Заголок', 'Контент данных данного отчета', TextFormatted())
report = Report('Заголок', 'Контент данных данного отчета', HtmlFormatted())

report.docPrinter()




















# Принцип инверсии зависимости (DIP, Dependency Inversion Principle)

# Создадим пример, в котором не используется данный принцип

class Book():
    def read(self):
        print("Чтение интрересной истории")

class StoryReader():
    def __init__(self):
        self.book = Book()

    def tell_story(self):
        self.book.read()

# Пример с использование DIP

from abc import ABC, abstractmethod
class StrySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class BookStrySource(StrySource):
    def get_story(self):
        print("Чтение интрересной истории")

class AudioStrySource(StrySource):
    def get_story(self):
        print("Прослушивание интрересной истории")

class StoryReader():
    def __init__(self, story_source: StrySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

book = BookStrySource()
audiobook = AudioStrySource()

readerBook = StoryReader(book)
readerAudioBook = StoryReader(audiobook)


readerBook.tell_story()
readerAudioBook.tell_story()



















































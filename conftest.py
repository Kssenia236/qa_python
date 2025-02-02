import pytest

from main import BooksCollector

@pytest.fixture
def two_books():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
    collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
    return collector


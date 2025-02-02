from conftest import two_books
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_add_genre_to_book(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre_add_two_books(self, two_books):

        collector = two_books

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби']
        assert collector.get_books_with_specific_genre('Ужасы') == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children_add_two_books_only_one_for_children(self, two_books):

        collector = two_books

        assert len(collector.get_books_genre()) == 2
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_add_two_books_only_one_for_favorites(self, two_books):

        collector = two_books

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 2
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_add_two_books(self, two_books):

        collector = two_books

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_add_two_books_delete_one(self, two_books):

        collector = two_books

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_add_one_book_to_favorite_try_delete_not_favorite(self, two_books):

        collector = two_books

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_add_one_book_to_favorite_try_delete_from_favorite_not_existing_book(self, two_books):

        collector = two_books

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить!')

        assert len(collector.get_books_genre()) == 2
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_add_new_book_add_book_without_name(self):

        collector = BooksCollector()

        collector.add_new_book('')

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_book_with_name_42_len(self):

        collector = BooksCollector()

        collector.add_new_book('abcdendkjfdifjefsdijfiejfuijndiurfnnvjndfi')

        assert len(collector.get_books_genre()) == 0

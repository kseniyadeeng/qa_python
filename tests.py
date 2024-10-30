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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #add_new_book
    def test_length_name_book_from_1_to_40_not_empty_result(self, name_book):
        collector = BooksCollector()
        assert collector.add_new_book(name_book) != ""

    def test_add_new_book_without_name_null_result(self, collector):
        collector.add_new_book("")

        assert len(collector.get_books_genre()) == 0


    # set_book_genre()
    def test_add_book_set_genre_in_list_genre_add(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Ужасы")

        assert list(collector.get_books_genre().values())[0] == "Ужасы"

    def test_add_book_set_genre_not_in_list_genre_not_add(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Ужасы1")

        assert list(collector.get_books_genre().values())[0] == ""


    # get_book_genre()
    def test_get_book_genre_from_exist_book_genre_add(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Ужасы")

        assert collector.get_book_genre("Гарри Поттер") == "Ужасы"

    # get_books_with_specific_genre()
    def test_get_books_with_spec_genre_exist_book_exist_genre__genre_add(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Ужасы")

        assert collector.get_books_with_specific_genre("Ужасы") == ["Гарри Поттер"]

    # get_books_genre()
    def test_get_books_genre_from_nonexist_books_null_result(self, collector):
        assert collector.get_books_genre() == {}

    # get_books_for_children()
    def test_get_books_for_children_exist_(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Гарри Поттер", "Ужасы")
        collector.set_book_genre("Война и мир", "Мультфильмы")

        assert collector.get_books_for_children() == ["Война и мир"]


    # add_book_in_favorites()
    def test_add_book_in_favorites_exist_book_add_to_list(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")

        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]


    # delete_book_from_favorites()
    def test_delete_book_from_favorites_exist_book_null_list(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")

        assert len(collector.get_list_of_favorites_books()) == 0

    # get_list_of_favorites_books()
    def test_get_list_of_favorites_books_exist_books(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_book_in_favorites("Война и мир")

        assert collector.get_list_of_favorites_books() == ["Гарри Поттер", "Война и мир"]
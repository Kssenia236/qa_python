# qa_python

1.test_add_new_book_add_two_books - проверяет добавление двух книг

2.test_set_book_genre_add_genre_to_book - проверяет добавление жанра книге

3.test_get_books_with_specific_genre_add_two_book - проверяет получение списка из двух книг с определенным жанром

4.test_get_books_for_children_add_two_books_only_one_for_children - проверяет, что из двух добавленных книг,в список для детей добавится только одна с подходящим жанром

5.test_add_book_in_favorites_add_two_books_only_one_for_favorites - проверяет добавление двух книг и только одна в список избранного

6.test_add_book_in_favorites_add_two_books - проверяет добавление двух книг в список избранного

7.test_delete_book_from_favorites_add_two_books_delete_one -проверяет добавление двух книг в избранное и удаление одной из них из списка избранного

8.test_delete_book_from_favorites_add_one_book_to_favorite_try_delete_not_favorite Этот тест проверяет логику работы функции удаления книги из избранного списка. Он подтверждает, что функция корректно обрабатывает ситуацию, когда пытаются удалить книгу, которая не находится в списке избранного, и не вызывает ошибок или сбоев в работе системы.

9.test_delete_book_from_favorites_add_one_book_to_favorite_try_delete_from_favorite_not_existing_book - Этот тест проверяет, что система корректно обрабатывает ситуацию, когда пытаются удалить книгу из избранного, но данная книга не существует в списке избранного.

10.test_add_new_book_add_book_without_name - Этот тест проверяет корректность обработки ситуации, когда пытаются добавить книгу в список без указания её названия. Он гарантирует, что система не позволяет добавлять книги без обязательных данных (в данном случае — без названия) и предотвращает ошибки или сбои в работе программы.

11.test_add_new_book_add_book_with_name_42_len - Тест подтверждает, что книга не добавляется в список, если название превышает допустимую длину.
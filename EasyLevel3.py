# Задание 3. Метод is_thick()
# Добавьте в класс Book метод is_thick(), который возвращает True, если количество страниц больше 300, иначе False. Проверьте его работу для book1 и book2.
# 📝 Пример вывода:
# Книга '1984' толстая? True
# Книга 'Неизвестно' толстая? False
class Book:
    book_count = 0
    library_name = "Главная библиотека"

    def __init__(self, title="Неизвестно", author="Неизвестно", pages=0 ):
            self.title = title
            self.author = author
            self.pages = pages
            # Увеличение счётчика книг при каждом создании экземпляра
            Book.book_count += 1

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}")

    @classmethod
    def change_library(cls, new_name):
        cls.library_name = new_name

    def is_thick(self):
        return self.pages > 300

book1 = Book(title="1984", author="Джордж Оруэлл", pages=328)
book2 = Book()

print(f"Книга'{book1.title}' толстая? {book1.is_thick()}")
print(f"Книга'{book2.title}' толстая? {book2.is_thick()}")
# Вывод:
# Книга'1984' толстая? True
# Книга'Неизвестно' толстая? False



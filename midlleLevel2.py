# # Задание 2. Инкапсуляция: методы get_max_speed и set_max_speed
# # Добавьте в класс Vehicle:
# # Метод get_max_speed(), возвращающий __max_speed.
# # Метод set_max_speed(new_speed), который изменяет __max_speed, если new_speed > 0.
# # Проверка:
# # Измените __max_speed на 200 через set_max_speed().
# # Выведите новое значение через get_max_speed().
# # 📝 Пример вывода:
# # Максимальная скорость: 200
# class Vehicle:
#     def __init__(self):
#         self._speed = 0 # защищенный атрибут
#         self.__max_speed = 120 # приватный
#
#     def drive(self):
#         print(f"Текущая скорость: {self._speed} км/ч")
#
#     def get_max_speed(self):
#         return self.__max_speed
#
#     def set_max_speed(self, new_speed):
#         if new_speed > 0:
#             self.__max_speed = new_speed
#
# class Car(Vehicle): # наследует все свойства и методы родительского класса
#     def __init__(self, brand="Неизвестно"):
#         super().__init__()
#         self.brand = brand
#
#     def drive(self):
#         print(f"Машина {self.brand} движется со скоростью {self._speed} км/ч")
#
# car = Car(brand="Toyota")
# car.set_max_speed(200)
# print(f"Максимальная скорость: {car.get_max_speed()}")
# # Вывод:
# # Максимальная скорость: 200



# class UserManager():
#     def __init__(self, user):
#         self.user - user
#
#     def change_user_name(self, user_name):
#         self.user = user_name
#
#     def save_user(self):
#         file = open("users.txt", "a")
#         file.write(self.user)
#         file.close()
#
#
# Принципы SOLID:
#
# принцип единственной ответственности (Single Responsibility Principle);
# принцип открытости/закрытости (Open closed Principle);
# принцип подстановки Барбары Лисков (Liskov substitution Principle);
# принцип разделения интерфейсов (Interface Segregation Principle);
# принцип инверсии зависимости (Dependency Inversion Principle)


class User():
    def __init__(self, name):
        self.name = name

class ChangeNameUser():
    def __init__(self, user):
        self.user = user

    def change_name(self, new_name):
        self.user.name = new_name

class SaveUser():
    def __init__(self, user):
        self.user = user

    def save_user(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()

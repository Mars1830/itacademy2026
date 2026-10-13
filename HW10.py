class Product:
    def __init__(self, price = 0):
        self.price = price


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height


class TestStats:
    def __init__(self, passed, total):
        self.passed = passed
        self.total = total
        self.success_rate = self.passed / self.total * 100


class PermissionMixin:
    @staticmethod
    def has_permission(user_role):
        return True if user_role == "admin" else False


class SecureAction(PermissionMixin):
    def execute(self, role):
        pass


class Logger:
    def log(self, message):
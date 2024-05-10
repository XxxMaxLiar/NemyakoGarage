import re

def is_valid_password(password: str) -> bool:
    """Проверяем, что пароль содержит буквы, цифры и спецсимволы"""
    if not any(re.match(f'^{symbol}', password) for symbol in '0OIll1lIi@#$%^&*()_+-=[]{};:"/,?'):
        return False

    """Проверяем, что пароль содержит буквы верхнего и нижнего регистра"""
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return False

    """Проверяем, что длина пароля больше минимальной (8 символов)"""
    min_len_password = 8
    if len(password) < min_len_password:
        return False

    return True

class Auth:
    @staticmethod
    def check_correct_password(password: str) -> bool:
        return is_valid_password(password)
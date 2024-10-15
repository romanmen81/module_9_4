first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

#----------------------------

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for idx, item in enumerate(data_set, start=1):
                file.write(f"{idx}. {item}\n")
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#----------------------------

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Вернет случайно одно из слов
print(first_ball())  # Вернет снова случайно
print(first_ball())  # Вернет снова случайно

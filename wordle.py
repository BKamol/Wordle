import random


class Wordle:
    #таблица рекордов
    records = {1: 0, 2: 0, 3: 0}

    def __init__(self):
        self.secret_word = None
        self._visible_word = ['_' for _ in range(4)]
        self.attempts = []
        self.found_letters = []       #отгаданные буквы
        self.log = []
        self.score = 0
        self.won = False
        self.init_secret_word()

    def init_secret_word(self):
        """Случайным образом инициализирует атрибут secret_word словом из файла words"""
        with open('words.txt', 'r') as f:
            words = [word.strip() for word in f.readlines()]
        index = random.randint(0, len(words)-1)
        self.secret_word = words[index]
        
    def new_game(self, score=0):
        """Перезапускает игру после победы и нажатия на y, возвращает строку с секретным словом"""
        self.__init__()
        self.score = score
        self.log.append(f"Игра: секретное слово - {''.join(self._visible_word)}")
        return '\n'.join(self.log)
    
    def make_attempt(self, word):
        """
        Вызвается после ввода слова в поле и нажатия кнопки отправить
        word: str - строка, полученная из lineEdit
        Проверяет игру на окончание, если игра окончена, вызывает нужную функцию, иначе обновляет логи
        Возвращает логи в виде строки
        """
        self.attempts.append(word)
        if word == self.secret_word:
            self.victory()
        elif len(self.attempts) >= 5 or self.won and word == 'n':
            self.game_over()
        elif self.won and word == 'y':
            self.new_game(self.score)
        else:
            self.log.append(f"Игрок: {word}")
            self._update_letters(word)
            self.log.append(f"Игра: слово - {''.join(self._visible_word)}   |   Отгаданные буквы - {' '.join(self.found_letters)}")
        return '\n'.join(self.log[-8:])

    def _update_letters(self, word):
        """Проверяет, нашел ли игрок буквы и добавляет их в атрибут found_letters"""
        for i, letter in enumerate(word):
            if letter in self.secret_word and letter not in self.found_letters:
                self.found_letters.append(letter)
                self._update_visible_word(letter, i)

    def _update_visible_word(self, letter, index):
        """Проверяет находится ли найденная буква на своем месте, если да, обновляет атрибут _visible_word"""
        if self.secret_word[index] == letter:
            self._visible_word[index] = letter

    def victory(self):
        """Вызывается в случае победы"""
        self.score += 6 - len(self.attempts)
        self.won = True
        self.log.append(f"Игра: Вы отгадали слово! Всего баллов в этом раунде: {6 - len(self.attempts)}. Желаете продолжить? (y-да, n-нет)")

    def game_over(self):
        """Вызывается при окончании игры. В случае поражения или победы и нажатия n"""
        self.update_records()
        if not self.won:
            self.log.append(f"Игра: К сожалению, вы проиграли, слово было: {self.secret_word}")
        self.log.append(f"Игра: Всего баллов заработано: {self.score}.")

    def update_records(self):
        """Обновляет таблицу рекодров"""
        if self.score > self.records[1]:
            self.records[1] = self.score
        elif self.score > self.records[2]:
            self.records[2] = self.score
        elif self.score > self.records[3]:
            self.records[3] = self.score

    def get_records(self):
        result = ''
        for key, item in self.records.items():
            result += f"{key} место: {item} баллов\n"
        return result
    
    def get_log(self):
        return '\n'.join(self.log)
        


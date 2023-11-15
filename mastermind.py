# import random
import copy
class Process:
    def __init__(self, pos=4, color=6) -> None:
        if 1 > pos > 10:
            raise ValueError('baka')
        self.__pos = pos
        self.__color = color
        self.__answer = ['2', '1', '1', '3', '2']
        # for i in range(pos):
        #     self.__answer.append(random.randint(1, color))

    @property
    def position(self):
        return self.__pos
    
    @position.setter
    def position(self, pos):
        self.__pos = pos
        
    @property
    def guess(self):
        return ''.join(self.__guess)
    
    @guess.setter
    def guess(self, value):
        self.__guess = list(value)

    @property
    def give_hint(self):
        hint = []
        pop_list = []
        if len(self.__guess) != len(self.__answer):
            raise AssertionError('Are you an idiot?')
        guess_temp = copy.deepcopy(self.__guess)
        answer_temp = copy.deepcopy(self.__answer)
        for i in range(len(self.__guess)):
            if guess_temp[i] == answer_temp[i]:
                hint.append('*')
                pop_list.append(i)
        pop_list.sort()
        pop_list.reverse()

        for i in pop_list:
            guess_temp.pop(i)
            answer_temp.pop(i)

        for i in range(len(guess_temp)):
            if guess_temp[i] in answer_temp:
                hint.append('o')
                answer_temp.remove(guess_temp[i])
        
        return ''.join(hint)
        
    def __str__(self) -> str:
        return str(self.give_hint)


game = Process()
game.guess = '21132'
print(game.guess)
print(game)

# import random
import copy
class Game:
    def __init__(self, pos, color) -> None:
        self.__pos = pos
        self.__color = color
        self.__answer = ['3', '3', '3', '6']
        # for i in range(pos):
        #     self.__answer.append(random.randint(1, color))


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
        return f'Playing Mastermind with {self.__color} colors and {self.__pos} positions'


class Main:
    def __init__(self) -> None:
        self.__pos = 4
        self.__color = 6
        self.__game = Game(self.__pos, self.__color)

    @property
    def position(self):
        return self.__pos

    @position.setter
    def position(self, pos):
        self.__pos = pos
        if 1 < self.__pos < 10:
            raise ValueError('the puzzle length must be from 1 - 10')
        self.__reset()

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
        if 1 < self.__color < 8:
            raise ValueError('You can only have 8 colors')
        self.__reset()


    def __reset(self):
        self.__game = Game(self.__pos, self.__color)
        print(self.__game)

    def play(self):
        print(self.__game)
        turn_count = 0
        while True:
            turn_count += 1
            self.__game.guess = input('Enter your guess: ')
            print(self.__game.give_hint)
            if self.__game.give_hint == ('*' * self.__pos):
                print(f"You successfully solved the puzzle in {turn_count} turns")
                break
            if self.__game.guess == 'giveup':
                print('You gave up')
                break


if __name__ == '__main__':
    game = Main()
    game.play()

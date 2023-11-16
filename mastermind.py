import random
import copy
class Game:
    def __init__(self, pos, color) -> None:
        self.__pos = pos
        self.__color = color
        self.__answer = []
        for _ in range(pos):
            self.__answer.append(str(random.randint(1, color)))

    @property
    def guess(self):
        return ''.join(self.__guess)

    @guess.setter
    def guess(self, value):
        self.__guess = list(value)

    @property
    def answer(self):
        return ''.join(self.__answer)
    
    @property
    def give_hint(self):
        hint = []
        pop_list = []
        if len(self.__guess) != len(self.__answer):
            raise AssertionError\
                ('Your guess must be the same length as your puzzle length, baka.')
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
        if 1 > self.__pos > 10:
            raise ValueError('the puzzle length must be from 1 - 10')
        self.__reset()

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
        if 1 > self.__color > 8:
            raise ValueError('You can only have 1-8')
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
            if self.__game.guess == 'giveup':
                print('You gave up')
                print(f"The answer is {self.__game.answer}")
                print(f"You've played for {turn_count} turn")
                break
            print(self.__game.give_hint)
            if self.__game.give_hint == ('*' * self.__pos):
                print(f"You successfully solved the puzzle in {turn_count} turns")
                break


if __name__ == '__main__':
    print("Mastermind, a game to kill your time\n\
Copyright (C) <2023>  <Jangsoodlor>\n\
\n\
This program is free software: you can redistribute it and/or modify\n\
it under the terms of the GNU General Public License as published by\n\
the Free Software Foundation, either version 3 of the License, or\n\
(at your option) any later version.\n\
\n\
This program is distributed in the hope that it will be useful,\n\
but WITHOUT ANY WARRANTY; without even the implied warranty of\n\
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n\
GNU General Public License for more details.\n\
\n\
You should have received a copy of the GNU General Public License\n\
along with this program.  If not, see <https://www.gnu.org/licenses/>.\n")
    end_game = False
    game = Main()
    while end_game == False:
        print('Game Options')
        print('1. Start the game')
        print('2. Set puzzle length')
        print('3. Set the amount of colors')
        print('4. How to Play?')
        print('5. Quit')
        option = int(input('enter your option: '))
        if option == 1:
            game.play()
            play_again = input('Play Again? (Y/N): ')
            if play_again.upper() == 'N':
                end_game = True
        elif option == 2:
            game.position = int(input('Set the puzzle length form 1 to 10: '))
        elif option == 3:
            game.color = int(input('Set the amount of colors from 1 to 8: '))
        elif option == 4:
            print('Ask ChatGPT')
        elif option == 5:
            end_game = True
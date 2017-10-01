import re

from dice import Dice, BufferedDice

dice_pattern = re.compile('\d+(d|D)\d+')


def extract_dice_from_string(s):
    s = str.lower(s)
    arr = s.split('d')
    dices = arr[0]
    sides = arr[1]
    return dices, sides


def throw_the_dice(command):
    dices, sides = extract_dice_from_string(command)
    d = Dice(sides=sides, dices=dices)
    print(d.roll)
    return dices, sides


def simple_dice_app():
    command = 'Y'
    last_dices = 0
    last_sides = 0
    prompt = 'roll a dice by entering e.g. 1d6 or enter Q to quit\n'
    while command != 'Q':
        if last_dices != 0:
            prompt = "roll " + str(last_dices) + "d" + str(
                last_sides) + " again by pressing enter, type another dice or Q to Quit\n"
        command = raw_input(prompt)
        if str(command) == '':
            throw_the_dice(str(last_dices) + 'd' + str(last_sides))
        elif dice_pattern.match(command):
            dices, sides = throw_the_dice(command)
            last_dices = dices
            last_sides = sides
        elif str(command) != str('Q'):
            print('invalid input, try "3d6" without "-signs')


def buffered_dice_app():
    command = 'Y'

    dice = None
    while dice is None:
        prompt = 'What kind of dice do you want to throw? input a valid dice (e.g. 1d6) or Q for quit\n'
        kind = raw_input(prompt)
        if dice_pattern.match(kind):
            dices, sides = extract_dice_from_string(kind)
            dice = BufferedDice(dices, sides)
        elif str(kind) == 'Q':
            break
        else:
            print('invalid input type')

    while command != 'Q':
        prompt = 'press enter to roll another ' + str(dice)
        command = raw_input(prompt)
        print(dice.roll)


if __name__ == '__main__':
    buffered_dice_app()
    # simple_dice_app()

class Character:
    def __init__(self, name, power, strong, attack, defense):
        self.name = name
        if power >= 0 and power <= 100:
            self.power = power
        else:
            raise Exception('Invalid number! Choose a number between 0 and 100.')
        if strong >= 0 and strong <= 100:
            self.strong = strong
        if attack >= 0 and attack <= 100:
            self.attack = attack
        if defense >= 0 and defense <= 100:
            self.defense = defense

def fight(character_one, character_one_option, character_two, character_two_option):
        if character_one_option > character_two_option:
            return f"{character_one}: {character_one_option}\n{character_two}: {character_two_option}\n {character_one} wins!"
        elif character_two_option > character_one_option:
            return f"{character_one}: {character_one_option}\n{character_two}: {character_two_option}\n\nResult: {character_two} wins!"


han_solo = Character('Han Solo', 47, 55, 81, 54)
luke_skywalker = Character('Luke Skywalker', 99, 74, 95, 94)


print(fight(han_solo.name, han_solo.attack, luke_skywalker.name, luke_skywalker.attack))


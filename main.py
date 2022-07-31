from mimetypes import init

from random import randint, seed

def roll_dice(n_faces=6):
    return randint(1, n_faces)

class Hero:
    def __init__(self) -> None:
        self.type = hero_types.get(roll_dice())

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.party = self.create_party()

    def create_party(self):
        party = []
        for hero in range(6):
            party.append(roll_dice())
        party.sort()
        return party

    def show_party(self):
        for hero in self.party:
            print(hero_types.get(hero))
        return
        
hero_types = {
    1: 'champion',
    2: 'wizard',
    3: 'warrior',
    4: 'sorcerer',
    5: 'thief',
    6: 'pergamin'
}

def main():
    player = Player('miguel')
    print('Hello %s!' % player.name)
    print('This is your party')
    player.show_party()

if __name__ == '__main__':
    main()
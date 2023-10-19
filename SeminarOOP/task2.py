import random


class Player():
    def __init__(self, team: str, id_obj: int) -> None:
        self._id_obj = id_obj
        self.team = team

class Hero(Player):
    DEFAULT_DAMAGE = 10

    def __init__(self, team: str, id_obj: int) -> None:
        super().__init__(id_obj=id_obj, team=team)
        self.damage = Hero.DEFAULT_DAMAGE

    def level_up(self):
        self.damage += 5
        print(f"Level up for {self._id_obj}. Now he has {self.damage} damage")

class Soldier(Player):
    def __init__(self, team: str, id_obj: int) -> None:
        super().__init__(id_obj=id_obj, team=team)
    
    def follow_hero(self, hero: Hero):
        print(f"Soldier {self._id_obj} following for hero {hero._id_obj}")


def main():
    teams = {"red": [], "blue": []}
    idx = 1
    for key, val in teams.items():
        hero = Hero(team=key, id_obj=idx)
        val.append(hero)
        idx += 1
    
    count_of_soldiers = 10
    for i in range(count_of_soldiers):
        s = Soldier(team=random.choice(list(teams.keys())), id_obj=(i+1))
        teams[s.team].append(s)
    soldiers = 0
    win_team = ""
    for team in teams.keys():
        length = len(teams[team])-1
        print(f"Team {team} has {length}")
        if length > soldiers :
            win_team = team
            soldiers = length
    
    teams[win_team][0].level_up()
    for s in teams[win_team][1:]:
        s.follow_hero(teams[win_team][0])

main()

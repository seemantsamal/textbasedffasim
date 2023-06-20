import random

BOLD = "\033[1m"
RESET = "\033[0m"

class Player:
    def __init__(self,name) -> None:
        self.name=name
        self.health=100
        self.damage=100
        self.damage_done=0
        self.eliminations=0
        self.rank=None

    def attack(self,other_player):
        damage = random.randint(1,self.damage)
        other_player.health -=damage
        self.damage_done +=damage

        if damage==100:
            self.eliminations +=1
            print(f"{BOLD}{self.name} eliminates {other_player.name} with a headshot.{RESET}")
        elif other_player.health>0:            
            print(f"{self.name} attacks {other_player.name} for {damage} damage. {other_player.name} has {BOLD}{other_player.health} HP{RESET} left.")
        else:
            self.eliminations +=1
            print(f"{self.name} attacks {other_player.name} for {damage} damage. {BOLD}{other_player.name} has been eliminated by {self.name}.{RESET}")
    
def initialize_players():
    numOfplayers=int(input("Enter the number of players and enter their names in separate lines:"))
    players = []

    for i in range(numOfplayers):
        name=input()
        players.append(Player(name))

    return players

def simulate_battle(player_list):
    total_players=len(player_list)

    while len(player_list) > 1:
        attacker = random.choice(player_list)
        defenders = [player for player in player_list if player != attacker]
        
        if defenders:
            defender = random.choice(defenders)
            attacker.attack(defender)
        else:
            break
        
        defender.rank=len(player_list)

        player_list = [player for player in player_list if player.health > 0]

    if player_list:
        print(f"\n{BOLD}{player_list[0].name} wins the battle royale!{RESET}")
        player_list[0].rank=1
    else:
        print("No players remaining.")

def display_stats(players_list):
    print(f"\n{BOLD}---Results: Eliminations(DMG)---{RESET}")
    sorted_players_list=sorted(players_list,key=lambda player:player.rank, reverse=False)
    for player in sorted_players_list:
        print(f"{BOLD}{player.rank}-{player.name}:{RESET} {player.eliminations}({player.damage_done})")

def main():
    players=initialize_players()
    print(f"\n{BOLD}---Simulating Battle Royale...---{RESET}")
    simulate_battle(players)
    display_stats(players)

main()
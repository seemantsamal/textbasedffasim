import random

BOLD = "\033[1m"
RESET = "\033[0m"

class Player:
    def __init__(self,name) -> None:
        self.name=name
        self.health=100
        self.damage=100

    def attack(self,other_player):
        damage = random.randint(1,self.damage)
        other_player.health -=damage
        if damage==100:
            print(f"{BOLD}{self.name} eliminates {other_player.name} with a headshot.{RESET}")
        elif other_player.health>0:            
            print(f"{self.name} attacks {other_player.name} for {damage} damage. {other_player.name} has {BOLD}{other_player.health} HP{RESET} left.")
        else:
            print(f"{self.name} attacks {other_player.name} for {damage} damage. {BOLD}{other_player.name} has been eliminated by {self.name}.{RESET}")
    
def initialize_players():
    numOfplayers=int(input("Enter the number of players and enter their names in separate lines:"))
    players = []

    for i in range(numOfplayers):
        name=input()
        players.append(Player(name))

    return players

def simulate_battle(player_list):
    while len(player_list) > 1:
        attacker = player_list[random.randint(0, len(player_list) - 1)]
        defenders = [player for player in player_list if player != attacker]
        
        if not defenders:
            break
        
        defender = defenders[random.randint(0, len(defenders) - 1)]
        attacker.attack(defender)

        player_list = [player for player in player_list if player.health > 0]

    if player_list:
        print(f"\n{BOLD}{player_list[0].name} wins the battle royale!{RESET}")
    else:
        print("No players remaining.")

def main():
    players=initialize_players()
    print(f"\n{BOLD}---Simulating Battle Royale...---{RESET}")
    simulate_battle(players)

main()
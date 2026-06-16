#studying argparse module

import argparse

parser = argparse.ArgumentParser(description="Profile Creator for gaming tournament")

parser.add_argument("player_name", help="Name of the player")
parser.add_argument("level",type = int, help="Level of the player")
parser.add_argument("--gclan", help="Gaming clan of the player")
parser.add_argument("--status", help="Player is pro or not")

args = parser.parse_args()
print("\n=== TOURNAMENT PLAYER REGISTRATION ===")
# print(f"the player name is {args.player_name}, level is {args.current_level}. The gaming clan is {args.gclan} and pro status is {args.pro_status}")
print(f"Gamer Tag: {args.player_name}")
print(f"Starting Level: {args.level}")
print(f"Bonus level Target: {args.level +5} (Level +5 Bonus)")

if args.gclan:
    print(f"Clan: Team {args.gclan}")
else:
    print("Clan: [Solo Player]")

if args.status:
    print(f"Rank Status: {args.status.upper()}")
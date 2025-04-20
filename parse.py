# FOR FUTURE WORK
import csv

def read_players_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        players = list(reader)
        return players

def print_players(players):
    for player in players:
        name = player['Name']
        height = player['Height(in)']
        weight = player['Weight(lbs)']
        speed = player['Speed']
        print(f"{name} - Height: {height} in, Weight: {weight} lbs, Speed: {speed}/10")

# Usage
players = read_players_from_csv('data.csv')
print_players(players)

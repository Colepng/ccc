# 5 stars for each point scored
# -3 starts for each foul
# every player has more points scored then number of fouls
num_players = int(input())
num_gold_players = 0
for i in range(num_players):
    num_points = int(input())
    num_fouls = int(input())
    stars = num_points * 5 + num_fouls * -3
    num_gold_players += 1 if stars > 40 else 0
print(f"{num_gold_players}{'+' if num_gold_players == num_players else ''}")
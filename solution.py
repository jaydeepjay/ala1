print("Sports Registration")

sports = ["Cricket", "Football", "Tennis"]
players = []

name = input("Enter name: ")
sport = input("Enter sport: ")

if sport in sports:
    players.append(name)
else:
    print("Sport not available")

print("Player:", name)
print("Sport:", sport)

for i in range(3):
    print("Registered")

print("End")

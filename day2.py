import re


class Game:
    def __init__(self, id, subsets):
        self.id = id
        self.subsets = subsets

    def __str__(self):
        return f"id: {self.id} rounds: {str(self.subsets)}"

    def __repr__(self):
        return f"id: {self.id} rounds: {str(self.subsets)}"

f = open("files/day2.txt")

conv = [x.strip() for x in f.readlines()]
games = []
for x in conv:
    gameId = int(x.replace(":", "").split(" ")[1])
    subsets = []
    for j in x.split(": ")[1].split("; "):
        combs = j.replace(",", "").split(" ")
        local_sub = {}
        for i in range(0, len(combs),2):
            local_sub[combs[i+1]] = int(combs[i])
        subsets.append(local_sub)
    games.append(Game(gameId, subsets))


maxColor = {
    "red": 12,
    "green": 13,
    "blue": 14
}
total = 0
for g in games:
    reachable = True
    for s in g.subsets:
        for k in s.keys():
            if s[k] > maxColor[k]:
                reachable = False
                break

    if reachable:
        total += g.id

total = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
powers = []
for g in games:
    maxColor = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for s in g.subsets:
        for k in s.keys():
            if s[k] > maxColor[k]:
                maxColor[k] = s[k]
    powers.append(maxColor["red"] * maxColor["blue"] * maxColor["green"])

print(sum(powers))


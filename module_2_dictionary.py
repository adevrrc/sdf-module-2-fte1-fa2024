hockey_teams = {
    "winnipeg": "jets",
    "edmonton": "oilers",
    "calgary": "flames"
}

print(hockey_teams)

print(hockey_teams["calgary"].title())

hockey_teams["calgary"] = "Lames"

print(hockey_teams["calgary"].title())

print(hockey_teams.keys())
print(hockey_teams.values())
print(hockey_teams.items())

hockey_teams.clear()

hockey_teams["vancouver"] = "canucks"

print(hockey_teams)

my_dict = {}

print(my_dict)

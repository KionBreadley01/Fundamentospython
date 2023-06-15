#Diccionarios 
#{"key:" "value","Key":"value"}

team = {
    "name":"City",
    "country":"Englad",
    "champions":1,
    "players":['halland','grealisnsh']

}
print(type(team))
print(team)
print(team["name"])
print(team["players"])
team["players"].append("Kevin")
team["name"] = "Mancheter City"
team["leage"] = "Premier league"
print(team)
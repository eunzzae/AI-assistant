player = {
    'name':"nico",
    'age':12,
    'alive':True,
    'fav_food':["🍟","🌭"]
}
# print(player.get('age'))
# print(player.get('fav_food'))
# print(player['fav_food'])
# print(player)
# player.pop('age')
# print(player)
# player['xp']=1550
# print(player)

player['fav_food'].append("🍬")
print(player.get('fav_food'))
print(player['fav_food'])
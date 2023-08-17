# print("nico".endswith("a"))

# numbers = [5,6,4,2,6,7,True, "True", 120]
# numbers.append(["🍬","🌭"])
# # print(numbers)
# # numbers.clear()
# # print(numbers)
# print(numbers[-1])

player = {
    'name':'nico',
    'age':12,
    'alive':True,
    'fav_food':("🍬","🌭"),
    'friend':{
        'name':'lynn',
        'fav_food':["🌭"]
    }
}
# print(player['fav_food'])
player['fav_food'] = '🍎'
player.pop('alive')
player['friend']['fav_food'].append('🥐')

print(player)
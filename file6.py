def make_bread(powder):
    return f"{powder} + 🧈"

def add_egg(bread):
    return f"{bread} + 🥚"

def add_sugar(bread2):
    return f"{bread2} + 🍬"

bread = make_bread("🥐")
bread2 = add_egg(bread)
perfect_bread = add_sugar(bread2)

print(perfect_bread) 

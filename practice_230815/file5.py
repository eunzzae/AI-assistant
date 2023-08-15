# def pay_calc(each):
#     return 5304 * each

# def pay_price(money):
#     print("thank you for paying", money)

# price = pay_calc(11)

# pay_price(price)

def make_juice(fruit):
    return f"{fruit} + 🍹"

def add_ice(juice):
    return f"{juice} + 🧊"

def add_sugar(iced_juice):
    return f"{iced_juice} + 🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice) 

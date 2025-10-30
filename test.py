# def lang(x):
#     t_count = []
#     s_count = []

#     for e in x:
#         if e == 't' or e == 'T':
#             t_count.append(e)
#         elif e == 's' or e == 'S':
#             s_count.append(e)

#         if len(t_count) > len(s_count):
#             print("English")
#         elif len(s_count) > len(t_count):
#             print("French")
#         elif len(s_count) == len(t_count):
#             print("Probably French")
#         break

# lang("The cat jumped from the trash pile into another trash pile")
# def spaces(n,y,t):
#     occ = 0
#     for i in range(n):
#         if (y[i] == "C" and t[i] == "C"):
#             occ += 1
#     return occ    
# print(spaces(5, "CC..C", ".C.C."))
# panpots = "pot"
# if panpots == "pot":
#     print(index['name']['pot'])

items = [

        {
            "name": "pots",
        "price": 100,
        "department": "pots and pans",
        "description": "yay"
        },
        {
            "name":"pans",
            "price": 150,
            "department": "pots and pans",
            "description":"tans"
        },

        {
            "name": "cans",
        "price": 200,
        "department": "Cans",
        "description": "not pots nor pans"}
]

for index, item in enumerate(items):
        print(index, ":" ,(item)["name"])
        items[1]["name"]
cart = []
cost = 0
choice = int(input("What would you like to buy?"))
cart.append(items[choice])
cost += items[choice]["price"]
print(f"Added {items[choice]['name']} into cart")

while True:
    checkout = (input("Would you like to continue shopping? (Yes/No)"))
    if checkout == "Yes":
        choice = int(input("What else would you like to buy?"))
        cart.append(items[choice])
        cost += items[choice]["price"]
        print(f"Added {items[choice]['name']} into cart")
    if checkout == "No":
         break
    
for item in cart: 
    print(f'{item["name"]} ${int(item["price"])}')
print(f"Total: ${cost}")


# class Calculator():
#     def add(x,y):
#             print(x+y)
#             return x+y
#     def add_many(list):
#           print(sum(list))
#           return sum(list)
# Calculator.add(15,5)      

# class Hero:
#       def _init_(self, name, money, inventory)
#         self,name = name
#         self.money = money
#         self,inventory = inventory
#       def buy(self, item):
#         print(f"{self.name} purhcased {item} and has {self.inventory}")]
#         names = Hero("Names", 0 , ["pencil"])
#         print(names_.dict_)
# names.buy("hi")
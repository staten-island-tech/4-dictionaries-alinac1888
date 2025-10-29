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
        
choice = input("What would you like to buy?")
cart = []
cart.append(choice)
print(f"Added", choice, "into cart")
while cart != "done":
    if choice == "pots":
        print[(item)("price")]
    elif choice == "pans":
        print[(item)("price")]
        cost += (items["pans"]["price"])
    else:
        print(co)
        cost += (items["cans"]["price"])




# e()
# print(items["pot"]["price"])
# print(items["cans"]["price"])

# for index, in enumerate[0][items]:
#         print()
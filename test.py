""" def lang(x):
    t_count = []
    s_count = []

    for e in x:
        if e == 't' or e == 'T':
            t_count.append(e)
        elif e == 's' or e == 'S':
            s_count.append(e)

        if len(t_count) > len(s_count):
            print("English")
        elif len(s_count) > len(t_count):
            print("French")
        elif len(s_count) == len(t_count):
            print("Probably French")
        break

lang("The cat jumped from the trash pile into another trash pile")
def spaces(n,y,t):
    occ = 0
    for i in range(n):
        if (y[i] == "C" and t[i] == "C"):
            occ += 1
    return occ    
print(spaces(5, "CC..C", ".C.C.")) """
""" panpots = "pot"
if panpots == "pot":
    print(index['name']['pot']) """

items = [
    "pot":{
        "price": 100,
        "department": "Pot",
        "description": "yay"
    }
    
    "pans":{
        "price": 20000000,
        "department": "Pot",
        "description": "pots and pans"
    }
]
print(items[0]["price"])

# for index, in enumerate[0][items]:
#         print()
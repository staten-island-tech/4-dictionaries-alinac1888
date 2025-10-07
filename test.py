def lang(x):
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

def spaces(y,t):
    y = ["CCC.."]
    t = [".C.C.C"]
    for i in t:
        if "C" == [0,1,2]:
            print("3")
        elif "C" == []:
        
spaces("CCC..",".C.C.C")    

# items = [{"name": "food", "price": 50, "department": "foodfood", "description": "hi"}
#          {"name: "ntofood", }]
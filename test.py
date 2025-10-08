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

lang("The cat jumped from the trash pile into another trash pile") """

def spaces(y,t):
    occ = 0
    for i in len(spaces):
        if y[i] == "C" and t[i] == "C":
            (y,t) = occ + 1
    if y == t:
        return occ
    
spaces("CC..C", ".C.C.")

# item = {

# },
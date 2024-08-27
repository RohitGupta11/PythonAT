def make_pizz(*toppings,base):
    for topin in toppings:
        print(topin,base)

def make_pizz(base,*toppings):
    for topin in toppings:
        print(base,topin)

parmod=make_pizz("tomato","cheese","mushroom",base="thin crust")
shahid=make_pizz(base="plain","tomato","paneer","corn") #not allowed * should be first one


my_shopping_list=["bread","butter","pizza","eggs"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_list):
    more_item=input("eneter the item: ")
    my_list.append(more_item)
    return my_shopping_list

l=bring_more_food(my_shopping_list)
print(l)

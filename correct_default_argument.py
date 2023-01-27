def add_to_list(element, list_B=None):
    if list_B is None:
        list_B = []
    list_B.append(element)
    return list_B

print(add_to_list(10))      #[10]
print(add_to_list(5,[3,4])) #[3, 4, 5]
print(add_to_list(20))      #[20]
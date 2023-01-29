# do not use an empty list (mutable element) as default argument to a function

def add_to_list(element, list_A=[]):    
    list_A.append(element)
    return list_A

print(add_to_list(10))      #[10]
print(add_to_list(5,[3,4])) #[3, 4, 5]
print(add_to_list(20))      #[10, 20]

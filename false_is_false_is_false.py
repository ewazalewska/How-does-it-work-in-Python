# Comparisions - all comparisions operations in Python have the same priority

print(False is False)   #True
print(True is False)    #False
print(False is False is False)      #--> (False is False) and (False is False) --> False and False --> True
print(2 < 18 == 22)                 #--> (2 < 18) and (18 == 22) --> True nad False --> False
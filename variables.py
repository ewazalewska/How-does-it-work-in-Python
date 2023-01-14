var1 = 'python'
var2 = var1 + '!'
var2 = var2[:-1]
print(var1, id(var1))
print(var2, id(var2))
print("Is value the same? ", var1==var2)
print("Are the variables the same? ", var1 is var2)
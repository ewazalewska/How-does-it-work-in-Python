a = b = c = 20
a = 4
print("a", a, id(a))    # zmieni się tylko a, id(a)
print("b", b, id(b))
print("c", c, id(c))

d = e = f = [1, 2, 3]
d.append(4)
print("d", d, id(d))
print("e", e, id(e))
print("f", f, id(f))

# zmieni się również e i f, będą miały takie same id, bo wskazują na komórkę pamięci, 
# w któej jest lista, 
# a dopiero lista jest wskaźnikiem do elementów tej listy

x = 10
y = 10
print("x", x, id(x))
print("y", y, id(y))
y = y + 1 - 1
print("y", y, id(y))
y = y + 1234567890 - 1234567890
print("y", y, id(y))
# niezależne zmienne, ale optymalizator pythona nadał takie samo id




# lambda argument: statement

Numbers = [(3, 'tree'), (1, 'one'), (2, 'two')]

Numbers_sorted = sorted(Numbers, key=lambda x: x[1])        #[(1, 'one'), (3, 'tree'), (2, 'two')]
print(Numbers_sorted)
Numbers_sorted = sorted(Numbers, key=lambda x: x[0])        #[(1, 'one'), (2, 'two'), (3, 'tree')]
print(Numbers_sorted)
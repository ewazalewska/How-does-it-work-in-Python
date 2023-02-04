with open('plik.txt','w') as f:
    for i in range(10):
        f.write(str(i)+"\n")

with open("plik.txt", "r") as f:
    #content = f.read()
    #print(content)
    print(f.read(3))
    print("----")
    print(f.read())

try:
    f = open('plik.txt','a')
    add_content = f.write('10\n')
finally:
    f.close()

with open('plik.txt','a') as f:
    lines = ['11\n','12\n','13\n']
    f.writelines(lines)

with open('plik.txt','r') as f:
    #lines = f.readlines()
    #print(lines)
    print(f.readlines())
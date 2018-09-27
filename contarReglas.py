with open('reglas.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
cumplen = 0
for line in content:
    cuenta = line.count("=t")
    if cuenta > 2:
        print(line)
        cumplen+=1
print("cumplen")
print(cumplen)

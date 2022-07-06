s = input()
abc = list(range(97, 123))

for i in range(len(abc)):
    abc[i] = s.find(chr(abc[i]))

print(*abc)
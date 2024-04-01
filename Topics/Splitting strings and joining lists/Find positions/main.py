sequence = input()
x = input()

test = sequence.split()
i = 0
index = []

if sequence.find(x) == - 1:
    print("not found")

for i in range(len(test)):
    if test[i] == x :
        index.append(str(i))

print(" ".join(index) )


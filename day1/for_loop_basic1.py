
for i in range(0, 150):
    print(i)


for s in range(5, 1000, 5):
    print(s)


for z in range(1, 100):
    print(z)
    if z % 5 == 0:
        print("coding")
    if z % 10 == 0:
        print("coding dojo")

sum = 0

for y in range(0, 500000, 2):
    sum += y
print(sum)


for x in range(2018, 0, -4):
    print(x)


lowNum = 0
highNum = 20
mult = 3
for x in range(lowNum, highNum, mult):
    if x % 3 == 0:
        print(x)

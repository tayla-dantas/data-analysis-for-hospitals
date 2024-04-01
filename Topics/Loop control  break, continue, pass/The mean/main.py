
number = input()
mean = 0
number_quantity = 0

while number != '.':
    mean += float(number)
    number_quantity += 1
    number = input()

result = mean / number_quantity
print(result)
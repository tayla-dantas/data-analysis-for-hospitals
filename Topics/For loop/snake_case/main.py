text = input()
snake_case = ''

for i in text:
    snake_case = i.lower()
    if i.isupper():
        snake_case =  '_' + snake_case
    print(snake_case, end='')

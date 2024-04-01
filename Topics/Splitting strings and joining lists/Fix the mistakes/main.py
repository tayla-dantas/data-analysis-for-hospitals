text = input()
words = text.split()

prefixes = ("www.", "WWW.", "https://", "http://")

for string in words:
    if string.startswith(prefixes):
        print(string)
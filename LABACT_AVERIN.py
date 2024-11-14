words = []
length = []

for user in range(10):
    x = input("Enter a word: ")
    words.append(x)
'''

    if any(char.isdigit() for char in x):
        print("Error! Enter a valid word.")
'''

letters = int(input("Enter the number of letters: "))

for word in words:
    if len(word) >= letters:
        length.append(word)
    else:
        continue
print(f"Here are the following words that have {letters} letters: {length}")
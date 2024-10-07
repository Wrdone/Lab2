N = int(input("Введіть кількість слів: "))
words = []
for i in range(N):
    word = input(f"Введіть слово {i+1}: ")
    words.append(word)

first_letter_count = {}

for word in words:
    first_letter = word[0]  
    if first_letter in first_letter_count:
        first_letter_count[first_letter] += 1
    else:
        first_letter_count[first_letter] = 1

for letter, count in first_letter_count.items():
    if count > 1:
        print(f"Слів, що починаються з '{letter}': {count}")



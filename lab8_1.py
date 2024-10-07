string1 = input("Введіть перший рядок: ")
string2 = input("Введіть другий рядок: ")

common_chars = set(string1) & set(string2)
if common_chars:
    print("Спільні символи: ", ''.join(common_chars))
else:
    print("Спільних символів немає.")

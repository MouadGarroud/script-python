from collections import Counter

input_string = input("Enter a string: ")
char_count = Counter(input_string)
print("Character frequencies:")
total_count = 0
for char, count in char_count.items():
    print(f"'{char}': {count}")
    total_count += count

print(f"Total character count: {total_count}")
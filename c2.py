def count_chars(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():  # Check if the character is a digit
            digit_count += 1
            
    return vowel_count, consonant_count, digit_count
# Example usage:
my_string = "Hello World 123!"
v, c, d = count_chars(my_string)

print(f"Original String: '{my_string}'")
print(f"Number of Vowels: {v}")
print(f"Number of Consonants: {c}")
print(f"Number of Digits: {d}")

my_string_2 = "Python is fun 4 everyone."
v2, c2, d2 = count_chars(my_string_2)
print(f"\nOriginal String: '{my_string_2}'")
print(f"Number of Vowels: {v2}")
print(f"Number of Consonants: {c2}")
print(f"Number of Digits: {d2}")
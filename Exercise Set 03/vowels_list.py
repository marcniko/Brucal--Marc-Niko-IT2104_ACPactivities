def extract_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s if char in vowels]
input_string = input("Enter a string: ")
vowel_list = extract_vowels(input_string)

print(vowel_list)

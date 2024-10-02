def count_vowels_and_consonants(input_value):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    
    vowel_count = 0
    consonant_count = 0
    
    for char in input_value:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count
    
user_input = input("Enter a string: ")
vowels_count, consonants_count = count_vowels_and_consonants(user_input)

print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")

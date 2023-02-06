VOWELS = 'aeiou'

enum_vowels = {}

for i, vowel in enumerate(VOWELS):
    enum_vowels[vowel] = i + 1
    print(i, vowel)


print(enum_vowels)
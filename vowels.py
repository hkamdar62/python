vowels=['a','e','i','o','u']

word=input("Enter a new word:")
word_list=list(word)
vowels_count=0

for letter in word_list:
    if letter in vowels:
        vowels_count+=1

print(vowels_count)
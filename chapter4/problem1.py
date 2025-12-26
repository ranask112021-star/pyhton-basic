#write a program to create a dictionary of Hindi words with values as their ENGLISH transtion . provide user with an option to look it up!.
words = {
    "madad": "help",
    "paani": "water",   
    "dost": "friend",
    "khushi": "happiness",
    "pustak": "book"
}
word = input("Enter a Hindi word to translate: ")
print(words[word])
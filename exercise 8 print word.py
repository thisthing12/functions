# Function to print name a word with the first x letters .upper()


def print_word(word, number):
    word1 = word[0:number]
    word2 = word[number:len(word)]
    print(f"{word1.upper()}{word2}")


# Main routine
word_ = input("Enter word: ")
number_ = int(input("Number of chars to capitalise: "))
print_word(word_, number_)

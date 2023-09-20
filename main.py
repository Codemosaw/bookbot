print("BookBoot V 0.1")
book_dir = "books/frankensein.txt"
with open(book_dir) as f:
    file_contents = f.read()
    words = file_contents.split()
    num_of_words = len(words)

    letters = "qwertyuiopasdfghjklñzxcvbnm"
    letter_inform = {}
    for letter in letters:
        letter_inform[letter] = 0
    
    for letter in file_contents.lower():
        try:
            letter_inform[letter] += 1
        except Exception as e:
            str(e)

    print("---Begin report on " + book_dir + " ---")
    print(str(num_of_words) + " words in the book!")
    for letter in letter_inform:
        print("The '" + letter + "' appeared " + str(letter_inform[letter]) + " times")
    print("--- End Report ---")
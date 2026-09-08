sentence = str(input("Enter a sentence for word count: ")).lower()

if sentence == "":
    print("You did not enter a sentence. Please try again.")
    exit()
elif sentence:
    def word_counter(sentence):
        words = sentence.split()
        word_count = len(words)
        return word_count

    def longest_word(sentence):
        words = sentence.split()
        longest = max(words, key=len)
        return longest

    def word_frequency(sentence):
        words = sentence.split()
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        most_used_word = max(frequency, key=frequency.get)

        return most_used_word, frequency[most_used_word]

    result = print(f"Word count: {word_counter(sentence)}, Longest word: {longest_word(sentence)}, Frequently used word: {word_frequency(sentence)[0]} (used {word_frequency(sentence)[1]} times)")
def count_word_occurrences(text):
    word_counts = {}

    # Split the text into words and count occurrences
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Find the length of the longest word for formatting
    max_word_length = max(len(word) for word in word_counts)

    # Print the word counts sorted alphabetically and aligned
    for word in sorted(word_counts):
        print(f"{word:{max_word_length}} : {word_counts[word]}")


def main():
    text = input("Enter a string: ")
    count_word_occurrences(text)


if __name__ == "__main__":
    main()

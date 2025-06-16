def word_count_tool():
    text = input("Write here: ")

    total_chars = len(text)
    no_space_chars = len(text.replace(" ", ""))
    word_list = text.split()
    word_count = len(word_list)

    print("\n Result: ")
    print(f"Letter count(Including spaces): {total_chars}")
    print(f"Letter count(Excluding spaces): {no_space_chars}")
    print(f"Word count: {word_count}")
    print(f"Word list: {word_list}")

if __name__ == "__main__":
    word_count_tool()

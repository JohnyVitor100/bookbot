import sys
from stats import get_book_text
from stats import count_words
from stats import count_characters
from stats import chars_dict_to_sorted_list

# Check if the program received the correct number of arguments
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Safely assign the argument to 'path'
path = sys.argv[1]

# Proceed with the rest of your code
text = get_book_text(path)
num_words = count_words(text)
char_counts = count_characters(text)
sorted_chars = chars_dict_to_sorted_list(char_counts)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")

# Print each character and its count
for char_dict in sorted_chars:
    for char, count in char_dict.items():
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")

print("============= END ===============")
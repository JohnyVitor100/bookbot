def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(book):
  
 words = book.split()
 num_words = len(words)
 return num_words

def count_characters(book):
  text_lower = book.lower()
  character_counts = {}
  for character in text_lower:
    if character in character_counts:
      character_counts[character] += 1
    else:
      character_counts[character] = 1
  return character_counts

def sort_on(dict_item):
    # Get the first (and only) value from the dictionary
    return list(dict_item.values())[0]

def chars_dict_to_sorted_list(char_dict):
    # Create an empty list to store the single-pair dictionaries
    chars_list = []
    
    # Convert the char_dict to a list of single-pair dictionaries
    for char, count in char_dict.items():
        # Create a dictionary with just this character and count
        char_count_dict = {char: count}
        # Add it to your list
        chars_list.append(char_count_dict)
    
    # Sort the list using your sort_on function
    chars_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return chars_list
 
 
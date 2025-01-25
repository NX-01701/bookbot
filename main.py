def count_words(text):
    """
    Counts the number of words in a given string.
    
    Args:
        text (str): The input text as a string.
    
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def count_character_frequency(text):
    """
    Counts the frequency of alphabetic characters (a-z) in the text.
    
    Args:
        text (str): The input text as a string.
    
    Returns:
        dict: A dictionary with alphabetic characters as keys and their counts as values.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        # Only count alphabetic characters
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def generate_report(word_count, char_frequency):
    """
    Generates a formatted report of the word count and character frequency.
    
    Args:
        word_count (int): The number of words in the text.
        char_frequency (dict): A dictionary of character frequencies.
    
    Returns:
        str: A formatted string containing the report.
    """
    report_lines = []
    report_lines.append("==== Book Report ====\n")
    report_lines.append(f"Total words: {word_count}\n")
    report_lines.append("\nCharacter frequencies:\n")
    
    # Sort characters alphabetically for better readability
    for char, count in sorted(char_frequency.items()):
        char_display = f"'{char}'"  # Represent characters with single quotes
        report_lines.append(f"{char_display}: {count}")
    
    return "\n".join(report_lines)

def main():
    # Path to the file
    path_to_file = "books/frankenstein.txt"
    
    # Open and read the file
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    
    # Get the word count
    word_count = count_words(file_contents)
    
    # Get the character frequency
    char_frequency = count_character_frequency(file_contents)
    
    # Generate the report
    report = generate_report(word_count, char_frequency)
    
    # Print the report to the console
    print(report)

if __name__ == "__main__":
    main()

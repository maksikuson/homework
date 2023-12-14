#Part 1

#Task 1

def palindrome(i):
    i = i.replace(" ", "").lower()
    return i == i[::-1]

line = input("Enter line: ")
if palindrome(line):
    print("It's a palindrome!")
else:
    print("This is not a palindrome(.")


#Task 2

def change_case_reserved_words(text, reserved_words):              #Робив з допомогою ChatGPT
    words = text.split() 
    result_words = []
    for word in words:
        if word.lower() in map(str.lower, reserved_words):
            result_words.append(word.upper())
        else:
            result_words.append(word)
    result_text = ''.join(result_words)
    return result_text
text = input("Enter text: ")
reserved_words_input = input("Enter a list of reserved words separated by commas:")          
reserved_words = [word.strip() for word in reserved_words_input.split(',')]
result_text = change_case_reserved_words(text, reserved_words)
print("Changed text:")
print(result_text)

#Task 3

def count_sentences(text):
    sentence_delimiters = ['.', '!', '?']
    sentence_count = 0
    
    for char in text:
        if char in sentence_delimiters:
            sentence_count += 1
    return sentence_count
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer hendrerit congue mi, porta vehicula nunc luctus nec. Aliquam vestibulum purus risus. Proin ultricies, tellus ac vulputate tempus, diam est iaculis ligula, sit amet efficitur libero felis vel dui. Etiam rhoncus odio non commodo porttitor. Phasellus ac felis sed dui sodales rutrum non mattis leo. Duis at blandit nisi. Mauris eleifend nec eros in vestibulum. Integer erat odio, venenatis in posuere sit amet, rhoncus eget nisi. Nunc vulputate fringilla metus, ut consectetur leo. Donec eu nulla vel neque scelerisque luctus. Nunc tristique, ipsum eget porttitor vehicula, arcu augue mattis nunc, ac porttitor quam augue vel risus."""
sentence_count = count_sentences(text)
print("Number of sentences in the text:", sentence_count)


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


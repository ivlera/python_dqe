str_var = """
homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# 1. Normalizing text from letter case point

# Making all letters lowercased and dividing all text into list of text elements, iterating through each element makes it easier to identify if element goes after tabulation, new line or dot
list_str_var = list(str_var.lower())
# Iterating through list indexes
for i in range(len(list_str_var)):
    # If letter on current iteration goes after new line or tabulation OR if letter goes after dot+whitespace, then the condition will be executed
    # Otherwise, if iterable item is '\n', '\t' or ' ' symbols OR if it is a letter that goes after letter+whitespace OR goes letter after letter - iterable will remain unchanged in 'list_str_var' list
    if (list_str_var[i-1] in ['\n', '\t']) or (list_str_var[i-1] == ' ' and list_str_var[i-2] == '.'):
        # If condition is True, then letter needs to be uppercased. Reassigning lowercased letter uppercased one in 'list_str_var' list
        list_str_var[i] = list_str_var[i].upper()

# New variable containing list joined into string
str_var_joined = ''.join(list_str_var)
# Explicitly making first letter uppercased
first_letter_upper = str_var_joined[0].upper()

# Concatenating first uppercased letter with the rest of the text
normalized_text = first_letter_upper+str_var_joined[1:-1]

# 2. Create one more sentence with last words of each existing sentence

# Again creating a list from string, but is this case dividing it by whitespaces, so each element in list will be word with special symbols ('\n', '\t', '.')
list_normalized_text = normalized_text.split(' ')
# New list where last words will be stored
sentence_last_words_list = []
# Iterating through previously created list of word
for word in list_normalized_text:
    # If word contains '.' symbol, then it is the last word in sentence
    if '.' in word:
        # Creating a variable where index of dot will be stored
        dot_index = word.index('.')
        # Inserting into list not the plain iterable: cutting up word from the very first symbol to '.' symbol. This is required in order to include only word that goes before dot
        sentence_last_words_list.append(word[:dot_index])

# Concatenating list items into string divided by whitespaces
sentence_last_words = ' '.join(sentence_last_words_list)
# Capitalizing first word in sentence
sentence_last_words = sentence_last_words.capitalize()

# 3. Add new sentence to the end of the paragraph

# As long as string are not mutable, it is not possible to insert new sentence into existing string.
# Creating new list where each element will be the sentence
normalized_text_sentences_list = normalized_text.split('.')
# Inserting new sentence after the one that has index=3 and adding whitespace before the inserted sentence
normalized_text_sentences_list.insert(3, ' '+sentence_last_words)
# Concatenating list items into string, using dot to join sentences
normalized_text_with_sentence = '.'.join(normalized_text_sentences_list)

# 4. Fix“iz” with correct “is”

# Creating new list where words are stored
normalized_text_with_sentence_list = normalized_text_with_sentence.split(' ')
# Iterating through list indexes
for i in range(len(normalized_text_with_sentence_list)):
    # If word on current iteration is equal to 'iz' then it should be replace with 'is'
    if normalized_text_with_sentence_list[i] == 'iz':
        # Replacing list item with 'is'
        normalized_text_with_sentence_list[i] = 'is'

# Joining list into one string
normalized_text_with_sentence_fixed = ' '.join(normalized_text_with_sentence_list)
print(normalized_text_with_sentence_fixed)

# 5. Calculate all whitespaces

# Creating a variable that stores the amount of whitespaces in string + the amount of tabs
whitespaces_count = normalized_text_with_sentence_fixed.count(' ')+normalized_text_with_sentence_fixed.count('\t')
print(whitespaces_count)

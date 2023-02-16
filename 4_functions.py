import random
import string


def list_of_random_dicts():
    '''
    :return: List of from 2 to 10 dictionaries where each dictionary consists of from 2 to 10 key-value pairs where key is a random letter and value is a random number from 0 to 100
    '''
    dict_list = []
    for l in range(random.randint(2, 10)):
        dict_list_item = {}
        for i in range(random.randint(2, 10)):
            dict_list_item[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        dict_list.append(dict_list_item)
    return dict_list


def common_dict(dict_list):
    '''
    :param dict_list: List of dictionaries where each dictionary consists of key-value pairs where key is a letter and value is a number
    :return: A dictionary where key is a plain key from input 'dict_list' if it is unique through all list and key+'_n' where n is the number of the dict where key came from and value is the max value for such key through all list
    '''
    dict_common = {}
    dict_list_keys = []
    for i in range(len(dict_list)):
        dict_list_keys.extend(dict_list[i].keys())
    for i in range(len(dict_list)):
        for k, v in dict_list[i].items():
            if dict_list_keys.count(k) == 1:
                dict_common[k] = v
            else:
                dict_common[f'{k}_{i + 1}'] = v
    repeatable_item_max = {}
    for k, v in dict_common.items():
        if len(k) > 1:
            if k[0] in repeatable_item_max.keys():
                if v > repeatable_item_max[k[0]]:
                    repeatable_item_max[k[0]] = v
            else:
                repeatable_item_max[k[0]] = v
    dict_common_final = {}
    for k, v in dict_common.items():
        if len(k) > 1:
            if k[0] in repeatable_item_max.keys():
                if v == repeatable_item_max[k[0]]:
                    dict_common_final[k] = v
        else:
            dict_common_final[k] = v
    return dict_common_final


def text_normalization(str_var):
    '''
    :param str_var: String that contains text without strict normalization, e.g. all letters are in uppercase, lowercase or mixed case
    :return: String that contains normalized text, where each sentence starts with capitalized letter and all other letters in sentence are in lowercase
    '''
    list_str_var = list(str_var.lower())
    for i in range(len(list_str_var)):
        if (list_str_var[i - 1] in ['\n', '\t']) or (list_str_var[i - 1] == ' ' and list_str_var[i - 2] == '.'):
            list_str_var[i] = list_str_var[i].upper()
    str_var_joined = ''.join(list_str_var)
    first_letter_upper = str_var_joined[0].upper()
    return first_letter_upper+str_var_joined[1:-1]


def last_words_sentence(text):
    '''
    :param text: String object containing any amount of sentences
    :return: Sentence that consists of last word of each sentence in input text
    '''
    list_from_text = text.split(' ')
    sentence_last_words_list = []
    for word in list_from_text:
        if '.' in word:
            dot_index = word.index('.')
            sentence_last_words_list.append(word[:dot_index])
    return ' '.join(sentence_last_words_list).capitalize()


def add_sentence_to_text(text, sentence, index=-1):
    '''
    :param text: String object containing text that should be extended with the sentence
    :param sentence: Sentence that should be added to the text
    :param index: Position where sentence should be inserted - index of the sentence after which new sentence goes, -1 by default means that sentence will be inserted to the end if 'index' parameter is not declared
    :return: Text extended with new sentence
    '''
    normalized_text_sentences_list = text.split('.')
    normalized_text_sentences_list.insert(index, ' ' + sentence)
    return '.'.join(normalized_text_sentences_list)


def replace_word_in_text(text, value_to_delete, value_to_insert):
    '''
    :param text: String object containing text where some word should be replaced
    :param value_to_delete: Word in text that should be replaced
    :param value_to_insert: Word that will replace 'value_to_delete' word
    :return: String object containing text with replaced word
    '''
    normalized_text_with_sentence_list = text.split(' ')
    for i in range(len(normalized_text_with_sentence_list)):
        if normalized_text_with_sentence_list[i] == value_to_delete:
            normalized_text_with_sentence_list[i] = value_to_insert
    return ' '.join(normalized_text_with_sentence_list)


def whitespace_calculator(text):
    '''
    :return: Number that shows amount of whitespaces in input text
    '''
    return text.count(' ') + text.count('\t')


# Code to verify task 2 implementation refactored

dict_list = list_of_random_dicts()
common_dict_from_dict_list = common_dict(dict_list)
print(dict_list)
print(common_dict_from_dict_list)

# Code to verify task 3 implementation refactored

normalized_text = text_normalization("""
homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
""")
sentence = last_words_sentence(normalized_text)
text_with_new_sentence = add_sentence_to_text(normalized_text, sentence, 3)
fixed_text = replace_word_in_text(text_with_new_sentence, 'iz', 'is')
print(fixed_text)
print(whitespace_calculator(fixed_text))

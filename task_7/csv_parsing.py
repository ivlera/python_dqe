import csv
import re


class CSVCountOutput:
    """
    Object of CSVCountOutput class requires only file_name to be initialized
    self.file_data is reached via reading file data
    self.file_data value is used in words_from_text() method
    """
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'r') as source_file:
            self.file_data = source_file.read()

    def words_from_text(self):
        """
        Creating several lists:
        1. list_from_file_splitted - nested list that was created by firstly splitting text by whitespace and then splitting by new line symbol
            e.g. text 'Hi ----- I am Lera.\nNice to meet you.' will look like ['Hi','-----','I','am',['Lera.','Nice'],'to','meet','you.']
        2. flat_list_from_file_splitted - items are same as in previous list, but no nested lists inside
            e.g. previous list will look like ['Hi','-----','I','am', 'Lera.','Nice','to','meet','you.']
        3. flat_list_cleared - same as previous list but items that have no letter at all are removed
            e.g. previous list will look like ['Hi','I','am', 'Lera.','Nice','to','meet','you.']
            '-----' not included, but 'Lera.', 'you.' are included, because there are letters
        4. flat_list_only_words - this list is final and method returns exactly this list
        It includes all items from previous list if they don't have any special symbols (symbols are listed in 'regex' asssingning)
        If special symbols are in item then method will include in list only characters before the symbol.
            e.g. previous list will look like ['Hi','I','am', 'Lera','Nice','to','meet','you']
        :return: As long as only letters/words amount should be counted, this method returns list where element is a word
        """
        list_from_file_splitted = [i if '\n' not in i else i.split('\n') for i in self.file_data.split(' ')]
        flat_list_from_file_splitted = []
        for element in list_from_file_splitted:
            if type(element) is list:
                for item in element:
                    flat_list_from_file_splitted.append(item)
            else:
                flat_list_from_file_splitted.append(element)
        flat_list_cleared = [item for item in flat_list_from_file_splitted if any(symbol.isalpha() for symbol in item) is True]
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:,.(0-9)-]')
        flat_list_only_words = []
        for i in flat_list_cleared:
            if (regex.search(i) == None):
                flat_list_only_words.append(i)
            else:
                index_of_symbol = regex.search(i).span()[0]
                flat_list_only_words.append(i[0:index_of_symbol])
        return flat_list_only_words

    def word_count_dict(self):
        """
        Method counts elements from list returned by self.words_from_text() in form of a dictionary
        :return: Dictionary where key is word and value shows how many times this word appears in list
        """
        word_count_dict = {}
        for i in self.words_from_text():
            if i.lower() in word_count_dict.keys():
                word_count_dict[i.lower()] += 1
            else:
                word_count_dict[i.lower()] = 1
        return word_count_dict

    def lowercase_letter_count_dict(self):
        """
        Method counts elements in string in form of a dictionary, where string is a joined items from list that is returned by self.words_from_text()
        :return: Dictionary where key is a lowercased letter and value shows how many times this letter appears in list
        """
        letter_count_dict = {}
        for i in ('').join(self.words_from_text()):
            if i.lower() in letter_count_dict.keys():
                letter_count_dict[i.lower()] += 1
            else:
                letter_count_dict[i.lower()] = 1
        return letter_count_dict

    def uppercase_letter_count_dict(self):
        """
        Method counts only uppercased letters in string in form of a dictionary, where string is a joined items from list that is returned by self.words_from_text()
        :return: Dictionary where key is an uppercased letter and value shows how many times this letter appears in list
        """
        count_uppercase_dict = {}
        for i in ('').join(self.words_from_text()):
            if (i.isupper() is True) and i in count_uppercase_dict.keys():
                count_uppercase_dict[i] += 1
            elif (i.isupper() is True):
                count_uppercase_dict[i] = 1
        return count_uppercase_dict

    def create_csv_of_word_count(self, csv_file_name):
        """
        Method writes dictionary returned by word_count_dict() method into .csv file
        :param csv_file_name: name of the file where dict keys-values will be placed
        """
        with open(csv_file_name, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            for k, v in self.word_count_dict().items():
                wr.writerow([k, v])

    def create_csv_of_letter_count(self, csv_file_name):
        """
        Method writes dictionary returned by lowercase_letter_count_dict(), uppercase_letter_count_dict() method into .csv file
        CSV file has header ['letter', 'count_all', 'count_uppercase', 'percentage']
        'letter' - lowercased letter(key) from lowercase_letter_count_dict()
        'count_all' - value from lowercase_letter_count_dict() for this key
        'count_uppercase' - 0 if such 'letter', when uppercased, is not in uppercase_letter_count_dict()
            value from uppercase_letter_count_dict() if such 'letter', when uppercased, is in uppercase_letter_count_dict()
        'percentage' - calculates the percentage of how much current 'letter' (lowercased) appears in file in comparison with other letters
        :param csv_file_name: name of the file where values will be placed
        """
        with open(csv_file_name, 'w', newline='') as csvfile:
            wr = csv.DictWriter(csvfile, fieldnames=['letter', 'count_all', 'count_uppercase', 'percentage'])
            wr.writeheader()
            for k, v in self.lowercase_letter_count_dict().items():
                upper_count = 0
                if k.upper() in self.uppercase_letter_count_dict().keys():
                    upper_count += self.uppercase_letter_count_dict()[k.upper()]
                wr.writerow({
                    'letter': k,
                    'count_all': v,
                    'count_uppercase': upper_count,
                    'percentage': round((v * 100 / len(''.join(self.words_from_text()))), 2)
                })

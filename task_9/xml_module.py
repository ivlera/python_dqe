import os.path
from python_dqe.task_5.classes_oop import *
from python_dqe.task_6.module_classes import PublicationFromFile
from python_dqe.task_8.json_module import PublicationFromJSONFile
import xml.etree.ElementTree as ET


class PublicationFromXMLFile(PublicationFromFile):
    def __init__(self, user_file_name, file_path):
        """
        Same as for PublicationFromFile class there have to initialized file name and path.
        Inherit from parent PublicationFromFile in order to be able to use .publish() and .remove_file() methods and to reach self.user_file_full_path parameter
        self.json_data parameter is a dict from input json data
        """
        self.user_file_name = user_file_name
        self.file_path = file_path
        PublicationFromFile.__init__(self, user_file_name=self.user_file_name, file_path=self.file_path)
        self.xml_file = ET.parse(self.user_file_full_path)
        self.root = self.xml_file.getroot()

    def __str__(self):
        """
        Iterating through dictionary from json. Basing on 'type' value in json there will be created object of News or Advertisement class
        Method return string representation of a class, so method publish() will insert exact string from return to the file
        """
        list_of_feed = []
        for news_item in self.root.findall('news_item'):
            if news_item.attrib['type'].lower() == 'news':
                post = News(content=news_item.find('content').text,
                            city=news_item.find('city').text)
                list_of_feed.append(post.__str__())
            elif news_item.attrib['type'].lower() == 'ad':
                post = Advertisement(content=news_item.find('content').text,
                                     expire_date=datetime.strptime(news_item.find('expire_date').text, "%d/%m/%Y"))
                list_of_feed.append(post.__str__())
            else:
                print(f"<type> 'news' or <type> 'ad' was expected, but type = {news_item.attrib['type']} received")
        str_of_feed = ''.join(list_of_feed)
        lines = str_of_feed.count("\n")-1
        return f'\n\nFollowing {lines} lines received from file {self.user_file_name} on {self.current_date}{str_of_feed}'


def publish_from_file(target_file_name='/task_5/news.txt'):
    """
    Was created as a separate function cause user input is required.
    :param target_file_name: Name of the file where data will be written. Has default value of news.txt file from task 5.
    """

    # Explicitly deleting and adding '/' symbol at the beginning, so both '/task_5/news.txt' and 'task_5/news.txt' inputs will work
    target_file_name = '/' + target_file_name.lstrip('/')

    # Assinging a varible in order to start while loop. when while loop will finish execution, variable will be reassigned to the same string, so user could start loop execution again
    x = input(f'Please enter "y" if you want to add data from file to {target_file_name} news feed file: ')
    while x.lower() == 'y':
        # New variable to identify whether user wants to use default directory or some other
        user_dir_var = input('Enter "y" if required file is located in default directory "user_files/". Enter any other symbol if directory is different: ')

        # Following piece of code is for default directory
        if user_dir_var.lower() == 'y':
            # Listing files that exist in default directory to the console, so user can choose required file easily
            print(f'These are the files in "user_files" directory:')

            try: # this execution won't fail if publish_from_file() is called from main.py file
                file_path = os.path.abspath('.') + r'\user_files'
                for dir_item in os.listdir(file_path):
                    if dir_item != '__pycache__':
                        print(dir_item)
            # if above execution failed, then trying to open /user_files folder via passing '..' as absolute path value
            except FileNotFoundError: # this execution won't fail if publish_from_file() is called from file in task_#/ folder, for example task_8/json_module.py file
                file_path = os.path.abspath('..') + r'\user_files'
                for dir_item in os.listdir(file_path):
                    if dir_item != '__pycache__':
                        print(dir_item)

        # Following piece of code is for directory received from user
        else:
            # If provided directory doesn't exist then string from 'else' condition will be printed "Given path was not found. Try again."
            file_path = input(r'Please enter the absolute path of required directory: ')
            if os.path.exists(file_path) is True:
                print(f'These are the files in "{file_path}" directory:')
                for dir_item in os.listdir(file_path):
                    if dir_item != '__pycache__':
                        print(dir_item)
            else:
                print(f'\nGiven path "{file_path}" was not found. Try again.\n')
                # reassinging x to start while loop from very beginning
                x = input(f'Please enter "y" if you want to add data from file to {target_file_name} news feed file: ')
                # 'continue' statement jumps back up to the top of the loop, skipping other lines in while loop
                continue

        user_file = input('\nPlease, enter the name of required file: ') # asking user to enter the name of the file
        user_file_with_path = os.path.join(file_path, user_file)

        # If provided file name doesn't exist in default directory then string from 'else' condition will be printed out "File was not found. Try again."
        if os.path.isfile(user_file_with_path) is True:

            # If file has json extension then there will be created object from class PublicationFromJSONFile
            if user_file_with_path[-5::] == '.json':
                pub = PublicationFromJSONFile(user_file_name=user_file_with_path, file_path=None) # file_path='user_files' can also be declared
                try:
                    pub.publish(target_file_name=target_file_name)
                    # not calling remove_file() in case of json file, because this is not a part of hometask
                    print(
                        f"Data from '{pub.user_file_full_path}' was added to '{target_file_name}'")
                except KeyError: # KeyError could occur in case if json file has invalid structure
                    print('Provided json file structure is not valid.')

            # If file has xml extension then there will be created object from class PublicationFromXMLFile
            elif user_file_with_path[-4::] == '.xml':
                pub = PublicationFromXMLFile(user_file_name=user_file_with_path, file_path=None) # file_path='user_files' can also be declared
                try:
                    pub.publish(target_file_name=target_file_name)
                    # not calling remove_file() in case of xml file, because this is not a part of hometask
                    print(
                        f"Data from '{pub.user_file_full_path}' was added to '{target_file_name}'")
                except AttributeError: # AttributeError could occur in case if tag in xml file has different name
                    print('Provided xml file structure is not valid.')

            # If file has any other extension then there will be created object from class PublicationFromFile
            else:
                pub = PublicationFromFile(user_file_name=user_file_with_path, file_path=None) # file_path='user_files' can also be declared
                pub.publish(target_file_name=target_file_name)
                pub.remove_file()
                print(f"Data from '{pub.user_file_full_path}' was added to '{target_file_name}'. File '{pub.user_file_name}' was removed.")

        # User will see following message if os.path.isfile(user_file_with_path) returned False
        else:
            print(f'\nFile "{user_file_with_path}" was not found. Try again.\n')

        # Reassinging variable to restart loop
        x = input(f'Please enter "y" if you want to add data from file to {target_file_name} news feed file: ')
    return 'exit' # this string is returned to use it as a flag in main.py that user finished entering data

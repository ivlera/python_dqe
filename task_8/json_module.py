import json
import os.path
from python_dqe.task_5.classes_oop import *
from python_dqe.task_6.module_classes import *


class PublicationFromJSONFile(PublicationFromFile):
    def __init__(self, user_file_name, file_path):
        """
        Same as for PublicationFromFile class there have to initialized file name and path.
        Inherit from parent PublicationFromFile in order to be able to use .publish() and .remove_file() methods and to reach self.user_file_full_path parameter
        self.json_data parameter is a dict from input json data
        """
        self.user_file_name = user_file_name
        self.file_path = file_path
        PublicationFromFile.__init__(self, user_file_name=self.user_file_name, file_path=self.file_path)
        self.json_data = json.load(open(self.user_file_full_path))

    def __str__(self):
        """
        Iterating through dictionary from json. Basing on 'type' value in json there will be created object of News or Advertisement class
        Method return string representation of a class, so method publish() will insert exact string from return to the file
        """
        list_of_feed = []
        for i in self.json_data["news_items"]:
            if i['type'].lower() == 'news':
                post = News(content=i['content'], city=i['city'])
                list_of_feed.append(post.__str__())
            elif i['type'].lower() == 'ad':
                post = Advertisement(content=i['content'], expire_date=datetime.strptime(i['expire_date'], "%d/%m/%Y"))
                list_of_feed.append(post.__str__())
            else:
                print(f"type = 'news' or type = 'ad' was expected, but type = {i['type']} received")
        str_of_feed = ''.join(list_of_feed)
        lines = str_of_feed.count("\n")-1
        return f'\n\nFollowing {lines} lines received from file {self.user_file_name} on {self.current_date}{str_of_feed}'

import os
from python_dqe.task_4.functions import text_normalization
from python_dqe.task_5.classes_oop import Publication


class PublicationFromFile(Publication):
    def __init__(self, user_file_name, file_path):
        """
        Inherit from parent Publication class in order to use self.current_date and self.publish() method.
        user_file_full_path: was declared in order not to call os.join method every time
        """
        super().__init__()
        self.user_file_name = user_file_name
        if file_path is None: # if file name was provided as None - using default folder
            self.file_path = 'user_files'
        else:
            self.file_path = file_path
        self.user_file_full_path = os.path.join(self.file_path, self.user_file_name)

    def __str__(self):
        """
        Returns human-readable string representation of content + one line that defines how many lines file contains and name of the file.
        """
        with open(self.user_file_full_path, 'r') as f:
            list_from_file = f.readlines()
            string_from_file = "".join(list_from_file)
            return f'\n\nFollowing {len(list_from_file)} lines received from file {self.user_file_full_path} on {self.current_date}\n\n{string_from_file}'

    def remove_file(self):
        """
        Method removes the file.
        """
        os.remove(self.user_file_full_path)


def publish_from_file(target_file_name='python_dqe/task_5/news.txt'):
    """
    Was created as a separate function cause user input is required.
    :param target_file_name: Name of the file where data will be written. Has default value of news.txt file from task 5.
    """
    # Assinging a varible in order to start while loop. when while loop will finish execution, variable will be reassigned to the same string, so user could start loop execution again
    x = input(f'Please enter "y" if you want to add data from file to {target_file_name} news feed file: ')
    while x.lower() == 'y':
        # New variable to identify whether user wants to use defult directory or some other
        user_dir_var = input('Enter "y" if required file is located in default directory "user_files/". Enter any other symbol if directory is different: ')
        # Following piece of code is for default directory
        if user_dir_var.lower() == 'y':
            # Listing files that exist in default directory to the console, so user can choose required file easily
            print('These are the files in "user_files" directory:')
            for i in os.listdir('user_files'):
                if i != '__pycache__': # excluding non-related folder
                    print(i)
            user_file = input('\nPlease, enter the name of required file: ')
            user_file_with_path = os.path.join('user_files', user_file)
            # If provided file name doesn't exist in default directory then string from 'else' condition will be printed out "File was not found. Try again."
            if os.path.exists(user_file_with_path) is True:
                # Creating class object and calling inherited publish() method and new remove_file() method
                pub = PublicationFromFile(user_file_name=user_file, file_path=None) # file_path='user_files' can also be declared
                pub.publish(target_file_name)
                pub.remove_file()
                print(
                    f"Data from '{pub.user_file_full_path}' was added to '{target_file_name}'. File '{pub.user_file_name}' was removed.")
            else:
                print(f'\nFile "{user_file_with_path}" was not found. Try again.\n')
        # Following piece of code is for directory other than default
        else:
            directory = input(r'Please enter the path of required directory: ')
            # If provided directory doesn't exist then string from 'else' condition will be printed "Given path was not found. Try again."
            if os.path.exists(directory) is True:
                print(f'These are the files in "{directory}" directory:')
                for i in os.listdir(directory):
                    if i != '__pycache__':
                        print(i)
                user_file = input('\nPlease, enter the name of required file: ')
                user_file_with_path = os.path.join(directory, user_file)
                # If provided file name doesn't exist in default directory then string from 'else' condition will be printed out "File was not found. Try again."
                if os.path.exists(user_file_with_path) is True:
                    # Creating class object and calling inherited publish() method and new remove_file() method
                    pub = PublicationFromFile(user_file_name=user_file, file_path=directory)
                    pub.publish(target_file_name)
                    pub.remove_file()
                    print(
                        f"Data from '{pub.user_file_full_path}' was added to '{target_file_name}'. File '{pub.user_file_name}' was removed.")
                else:
                    print(f'\nFile "{user_file_with_path}" was not found. Try again.\n')
            else:
                print(f'\nGiven path "{directory}" was not found. Try again.\n')
        x = input(f'Please enter "y" if you want to add data from file to {target_file_name} news feed file: ')


def file_data_case_normalization(file_name, file_path=''):
    """
    Function that applies text_normalization() to the text in file
    """
    with open(os.path.join(file_path, file_name), "r") as f_read:
        file_data = f_read.readlines()
        with open(os.path.join(file_path, file_name), "w") as f_wr:
            f_wr.write(text_normalization(''.join(file_data)))
        return text_normalization(''.join(file_data))

# python_dqe
User is supposed to run main.py file.

### Step 1

After running main.py, user will be offered two options:

*Please enter 1 if you want to add data to news feed through console*

*Please enter 2 if you want to add data from file*

#### Step 1.1
If in *Step 1* user input is __1__ - this is task 5 implementation (input of news feed items by user via the console):
 1. User will have to confirm choosing this option by entering __1__. In case if input is different, user will see input from *Step 1*.
 2. User will have to choose the category (news, ad or joke) by entering __1__, __2__ or __3__. In case if input is different, user will see input from point 1.
 3. In case of successfull publishing of news feed item or if news feed item failed to publish (e.g. because wrong date format was entered, or in above option user input was different from __1__, __2__ or __3__) - user will will see input from *Step 1*.

#### Step 1.2
If in *Step 1* user input is __2__ - this is tasks 6, 8, 9 implementation (publication of news feed items from selected file, programm is able to read data from .txt, .xml and .json files)
 1. User will have to confirm choosing this option by entering __y__. If user input is different from __y__, then user will see input from *Step 1*
 2. User will have to confirm choosing the default [user_files/](https://github.com/ivlera/python_dqe/blob/main/user_files) directory by entering __y__. If input is different from __y__ - user will be asked to enter the full path of the directory where required file is located.
 3. User will see list of files within the provided or default directory. User will be asked to enter the name of required file.
 4. If path entered in point 3 and/or file name entered in point 4 is incorrect or doesn't exist - user will see input from point 1.

```
txt files are deleted after data from file was successfully published to the target news feed file. 

json and xml files are not deleted after processing.
```

Expected JSON file structure can be viewed in [python_dqe/user_files/news2.json](https://github.com/ivlera/python_dqe/blob/main/user_files/news2.json)

Expected XML file structure can be viewed in [python_dqe/user_files/news3.xml](https://github.com/ivlera/python_dqe/blob/main/user_files/news3.xml)

```
DD/MM/YYYY is expected date format for user input and json/xml files.
```

### Step 2

User will be asked if he wants to apply case normalization to the target file.

*Please enter 1 if you want to apply case normalization to task_5/news.txt file*

If user enters __1__ - case normalization functionality from task_6.module_classes, function file_data_case_normalization() will be applied to the news feed file data. If user input is different from __1__, then program will finish execution.

### Output csv files

Method that updates data in CSV files where letters and words are counted is called every time new publication arrives to the target news feed file. 

- [task_5/letter_count.csv](https://github.com/ivlera/python_dqe/blob/main/task_5/letter_count.csv)
- [task_5/word_count.csv](https://github.com/ivlera/python_dqe/blob/main/task_5/word_count.csv)

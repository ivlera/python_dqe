from python_dqe.task_5.classes_oop import publish_from_console
from python_dqe.task_9.xml_module import publish_from_file
from python_dqe.task_6.module_classes import file_data_case_normalization


if __name__ == '__main__':

    news_feed_file = "task_5/news.txt"

    x = input('Please enter 1 if you want to add data to news feed through console\nPlease enter 2 if you want to add data from file\n')
    while x.strip() in ('1', '2'):
        rerun_flag = ''
        if x == '1':
            if publish_from_console(news_feed_file) == 'exit':
                x = input(
                    'Please enter 1 if you want to add data to news feed through console\nPlease enter 2 if you want to add data from file\n')
        elif x == '2':
            if publish_from_file(news_feed_file) == 'exit':
                x = input(
                    'Please enter 1 if you want to add data to news feed through console\nPlease enter 2 if you want to add data from file\n')

    normalization_required = input(f'\nPlease enter 1 if you want to apply case normalization to {news_feed_file} file\n')
    if normalization_required == '1':
        file_data_case_normalization(news_feed_file)

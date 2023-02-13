from datetime import datetime
import calendar
import random


class Publication:
    '''
    A parent class that initializes attribute that every child class requires: current date
    Method publish(file_name) adds content to the file (news.txt by default, but name of the file can be entered by user as an input parameter)
    Method publish() adds to the file string representation of content
    Human-readable string representation of content is defined in every child class via __str__ dunder method. It unites parameters into content following strict predefined pattern that is different within child classes
    '''
    def __init__(self):
        self.current_date = datetime.now().strftime("%d/%m/%Y %H:%M")

    def publish(self, file_name="news.txt"):
        with open(file_name, "a") as f:
            f.write(self.__str__())


class News(Publication):
    '''
    The class that is inherited from Publication, so it has self.current_date parameter and method publish()
    self.content and self.city parameters should be entered while initializing the object of the class
    __str__ dunder method is used to unite parameters into text following strict predefined pattern

    '''
    def __init__(self, content, city):
        super().__init__()
        self.content = content
        self.city = city

    def __str__(self):
        return f'\n\nNews -----------------------\n{self.content}\n{self.city},  {self.current_date}'


class Advertisement(Publication):
    '''
    The class that is inherited from Publication, so it has self.current_date parameter and method publish()
    self.content and self.expire_date parameters should be entered while initializing the object of the class
    self.days_left parameter is calculated based on self.current_date and self.expire_date
    __str__ dunder method is used to unite parameters into text following strict predefined pattern
    '''
    def __init__(self, content, expire_date):
        super().__init__()
        self.content = content
        self.expire_date = expire_date
        self.days_left = (expire_date - datetime.strptime(self.current_date, "%d/%m/%Y %H:%M")).days
        if self.days_left < 0:
            self.days_left = 0

    def __str__(self):
        return f"\n\nPrivate Ad -----------------\n{self.content}\nActual until: {str(self.expire_date)[0:10]},  {self.days_left} days left"


class WeekdayJoke(Publication):
    '''
    The class that is inherited from Publication, so it has self.current_date parameter and method publish()
    self.day parameter is calculated based on self.current_date parameter value
    self.jokes is a list of 7 jokes. In __str__ method there is one joke selected based on what is the current day of the week
    Day of the week is selected from self.day parameter via day_name method from calendar module
    self.funnymeasure is a random number from 0 to 4. Such range was chosen because, to be honest, jokes in self.jokes are not funny enough to be 5 of 10 :(
    __str__ dunder method is used to unite parameters into text following strict predefined pattern
    '''
    def __init__(self):
        super().__init__()
        self.day = datetime.strptime(self.current_date, "%d/%m/%Y %H:%M").weekday()
        self.jokes = [
            'What do you call a fish without eyes? Fsh.',
            'What do you call an alligator detective? An investi-gator.',
            'What do you call a pig that does karate? A pork chop.',
            'Why are there gates around cemeteries? Because people are dying to get in.',
            'What kind of music do planets like? Neptunes.',
            'Where can you buy chicken broth in bulk? The stock market.',
            'Why do bees have sticky hair? Because they use honeycombs.'
        ]
        self.funnymeasure = random.randint(0, 4)

    def __str__(self):
        return f"\n\nJoke of the day ------------\nToday is {calendar.day_name[self.day]} and here is the joke:\n{self.jokes[self.day]}\nProgram rates this joke as {self.funnymeasure} of 10"


def publishment(file_name):
    '''
    Function writes the condition into the console. Based on user input it creates the object of one from three classes with user inputs as a parameters to initialize the object.
    After all parameters are known and object is created, function calls publish() method in order to add string representation of a class into file
    :param file_name: Name of the file where news feed items will be added. Any existing text file in current folder can be chosen here.
    '''
    with open(file_name, "r") as f:
        # This piece of code is required in order to add 'header' to the file in case of file is empty
        if f.readlines() == []:
            f = open(file_name, "w")
            f.write("News feed")
            f.close()
    # Assigning x to input from user, so if 1 will be received, then 'while' clause will start execution. If user will enter any symbol, different from '1', then function will finish execution
    x = input("Please enter 1 if you want to add item to the newspaper\n")
    while x == '1':
        # Assigning a number to the variable. Basing on what the number is, there will be created object from one of three classes with different parameters.
        # If input from user is not '1', '2' or '3' then in the console user will see "Wrong choice...." message and x variable will be reassigned (line 124)
        input_number = input("Please select the category of your publication:\nEnter 1 for News\nEnter 2 for Advertisement\nEnter 3 for Joke of the day\n")
        if input_number == '1':
            content = input("Enter your text: ")
            city = input("Enter the city: ")
            post = News(content, city)
            post.publish(file_name)
        elif input_number == '2':
            content = input("Enter your text: ")
            try:
            # Error handling here is required in order to continue function execution even if user entered date in wrong format
            # If date is in correct format, then object will be created and publish() method will be executed
                expire_date = datetime.strptime(input("Enter the expire date in DD/MM/YYYY format: "), "%d/%m/%Y")
                post = Advertisement(content, expire_date)
                post.publish(file_name)
            except ValueError:
            # If date is not in correct format, then error message will be printed to the console and x variable will be reassigned (line 124)
                print('Wrong date format. DD/MM/YYYY format is expected. Try again')
        elif input_number == '3':
            post = WeekdayJoke()
            post.publish(file_name)
        else:
            # If none of 3 'if' conditions were True, i.e. if user input was not in [1, 2, 3], then user will see following message in the console and user will have to start entering numbers from very beggining
            print("Wrong choice. Please, review the condition again, you should enter only 1, 2 or 3.")
        # Again assigning x to input from user, so if 1 will be received, then 'while' clause will start execution
        x = input("Please enter 1 if you want to add item to the newspaper\n")


publishment("news.txt")

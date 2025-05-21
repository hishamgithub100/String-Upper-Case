#create class
class IOString():

    #Constructor to set default value
        def __init__(self):
                self.str1 = ''
    #function to get input from user
        def get_string(self):
                self.str1 = input("Enter String : ")
    #function to print the string in upper case
        def print_string(self):
                print("Result is: " , self.str1.upper())

#object creation
str1 = IOString()

#call function
str1.get_string()
str1.print_string()

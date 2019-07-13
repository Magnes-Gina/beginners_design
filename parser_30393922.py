# Author: Mary Agnes Joseph
# Student ID: 30393922
# Start Date: 15th May 2019
# Last Modified Date: 21st May 2019

from datetime import datetime  # Incorporate datetime to convert string to datetime object
from preprocessData_30393922 import preprocessLine  # Incorporate preprocessLine()
import string  # Incorporate String manipulation methods
import re  # Make use of regular expression


class Parser:
    """Class to define various attributes for object."""
    def __init__(self, inputString):
        self.inputString = inputString
        self.ID = self.getID()
        self.type = self.getPostType()
        self.dateQuarter = self.getDateQuarter()
        self.cleanBody = self.getCleanedBody()
        self.vocabularySize = self.getVocabularySize()

    """The below method accepts an inout line returns the row ID for each line. 
    This is achieved through regular expression and string manipulation."""
    def getID(self):
        if "Id" in self.inputString:
            pattern = re.search("""Id="\d+""", self.inputString)
            # Looks for the location where regex produces a match and return a match object
            index = pattern.start()  # Assigns the indices of start of sub-string matched by pattern
            index_n = pattern.end()   # Assigns the end of the index of string "ID=1"
            self.ID = self.inputString[index+4:index_n]  # Slices the string to retrieve the ID
            return self.ID

    """The below method is used to present the attributes of an object in a printable human readable form"""
    def __str__(self):
        # print ID, Question/Answer/Others, creation date, the main content
        return "ID : " + str(self.getID())+" " + "PostType Id: " + str(self.getPostType()) + " " + "Quarter: " + str(self.getDateQuarter()) + " Body : " + " " + str(self.getCleanedBody()) + " " + "Unique Words" + " " + str(self.getVocabularySize())

    """The below method accepts an input line and return the Post Type of each row.
    This is achieved through slicing. If an ID is between 3 and 8, then it is coded to return others"""
    def getPostType(self):
        if "PostTypeId" in self.inputString:
            index = self.inputString.index("PostTypeId")  # Assigns the start of the index of string PostTypeID
            self.type = self.inputString[index+12:index+13]  # Slices the string and assigns the ID to self.type
            if "3" <= self.type <= "8":  # Codes the value "others" if ID is between 3 and 8
                self.type = "Others"
                return self.type
            return self.type  # Else returns either 1 or 2, depending on the value in each post.

    """The  below method accepts an input string and return the Creation Date for each row. 
    It makes use of date library to get the Creation data in YYYY-MM-DD format. 
    Based on the month the quarters are categorized as Q1, Q2,Q3,Q4"""
    def getDateQuarter(self):
        if "CreationDate" in self.inputString:
            index = self.inputString.index("CreationDate")
            self.dateQuarter = self.inputString[index+14:index+24]
            self.dateQuarter = datetime.strptime(self.dateQuarter, '%Y-%m-%d')  # String is parsed to datetime object
            quarter = self.dateQuarter.month
            # Conditional statements to assign the month to the right quarter
            if 1 <= quarter <= 3:
                quarter = "Q1"
                return str(self.dateQuarter.year)+quarter
            elif 4 <= quarter <= 6:
                quarter = "Q2"
                return str(self.dateQuarter.year)+quarter
            elif 7 <= quarter <= 9:
                quarter = "Q3"
                return str(self.dateQuarter.year)+quarter
            elif 10 <= quarter <= 12:
                quarter = "Q4"
                return str(self.dateQuarter.year)+quarter  # Concatenating the year and the quarter

    """The below method reads each line and uses the preprocessLine() defined in first module to cleaned the body"""
    def getCleanedBody(self):
        self.cleanBody = preprocessLine(self.inputString)
        if "Body=" in self.cleanBody:
            index = self.cleanBody.index("Body=")  # Finding the index of the string "Body="
            self.cleanBody = self.cleanBody[index+5:]  # Slicing the string to retrieve only the content of body tag
        return self.cleanBody

    """The below method reads each line and uses the cleaned body content obtained 
    from the getCleanedBody() to obtain unique words in each line."""
    def getVocabularySize(self):
        self.vocabularySize = self.getCleanedBody()
        for line in string.punctuation:
            self.vocabularySize = self.vocabularySize.replace(line, '')
            # Replacing the punctuation present in string with null value
        self.vocabularySize = self.vocabularySize.lower()  # Converting the entire string to lower case
        self.vocabularySize = len(set(self.vocabularySize.split()))
        # Splitting the string by spaces and adding it to a set to find the number of unique words
        return self.vocabularySize


readLine = open("data.xml", "r")
# readLine holds a reference to file object returned by open function.

for each in readLine:
    eachLine = Parser(each)  # Instantiate an object of type Parser
    print(eachLine)
readLine.close()  # The file is closed.


# Author: Mary Agnes Joseph
# Student ID: 30393922
# Start Date: 12th May 2019
# Last Modified Date: 21st May 2019

import re  # Make use of regular expression


# The below function is used to remove the xml encoding line with which the xml file begins.
""" Each of the function below checks if the input is a string or not. The string condition is
checked as in the second module the input is given one line at a time. In this module the 
the data is read and stored in the list, hence the not string condition is checked. """


def read(f_readfile):
    # Takes input as a line from the data.xml file and writes it to a list.
    result = []
    if type(f_readfile) != str:
        for eachItem in f_readfile:
            result.append(eachItem)
        return result
    if type(f_readfile) == str:
        return f_readfile


"""Below function is programmed to remove the trailing < and /> tags from each of the posts
, this is achieved through string manipulation."""


def pre_processing(f_read_data):
    result = []  # list to store data after removing the tags
    if type(f_read_data) != str:
        for eachItem in f_read_data:
            i = 0  # for loop traversal
            index = 0  # stores the index of "<"
            next_index = 0  # stores the index of "/"

            while i < len(eachItem):
                if eachItem[i] == "<":
                    index = i
                if eachItem[i] == "/":
                    next_index = i
                removed_tags = eachItem[index+1:next_index]
                # Slicing the string to obtain data between opening and closing tags
                i += 1
            result.append(removed_tags)  # List appended after each line goes through the cleaning process
        return result
    if type(f_read_data) == str:
        i = 0
        index = 0
        next_index = 0
        while i < len(f_read_data):
            if f_read_data[i] == "<":
                index = i
            if f_read_data[i] == "/":
                next_index = i
            removed_tags = f_read_data[index+1:next_index]
            i += 1
        return removed_tags


"""The below function is used to replace character reference with their original form.
It makes use of the string.replace() to achieve the same"""


def pre_processing_special(f_processed_data):
    result = []  # list to store data after removing the tags
    if type(f_processed_data) != str:
        #  Conditional statement to replace the special characters with the original form.
        for each_item in f_processed_data:
            each_item = each_item.replace('&lt;', '<')
            each_item = each_item.replace('lt;', '<')
            each_item = each_item.replace('&gt;', '>')
            each_item = each_item.replace('gt;', '<')
            each_item = each_item.replace('&apos;', '\'')
            each_item = each_item.replace('&amp;', '&')
            each_item = each_item.replace('amp;', '')
            each_item = each_item.replace('&quot', '"')
            each_item = each_item.replace('&#xA;', '')
            each_item = each_item.replace('&#xD;', '')
            result.append(each_item)
        return result
    if type(f_processed_data) == str:
        f_processed_data = f_processed_data.replace('&lt;', '<')
        f_processed_data = f_processed_data.replace('lt;', '<')
        f_processed_data = f_processed_data.replace('&gt;', '>')
        f_processed_data = f_processed_data.replace('gt;', '<')
        f_processed_data = f_processed_data.replace('&apos;', '\'')
        f_processed_data = f_processed_data.replace('&amp;', '&')
        f_processed_data = f_processed_data.replace('amp;', '')
        f_processed_data = f_processed_data.replace('&quot', '"')
        f_processed_data = f_processed_data.replace('&#xA;', ' ')
        f_processed_data = f_processed_data.replace('&#xD;', ' ')
        return f_processed_data


"""The below function is used to remove the HTML/XML tags and replace it with spaces. 
This is achieved by regular expressions."""


def pre_processing_tags(f_processed_data_spl):
    result = []  # list to store data after removing the tags
    if type(f_processed_data_spl) != str:
        # Conditional statement to remove the HTML tags
        for eachItem in f_processed_data_spl:
            removed_tags = re.sub("<\w*>|</\w*>|<\w*/>|<\w*\s/>|<\w*;>|<ol.*;>|<img.*;\s/>|<a.*</a>|<img.*;>", " ", eachItem)
            result.append(removed_tags)
        return result
    if type(f_processed_data_spl) == str:
        removed_tags = re.sub("<\w*>|</\w*>|<\w*/>|<\w*\s/>|<\w*;>|<ol.*;>|<img.*;\s/>|<a.*</a>|<img.*;>", " ", f_processed_data_spl)
        return removed_tags


"""Function that is called to pre-process and clean each line.
It in turns makes use of the other functions written above to achieve the same."""


def preprocessLine(f_readFile):
    # pre-process the data in each line
    if type(f_readFile) != str:
        read_data = read(f_readFile)
        processed_data = pre_processing(read_data)
        processed_data_spl = pre_processing_special(processed_data)
        processed_data_tags = pre_processing_tags(processed_data_spl)
        return processed_data_tags
    if type(f_readFile) == str:
        processed_data = pre_processing(f_readFile)
        processed_data_spl = pre_processing_special(processed_data)
        processed_data_tags = pre_processing_tags(processed_data_spl)
        return processed_data_tags


"""This function is used to split the cleaned body/content into two files based on the Post Type ID.
The questions are placed in questions.txt and answers.txt. It takes three arguments
, the input file, output_question, output_answer"""


def splitFile(inputFile, outputFile_question, outputFile_answer):
    # pre-process the original file, and split them into two files.
    # please call pre-processLine() function within this function
    readfile = open(inputFile, "r")  # readfile references to the input file-data.xml
    question = open(outputFile_question, "w")  # question references to the output file- questions
    answer = open(outputFile_answer, "w")  # answer references to the output file-answers
    cleaned_data = preprocessLine(readfile)
    # cleaned_data contains cleaned data row by row.
    if type(cleaned_data) != 'str':
        # Conditional statement to split the files based on post ID.
        for each in cleaned_data:
            if """PostTypeId="1""" in each:
                index = each.index("Body=")
                each = each[index + 6:]
                each = each.strip()
                each = each.rstrip('\"')
                question.write(each)
                question.write("\n")
            elif """PostTypeId="2""" in each:
                index = each.index("Body=")
                each = each[index + 6:]
                each = each.strip()
                each = each.rstrip('\"')
                answer.write(each)
                answer.write("\n")
    readfile.close()
    question.close()
    answer.close()  # Closing the file

# The program starts from this point


if __name__ == "__main__":
    f_data = "data.xml"  # Data set for the program
    f_question = "question.txt"
    f_answer = "answer.txt"
    splitFile(f_data, f_question, f_answer)  # Calling the split file function



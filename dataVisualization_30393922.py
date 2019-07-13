# Author: Mary Agnes Joseph
# Student ID: 30393922
# Start Date: 18th May 2019
# Last Modified Date: 22nd May 2019

from parser_30393922 import Parser  # Importing Parser class
import numpy as np  # To build a numpy array
import matplotlib.pyplot as plt  # To plot a graph


"""The below function will calculate the number of questions 
and answers in each quarter to plot a line graph"""


def visualizeWordDistribution(inputFile, outputImage):
    i = 0  # To traverse the loop
    duplicates = []  # A list that is used to store the vocabulory size
    read_file = open(inputFile, "r", encoding="utf-8")   # Reading the data set and returning a reference to file object
    for eachLine in read_file:  # Iterating and referring to each row
        each = Parser(eachLine)   # Instantiate object of type Parser
        duplicate_words = each.getVocabularySize()  # Retrieving the vocabulory size of each row
        duplicates.append(duplicate_words)   # Appending the vocabulory size of each row to the list
    values = {}  # Creating a dictionary to store vocabulory size:number of posts
    # Below conditional statement loops through the duplicates list
    # to find out number of posts for each vocabulory size
    while i < len(duplicates):
        j = 0
        count = 0
        while j < len(duplicates):
            if duplicates[i] == duplicates[j]:
                result = duplicates[i]  # result represent the vocabulory size
                count += 1  # count represent number of posts with same size
                values[result] = count
            else:
                result = duplicates[i]
                values[result] = count
            j += 1

        i += 1
    vocab_size = []
    number_of_posts = []

    for key, value in values.items():
        vocab_size.append(key)
        number_of_posts.append(value)
    # Saving the key and value of dictionary values to vocab_size and number_of_posts lists respectively
    # Frequency of the data is calculated to plot the data in an interval of 10
    frequency = 11*[0]  # Frequency array is defined to categorize the values accordingly
    # Vocab size values are categorized based on the range with an interval set to 10.
    for each in vocab_size:
        if 0 <= each < 10:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[0] += value
        elif 10 <= each < 20:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[1] += value
        elif 20 <= each < 30:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[2] += value
        elif 30 <= each < 40:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[3] += value
        elif 40 <= each < 50:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[4] += value
        elif 50 <= each < 60:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[5] += value
        elif 60 <= each < 70:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[6] += value
        elif 70 <= each < 80:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[7] += value
        elif 80 <= each < 90:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[8] += value
        elif 90 <= each < 100:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[9] += value
        else:
            i = vocab_size.index(each)
            value = number_of_posts[i]
            frequency[10] += value

    # group_labels are assigned for x-axis
    group_labels = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100", "Others"]
    y_pos = np.arange(len(frequency))  # Define the range of x-axis
    plt.style.use('ggplot')  # Defines the style of the plot
    plt.bar(y_pos, frequency, alpha=1.0, color=(0.2, 0.4, 0.6, 0.6))
    # Bar graph is plotted with y_pos as x-axis and frequency as y-axis
    plt.xticks(y_pos, group_labels)  # Defines positions where the ticks have to be placed
    plt.tick_params(axis='x', colors='black', direction='out', length=5, width=3)
    # Defines the tick parameters for x-axis
    plt.xlabel('Vocabulary Size', fontsize=10)  # Setting the label for x-axis
    plt.ylabel('Number of Words', fontsize=10)  # Setting the label for y-axis
    figure = plt.gcf()  # Retrieving the current plotted figure
    figure.set_size_inches(8, 4)  # Setting the size of the layout of the graph
    plt.title('Vocabulary Size Distribution', fontsize=15)  # Setting the title of the plot
    plt.savefig(outputImage)  # Saving the figure as wordNumberDistribution.png
    plt.clf()  # Clears the figure
    read_file.close()  # Closing the file

def visualizePostNumberTrend(inputFile, outputImage):
    read_file = open(inputFile, "r", encoding="utf-8")  # Reading the data set and returning a reference to file object
    # Initializing variables to store number of questions and answers in each yearly-quarter
    q15_questions, q15_answers, q35_questions, q35_answers, q25_questions, q25_answers, q45_questions, q45_answers = 0, 0, 0, 0, 0, 0, 0, 0
    q16_questions, q16_answers, q26_questions, q26_answers, q36_questions, q36_answers, q46_questions, q46_answers = 0, 0, 0, 0, 0, 0, 0, 0
    q17_questions, q17_answers, q27_questions, q27_answers, q37_questions, q37_answers, q47_questions, q47_answers = 0, 0, 0, 0, 0, 0, 0, 0
    q18_questions, q18_answers, q28_questions, q28_answers, q38_questions, q38_answers, q48_questions, q48_answers = 0, 0, 0, 0, 0, 0, 0, 0
    q19_questions, q19_answers, q29_questions, q29_answers, q39_questions, q39_answers, q49_questions, q49_answers = 0, 0, 0, 0, 0, 0, 0, 0
    # Processing data line by line
    for eachLine in read_file:
        each = Parser(eachLine)  # Instantiate object of type Parser
        # Below conditional statements calculates the number of questions and answers
        # from the post_type in each yearly quarter.
        if "2015Q1" in str(each.getDateQuarter()):
            q1_15 = str(each.getPostType())
            if "1" in q1_15:
                q15_questions += 1
            if "2" in q1_15:
                q15_answers += 1
        elif "2015Q2" in str(each.getDateQuarter()):
            q2_15 = str(each.getPostType())
            if "1" in q2_15:
                q25_questions += 1
            if "2" in q2_15:
                q25_answers += 1
        elif "2015Q3" in str(each.getDateQuarter()):
            q3_15 = str(each.getPostType())
            if "1" in q3_15:
                q35_questions += 1
            if "2" in q3_15:
                q35_answers += 1
        elif "2015Q4" in str(each.getDateQuarter()):
            q4_15 = str(each.getPostType())
            if "1" in q4_15:
                q45_questions += 1
            if "2" in q4_15:
                q45_answers += 1
        elif "2016Q1" in str(each.getDateQuarter()):
            q1_16 = str(each.getPostType())
            if "1" in q1_16:
                q16_questions += 1
            if "2" in q1_16:
                q16_answers += 1
        elif "2016Q2" in str(each.getDateQuarter()):
            q2_16 = str(each.getPostType())
            if "1" in q2_16:
                q26_questions += 1
            if "2" in q2_16:
                q26_answers += 1
        elif "2016Q3" in str(each.getDateQuarter()):
            q3_16 = str(each.getPostType())
            if "1" in q3_16:
                q36_questions += 1
            if "2" in q3_16:
                q36_answers += 1
        elif "2016Q4" in str(each.getDateQuarter()):
            q4_16 = str(each.getPostType())
            if "1" in q4_16:
                q46_questions += 1
            if "2" in q4_16:
                q46_answers += 1
        elif "2017Q1" in str(each.getDateQuarter()):
            q1_17 = str(each.getPostType())
            if "1" in q1_17:
                q17_questions += 1
            if "2" in q1_17:
                q17_answers += 1
        elif "2017Q2" in str(each.getDateQuarter()):
            q2_17 = str(each.getPostType())
            if "1" in q2_17:
                q27_questions += 1
            if "2" in q2_17:
                q27_answers += 1
        elif "2017Q3" in str(each.getDateQuarter()):
            q3_17 = str(each.getPostType())
            if "1" in q3_17:
                q37_questions += 1
            if "2" in q3_17:
                q37_answers += 1
        elif "2017Q4" in str(each.getDateQuarter()):
            q47_15 = str(each.getPostType())
            if "1" in q47_15:
                q47_questions += 1
            if "2" in q47_15:
                q47_answers += 1
        elif "2018Q1" in str(each.getDateQuarter()):
            q1_18 = str(each.getPostType())
            if "1" in q1_18:
                q18_questions += 1
            if "2" in q1_18:
                q18_answers += 1
        elif "2018Q2" in str(each.getDateQuarter()):
            q2_18 = str(each.getPostType())
            if "1" in q2_18:
                q28_questions += 1
            if "2" in q2_18:
                q28_answers += 1
        elif "2018Q3" in str(each.getDateQuarter()):
            q3_18 = str(each.getPostType())
            if "1" in q3_18:
                q38_questions += 1
            if "2" in q3_18:
                q38_answers += 1
        elif "2018Q4" in str(each.getDateQuarter()):
            q4_18 = str(each.getPostType())
            if "1" in q4_18:
                q48_questions += 1
            if "2" in q4_18:
                q48_answers += 1
        elif "2019Q1" in str(each.getDateQuarter()):
            q1_19 = str(each.getPostType())
            if "1" in q1_19:
                q19_questions += 1
            if "2" in q1_19:
                q19_answers += 1
        elif "2019Q2" in str(each.getDateQuarter()):
            q2_19 = str(each.getPostType())
            if "1" in q2_19:
                q29_questions += 1
            if "2" in q2_19:
                q29_answers += 1
        elif "2019Q3" in str(each.getDateQuarter()):
            q3_19 = str(each.getPostType())
            if "1" in q3_19:
                q39_questions += 1
            if "2" in q3_19:
                q39_answers += 1
        elif "2019Q4" in str(each.getDateQuarter()):
            q4_19 = str(each.getPostType())
            if "1" in q4_19:
                q49_questions += 1
            if "2" in q4_19:
                q49_answers += 1
    # Defining a list number_of_questions and number_of_answers to store
    # the total number of question and answers in each quarter
    number_of_questions = [q15_questions, q25_questions, q35_questions, q45_questions, q16_questions, q26_questions, q36_questions, q46_questions, q17_questions, q27_questions, q37_questions, q47_questions, q18_questions, q28_questions, q38_questions, q48_questions, q19_questions, q29_questions, q39_questions, q49_questions]
    number_of_answers = [q15_answers, q25_answers, q35_answers, q45_answers, q16_answers, q26_answers, q36_answers, q46_answers, q17_answers, q27_answers, q37_answers, q47_answers, q18_answers, q28_answers, q38_answers, q48_answers, q19_answers, q29_answers, q39_answers, q49_answers]
    quarter = ["2015Q1", "2015Q2", "2015Q3", "2015Q4", "2016Q1", "2016Q2", "2016Q3", "2016Q4","2017Q1", "2017Q2", "2017Q3", "2017Q4","2018Q1", "2018Q2", "2018Q3", "2018Q4", "2019Q1", "2019Q2", "2019Q3", "2019Q4"]
    plt.style.use("seaborn-dark-palette")  # Defining the style of plot
    plt.plot(quarter, number_of_questions, label="Questions", linestyle='-', linewidth=2, color="red")
    # Plotting the line graph, with quarter in x-axis and number of questions in y-axis
    figure = plt.gcf()  # Current figure is retrieved
    figure.set_size_inches(8, 4)  # Control the size of the layout of the graph
    plt.plot(quarter, number_of_answers, label="Answers", linestyle='-.', linewidth=2)
    # Plotting the second line, with quarter in x-axis and number of answers in y-axis
    plt.xlabel("Quarter", fontsize=15, family='Arial', weight='bold')  # Setting label for x-axis
    plt.ylabel("Questions and Answers", fontsize=15, family='Arial', weight='bold')  # Setting label for y-axis
    plt.title("Post Number Trend", fontsize=15, family='Arial', weight='bold')  # Setting title for the plot
    plt.xticks(rotation=30, horizontalalignment='right')  # Aligning the x-ticks to prevent overlapping
    plt.legend()  # Creating a legend for the two plotted lines
    plt.savefig(outputImage)  # Saving the graph as PostNumberTrend.png
    plt.clf()  # Clearing the figure
    read_file.close()  # Closing the file


"""Below method is used to find number of posts with
same unique words and plot them with an interval of 10."""


if __name__ == "__main__":  # Program starts here
    f_data = "data.xml"
    f_wordDistribution = "wordNumberDistribution.png"
    f_postTrend = "postNumberTrend.png"

    visualizeWordDistribution(f_data, f_wordDistribution)  # Function Call
    visualizePostNumberTrend(f_data, f_postTrend)  # Function Call

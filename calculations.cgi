#!/usr/local/bin/python3
print("Content-Type: text/html\n\n")
print("")
import cgi
import cgitb
cgitb.enable()


import math
import re
import os
import io
import sys
import base64
# os.environ['HOME'] = r'#!/usr/local/bin/python3'
import matplotlib.pyplot as plt



"""
 Gets number of rows in the file, and prepares form for input
"""


form = cgi.FieldStorage()


fileName = form.getvalue('fileName') # Get number from user as GET variable

saveObject = io.BytesIO()  # Create buffer to save figure

#Define a gene array for input for each severity score
target_severity1 = []
target_severity2 = []
target_severity3 = []
target_severity4 = []
#Define a control array for input
control_severity1 = []
control_severity2 = []
control_severity3 = []
control_severity4 = []
# Arrays to store normalized values after simpleNormalizer funtion..
normalized_severity1 = []
normalized_severity2 = []
normalized_severity3 = []
normalized_severity4 = []


# File input is done through form
my_file = open(fileName+'.txt')

def organizeArrays():
    global target_severity1,target_severity2,target_severity3,target_severity3,target_severity4,control_severity1,control_severity2,control_severity3
    global control_severity4
    for line in my_file:
        my_column = line.split('\t')
        if re.search(r'1',my_column[2]):
            target_severity1.append(my_column[0])
            control_severity1.append(my_column[1])
        if re.search(r'2',my_column[2]):
            target_severity2.append(my_column[0])
            control_severity2.append(my_column[1])
        if re.search(r'3',my_column[2]):
            target_severity3.append(my_column[0])
            control_severity3.append(my_column[1])
        if re.search(r'4',my_column[2]):
            target_severity4.append(my_column[0])
            control_severity4.append(my_column[1])


# a simpler normalizer that neglects control group...
# It would take a value from gene input as target,
# internal control input as control
# and add this value to the expression array..
# This is a basic delta ct normalization method for PCR based on ct values..

def simpleNormalizer(target,control,my_expression_array):
    mydelta = int(target)-int(control)
    my_expression = math.pow(2,-mydelta)
    my_expression_array.append(my_expression)

# a simple boxplot function
# It would take the values from normalized gene arrays and show a boxplot
# based on the severityScores...

def plotData(sample1, sample2, sample3, sample4):
    global saveObject  # Buffer object
    data_to_plot = [sample1, sample2, sample3, sample4]
    # Create a figure instance
    plt.boxplot(data_to_plot, patch_artist=True,
                labels=['severity1', 'severity2', 'severity3', 'severity4'])
    plt.title('Correlation results of Gene Based on Severity Score:')
    plt.ylabel('Expression')

    plt.savefig('image.png',format='png')  # Save figure in buffer



# Mean Expression method.. This method calculates the mean value of each
# normalized expression array..
def meanExpression(sample):
    # IF sample is empty avoid division by 0
    if sample==[]:
        return 0
    my_sum = 0
    for i in range(1,len(sample)):
        my_sum = my_sum + sample[i]
    my_mean_expression = my_sum/len(sample)
    return my_mean_expression

#MAIN function
#It normalizes all of the arrays...
def normalizeAll():
    for i in range(1,len(target_severity1)):
        simpleNormalizer(target_severity1[i],control_severity1[i],
        normalized_severity1)
    for i in range(1,len(target_severity2)):
        simpleNormalizer(target_severity2[i],control_severity2[i],
        normalized_severity2)
    for i in range(1,len(target_severity3)):
        simpleNormalizer(target_severity3[i],control_severity3[i],
        normalized_severity3)
    for i in range(1,len(target_severity4)):
        simpleNormalizer(target_severity4[i],control_severity4[i],
        normalized_severity4)

# Now the program is ready to run...

# Step 1 -> Organize arrays based on our input file...
organizeArrays()
my_file.close() # Close file when done reading
# Step 2 -> Normalize these arrays...
normalizeAll()

# Step 4 -> Boxplot output..
plotData(normalized_severity1,normalized_severity2,normalized_severity3,normalized_severity4)

print('<html><body>')
print('<h1>Calculations</h1>')

# Step 3 -> Print mean values for each Severity Score as a command line output.
print("<p>Mean R Value for Severity Score 1 is: " +
str(meanExpression(normalized_severity1))+'</p>')
print("<p>Mean R Value for Severity Score 2 is: " +
str(meanExpression(normalized_severity2))+'</p>')
print("<p>Mean R Value for Severity Score 3 is: " +
str(meanExpression(normalized_severity3))+'</p>')
print("<p>Mean R Value for Severity Score 4 is: " +
str(meanExpression(normalized_severity4))+'</p>')

data = base64.b64encode(open('image.png', 'rb').read()).decode('utf-8')
img = '<img defer src="data:image/png;base64,{0}">'.format(data)
print(img)

print('</body></html>')

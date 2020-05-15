#!/usr/local/bin/python3

import cgi
import cgitb
cgitb.enable()

"""
 Gets number of rows in the file, and prepares form for input
"""

form = cgi.FieldStorage()

number = form.getvalue('number') # Get number from user as GET variable

print('Content-type: text/html\r\n\r')
print('<html>')
print('<h1>Enter ct values for target and control gene on the first two columns and severity score on the third column..</h1>')
print('<form action="create.cgi" method="get">')
print('<input hidden type="number" name="number" value="%d">  <br />'%(int(number)))
# Also pass the number as well
for i in range(int(number)):
    # Create a single input row with names that use number index and columns
    print('Sample',i,': <input type="number" name="%s"> '
                '<input type="number" name="%s"> '
                '<input type="number" min=1 max=4 step="1" name="%s">  <br />'%('F'+str(i),'H'+str(i),'S'+str(i)))

print('<input type="submit" value="Submit" />')
print('</form>')

print('</html>')

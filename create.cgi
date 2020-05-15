#!/usr/local/bin/python3
import cgi
import cgitb
cgitb.enable()



"""
 Script gets all data inputs, and creates file so that main reads it
"""
fileName='fileData'  # This is the file name that this script will create and
                     # fill up , and calculations.cgi will use to calculate
my_file =open(fileName+'.txt','w') # Open file to write
my_file.write('FAM\tHEX\tSeverityScore\n')    # Write heading


form = cgi.FieldStorage()
number =form.getvalue('number') # Hidden field from number (set in index)

# Per each row input by user
for i in range(int(number)):
    row=form.getvalue('F'+str(i)),form.getvalue('H'+str(i)), form.getvalue('S'+str(i))
    row='\t'.join(row)      # Join all columns values with tabs
    my_file.write(row+'\n') # Write to file with newline

my_file.close() # Close object


print("Content-Type: text/html\n")
print("")
print('File created...')
# Form here
print('<form action="calculations.cgi" method="get">')
print('<input type="hidden" name="fileName" value="%s">  <br />' % fileName)
 # Pass filename as hidden field value
print('<input type="submit" value="Submit" />')
print('</form>')

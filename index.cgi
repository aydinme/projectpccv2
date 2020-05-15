#!/usr/local/bin/python3


import cgi
import cgitb
cgitb.enable()

print('Content-type: text/html\n\n')
print('<html>')
print('<h1>This is a correlation checker program <br> Enter how many samples you want to show</h1>')
print('<form action="number.cgi" method="get">')
print('Sample Size: <input type="number" name="number">  <br />')
print('<input type="submit" value="Submit" />')
print('</form>')
print('</html>')

#!/usr/bin/python
import cgi


print ("Content-type: text/html\r\n\r\n")
print()
print ("Set-Cookie:sess=false")
print ("Location:index.py")
print ("<script>location.href='index.py';</script>")
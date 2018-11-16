import cgi

print("Content-Type: text/html")
url_input = cgi.FieldStorage()
print("""
<html>
<head>
    <title>Título de la página</title>
</head>
<h3>Hola %s!</h3>
</html>""" % url_input["nombre"].value)
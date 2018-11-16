import cgi
# Headers
print("Content-Type: text/html")
print()

print("""<html>
<head>
    <title>Título de la página</title>
</head>
<h3>Hola CGI!</h3>
</html>""")

url_input = cgi.FieldStorage()
# Se trata como cualquier diccionario
url_input["nombre"].value  # 'Pedro'
url_input["edad"].value    # '25'
url_input["idioma"].value  # 'Ingles'
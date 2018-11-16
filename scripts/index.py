import cgi
import os
import Cookie
import md5



lista_usuarios = ["admin", "JaAViEr"] #Usuarios
lista_passwords = ["root", "toor"] # Contrase&#241;as
method = os.environ.get("REQUEST_METHOD")
logueado = False
contenido_cookies = os.environ.get('HTTP_COOKIE')
 
tag_head = """<meta charset="UTF-8">\n<link rel="stylesheet" type="text/css" href="/topcoat/css/topcoat-mobile-dark.min.css" class="uib-framework-theme">\n<link rel="stylesheet" type="text/css" href="/css/index_main.less.css" class="main-less">\n<meta http-equiv="Content-type" content="text/html; charset=utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=0">\n<style type="text/css">\n\t/* Prevent copy paste for all elements except text fields */\n\t*  { -webkit-user-select:none; -webkit-tap-highlight-color:rgba(255, 255, 255, 0); }\n\tinput, textarea  { -webkit-user-select"""
 
def code_login(accion=False):
 
	if accion == 'error':
 
		mensaje_error = """
		  <div class="topcoat-navigation-bar widget uib_w_1 d-margins" data-uib="topcoat/nav" data-ver="0">
			<div class="topcoat-navigation-bar__item center full">
				<h1 class="topcoat-navigation-bar__title">Verifica tus credenciales por favor[/size][/center]
			</div>
		  </div>
		"""
 
	else:
 
		mensaje_error = ''
 
	return """
<!DOCTYPE html>
<html>
 
  <head>
	""" + tag_head + """
	<title>Indetif&#237;cate en el sistema</title>
  </head>
 
  <body>
    <div class="uwrap">
      <div class="upage" id="mainpage">
        <div class="upage-outer">
          <div class="upage-content" id="mainsub">
 
            <div class="grid grid-pad urow uib_row_2 row-height-2" data-uib="layout/row" data-ver="0">
              <div class="col uib_col_2 col-0_12-12" data-uib="layout/col" data-ver="0">
                <div class="widget-container content-area vertical-col">
 
                  <div class="topcoat-navigation-bar widget uib_w_1 d-margins" data-uib="topcoat/nav" data-ver="0">
                    <div class="topcoat-navigation-bar__item center full">
                      <h1 class="topcoat-navigation-bar__title">Indentif&#237;cate[/size][/center]
                    </div>
                  </div>
                  <span class="uib_shim"></span>
                </div>
              </div>
              <span class="uib_shim"></span>
            </div>
 
            <div class="grid grid-pad urow uib_row_3 row-height-3" data-uib="layout/row" data-ver="0">
 
				<form action="" method="POST">
					<div class="col uib_col_3 col-0_12-12" data-uib="layout/col" data-ver="0">
					<div class="widget-container content-area vertical-col">
					<div class="table-thing widget uib_w_2 d-margins" data-uib="topcoat/input" data-ver="0">
					<label class="narrow-control label-top-left">Usuario</label>
					<input class="wide-control topcoat-text-input" type="text" placeholder="Usuario" name="usuario">
					</div>
					<div class="table-thing widget d-margins" data-uib="topcoat/input" data-ver="0">
					<label class="narrow-control label-top-left">Contrase&#241;a</label>
					<input class="wide-control topcoat-text-input" type="password" placeholder="Contrase&#241;a" name="password">
					</div>
					<button class="widget d-margins topcoat-button--cta" data-uib="topcoat/button" data-ver="0">Ingresar</button><span class="uib_shim"></span>
					</div>
					""" +mensaje_error+ """
				</form>
              </div>
              <span class="uib_shim"></span>
            </div>
          </div>
          <!-- /upage-content -->
 
        </div>
        <!-- /upage-outer -->
 
      </div>
      <!-- /upage -->
 
    </div>
    <!-- /uwrap -->
  </body>
 
</html>"""
 
code = """<!DOCTYPE html>
<!--HTML5 doctype-->
<html>
 
	<head>
	""" + tag_head + """
		<title>Control Remoto :: 2014</title>
	</head>
 
	<body>
		<!-- content goes here-->
		<div class="uwrap">
			<div class="upage" id="mainpage">
				<div class="upage-outer">
					<div class="upage-content" id="mainsub">
 
						<div class="grid grid-pad urow uib_row_1 row-height-1" data-uib="layout/row" data-ver="0">
							<div class="col uib_col_2 col-0_12-12" data-uib="layout/col" data-ver="0">
								<div class="widget-container content-area vertical-col">
 
									<div class="topcoat-navigation-bar widget uib_w_2 d-margins" data-uib="/topcoat/nav" data-ver="0">
										<div class="topcoat-navigation-bar__item center full">
											<h1 class="topcoat-navigation-bar__title">Panel de Control Remoto[/size][/center]
										</div>
									</div>
									<button class="widget uib_w_4 d-margins topcoat-button--large--cta" data-uib="/topcoat/button" data-ver="0">Consola - Terminal</button>
									<button class="widget uib_w_3 d-margins topcoat-button--large--cta" data-uib="/topcoat/button" data-ver="0">Enviar comando r&#225;pido</button>
									<button class="widget uib_w_5 d-margins topcoat-button--large" onclick='location.href="logout.py"' data-uib="/topcoat/button" data-ver="0">Salir</button>
									<span class="uib_shim"></span>
								</div>
							</div>
							<span class="uib_shim"></span>
						</div>
 
					</div>
					<!-- /upage-content -->
 
				</div>
				<!-- /upage-outer -->
 
			</div>
			<div class="upage hidden" id="uib_page_3">
				<div class="upage-outer">
					<div id="uib_page_3sub" class="upage-content ">
					</div>
				</div>
				<!-- /upage-outer -->
te			</div>
			<div class="upage hidden" id="uib_page_2">
				<div class="upage-outer">
					<div id="uib_page_2sub" class="upage-content ">
					</div>
				</div>
				<!-- /upage-outer -->
			</div>
			<div class="upage hidden" id="uib_page_1">
				<div class="upage-outer">
					<div id="uib_page_1sub" class="upage-content ">
					</div>
				</div>
				<!-- /upage-outer -->
			</div>
 
			<!-- /upage -->
 
		</div>
		<!-- /uwrap -->
	</body>
 
</html>"""
 
def verificar_login(u, p):
 
	if u in lista_usuarios and p in lista_passwords:
 
		session = u + p
		session = md5.md5(session).hexdigest()
		return True
 
	else:
 
		return False
 
if contenido_cookies: #Si hay cookies...
 
	valores_cookie = Cookie.SimpleCookie(contenido_cookies)
	session_actual = valores_cookie['sess'].value # session_actual = cookie "sess"
 
	if session_actual == "false": # No logueado
 
		logueado = False
 
	else: # Verifica login
 
		for a, b in zip(lista_usuarios, lista_passwords):
 
			session_temporal = a + b
			session_temporal = md5.md5(session_temporal).hexdigest()
 
			if session_actual == session_temporal:
 
				logueado = True # Login coincide
				break
 
			else:
 
				pass
 
else: #No logueado, sess = false
 	print("Content-Type: text/html")
	print("Set-Cookie:sess=false")
 
print("Content-Type: text/html")
 
if method == "POST":
 
	form = cgi.FieldStorage()
	usuario = form.getvalue('usuario')
	password = form.getvalue('password')
 
	if verificar_login(usuario, password):
 
		session = usuario + password
		session = md5.md5(session).hexdigest()
		print("Set-Cookie:sess=%s" % session)
		print()
		print (code)
 
	else:
 
		print()
		print (code_login('error'))
 
elif method == "GET":
 
	if not logueado:
 
		print (code_login())
 
	else:
 
		print (code)
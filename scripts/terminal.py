import cgi
import os
import Cookie
import md5
 
print "Content-Type: text/html"
print
 
code_terminal = '''
<!DOCTYPE html>
<html>
 
  <head>
    <link rel="stylesheet" type="text/css" href="/topcoat/css/topcoat-mobile-dark.min.css" class="uib-framework-theme">
    <link rel="stylesheet" type="text/css" href="/css/terminal_main.less.css" class="main-less">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=0">
	<title>Terminal</title>
    <script src="/js/jquery.min.js"></script>
  </head>
 
  <body>
    <div class="uwrap">
      <div class="upage" id="mainpage">
        <div class="upage-outer">
          <div class="upage-content" id="mainsub">
 
            <div class="grid grid-pad urow uib_row_1 row-height-1" data-uib="layout/row" data-ver="0">
              <div class="col uib_col_1 col-0_12-12" data-uib="layout/col" data-ver="0">
                <div class="widget-container content-area vertical-col">
 
                  <div class="topcoat-navigation-bar widget uib_w_1 d-margins" data-uib="/topcoat/nav" data-ver="0">
                    <div class="topcoat-navigation-bar__item center full">
                      <h1 class="topcoat-navigation-bar__title">Consola - Terminal[/size][/center]
                    </div>
                  </div>
                  <div class="table-thing widget uib_w_2 d-margins" data-uib="/topcoat/textarea" data-ver="0">
                    <label class="narrow-control label-inline"></label>
                    <textarea class="wide-control topcoat-textarea" type="text" placeholder="Comandos" name="comando"></textarea>
                  </div>
					<button class="widget uib_w_2 d-margins topcoat-button--cta" data-uib="topcoat/button" data-ver="0" onclick='execute();'>&#161;Ejecutar!</button>
					<button class="widget uib_w_2 d-margins topcoat-button" data-uib="topcoat/button" data-ver="0" onclick='location.href="index.py"'>Volver</button>
					<hr>
					Salida:
					<span id="loader"></span>
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
      <!-- /upage -->
 
    </div>
    <!-- /uwrap -->
	<script language="javascript">
 
	function execute(){
 
		comando = $("textarea[name=comando]").val();
		$("#loader").load("terminal.py", {"comando":comando});
 
	}
	</script>
  </body>
 
</html>'''
 
logueado = False
lista_usuarios = ["admin", "JaAViEr"] #Usuarios
lista_passwords = ["root", "toor"] # Contrase&#241;as
method = os.environ['REQUEST_METHOD']
lectura_cookies = os.environ.get('HTTP_COOKIE')
 
if lectura_cookies:
 
	valores_cookie = Cookie.SimpleCookie(lectura_cookies)
	session_actual = valores_cookie['sess'].value # session_actual = cookie "sess"
 
	if session_actual != "false":
 
		for a, b in zip(lista_usuarios, lista_passwords):
 
			session_temporal = a + b
			session_temporal = md5.md5(session_temporal).hexdigest()
 
			if session_actual == session_temporal:
 
				logueado = True # Login coincide
				break
 
			else:
 
				pass
	else:
 
		pass
 
	if logueado:
		if method == "GET":
 
			print code_terminal
 
		elif method == "POST":
 
			form = cgi.FieldStorage()
			comando = form.getvalue("comando")
			lineas = comando.split("\n")
			print '''
			<span  style="font-family:Trebuchet Ms; color: #fff;" class="wide-control">
			<br />
		'''
			for l in lineas:
 
				try:
 
					run = os.popen(l, "r")
					run_content = run.read()
					run_content = run_content.replace("\n", "<br>")
					run_content = run_content.replace(" ", "&nbsp;")
					print run_content
					run.close()
 
				except:
 
					print "Error al ejecutar comando %s" % (l)
 
			print "</span>"
	else:
		print "<script>location.href='index.py';</script>"
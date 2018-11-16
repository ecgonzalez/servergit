import cgi
import os
import subprocess
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
	<title>Comandos r&#225;pidos</title>
    <script src="/js/jquery.min.js"></script>
  </head>
 
  <body>
    <div class="uwrap">
      <div class="upage" id="mainpage">
        <div class="upage-outer">
          <div class="upage-content" id="mainsub">
 
            <div class="grid grid-pad urow uib_row_3 row-height-3" data-uib="layout/row" data-ver="0">
              <div class="col uib_col_3 col-0_12-12" data-uib="layout/col" data-ver="0">
                <div class="widget-container content-area vertical-col">
 
                  <div class="topcoat-navigation-bar widget uib_w_1 d-margins" data-uib="topcoat/nav" data-ver="0">
                    <div class="topcoat-navigation-bar__item center full">
                      <h1 class="topcoat-navigation-bar__title">Comandos r&#225;pidos[/size][/center]
                    </div>
                  </div>
                  <span class="uib_shim"></span>
                </div>
              </div>
              <span class="uib_shim"></span>
            </div>
 
            <div class="grid grid-pad urow uib_row_4 row-height-4" data-uib="layout/row" data-ver="0">
              <div class="col uib_col_4 col-0_12-12" data-uib="layout/col" data-ver="0">
                <div class="widget-container content-area vertical-col">
 
					<button class="widget uib_w_2 d-margins topcoat-button--cta" data-uib="topcoat/button" data-ver="0" onclick="comando('apagar'); return false;">Apagar</button>
					<button class="widget uib_w_3 d-margins topcoat-button--cta" data-uib="topcoat/button" data-ver="0" onclick="comando('reiniciar'); return false;">Reiniciar</button>
					<button class="widget uib_w_4 d-margins topcoat-button--cta" data-uib="topcoat/button" data-ver="0" onclick="comando('cancelar salida'); return false;">Cancelar Apagado/Rein.</button>
					<button class="widget uib_w_5 d-margins topcoat-button--cta" data-uib="topcoat/button" data-ver="0" onclick="matar_proceso('mostrar'); return false;">Matar proceso</button>
					<span id="matar_proceso" style="display:none">
						<hr>
						<input class="wide-control topcoat-text-input" type="text" placeholder="proceso.ext" name="proceso">
						<button class="widget uib_w_6 d-margins topcoat-button wide-control" data-uib="topcoat/button" data-ver="0" onclick="matar_proceso('kill'); return false;">&#161;Matar ahora!</button>
						<hr>
					</span>
					<button class="widget uib_w_6 d-margins topcoat-button--cta" data-uib="topcoat/button" data-ver="0" onclick="iniciar_proceso('mostrar'); return false;">Iniciar proceso</button>
					<span id="iniciar_proceso" style="display:none">
						<hr>
						<input class="wide-control topcoat-text-input" type="text" placeholder="proceso.ext" name="iniciar_proceso">
						<button class="widget uib_w_6 d-margins topcoat-button wide-control" data-uib="topcoat/button" data-ver="0" onclick="iniciar_proceso('iniciar'); return false;">&#161;Iniciar ahora!</button>
						<hr>
					</span>
					<button class="widget uib_w_2 d-margins topcoat-button" data-uib="topcoat/button" data-ver="0" onclick='location.href="index.py"'>Volver</button>
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
  </body>
  <span id="loader" style="display:none;"></span>
  <script language="javascript">
 
  function comando(cmd){
 
	$("#loader").load("comando_rapido.py", {"comando":cmd});
 
  }
  function matar_proceso(param){
 
	if(param == 'mostrar'){
		$("#matar_proceso").fadeIn();
		$("#iniciar_proceso").fadeOut();
	}else if(param == 'kill'){
		proceso = $("input[name=proceso]").val();
		$("#loader").load("comando_rapido.py", {"kill": proceso});
		$("#matar_proceso").fadeOut();
		$("input[name=proceso]").val("");
	}
  }
 
  function iniciar_proceso(accion){
 
  if (accion == "mostrar"){
 
	$("#matar_proceso").fadeOut();
	$("#iniciar_proceso").fadeIn();
 
  }else if(accion == "iniciar"){
 
 
	nuevo_proceso = $("input[name=iniciar_proceso]").val();
	$("#loader").load("comando_rapido.py", {"correr": nuevo_proceso});
	$("#iniciar_proceso").fadeOut();
	$("input[name=iniciar_procesoproceso]").val("");
 
  }
 
  }
  </script>
 
 
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
		if os.name == "nt":
 
			so = "windows"
 
		else:
 
			so = "unix"
 
		if method == "GET":
 
			print code_terminal
 
		elif method == "POST":
 
			form = cgi.FieldStorage()
			comando = form.getvalue("comando")
			kill = form.getvalue("kill")
			correr = form.getvalue("correr")
			iniciar_proceso = ""
			matador = ""
 
			try:
 
				if correr:
 
					if so == "windows":
 
						iniciar_proceso = "start %s" % (correr)
 
					elif so == "unix":
 
						iniciar_proceso = "%s" % (correr)
 
					subprocess.call(iniciar_proceso)
 
				if kill:
 
					if so == "windows":
 
						matador = "taskkill /F /IM %s" % (kill)
 
					elif so == "unix":
 
						matador = "pkill -9 %s" % (kill)
 
					kill = subprocess.call(matador)
					kill.close()
 
				if comando == "apagar":
 
					if so == "windows":
 
						accion = "shutdown /S /T 60"
 
					elif so == "unix":
 
						accion = "sudo poweroff"
 
 
				elif comando == "reiniciar":
 
					if so == "windows":
 
						accion = "shutdown /R /T 60"
 
					elif so == "unix":
 
						accion = "sudo reboot"
 
					#accion = ""
 
				elif comando == "cancelar salida":
 
					if so == "windows":
 
						accion = "shutdown /A"
 
					elif so == "unix":
 
						accion = ""
 
					#accion = ""
 
 
				action = subprocess.call(accion)
				action.close()
			except:
 
				pass
 
	else:
		print "<script>location.href='index.py';</script>"
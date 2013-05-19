<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Search Result</title>
    <link rel="stylesheet" type="text/css" href="style/style.css" /> 
  </head>
  <body>
    <div id="container">
		<div id="header"></div>
    <h3>Resultado de la busqueda</h3>      
    <p> 
     %for i in goods:
	<p>{{i}}<img src="{{i}}"</p>
	 %end
    </p>
   </div>
  </body>
</html>


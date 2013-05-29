<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Groupones</title>
    <link rel="stylesheet" type="text/css" href="style/style.css" /> 
  </head>
  <body>
    <div id="container">
		<div id="header"></div>
    <h3>Search Result</h3>      
    <p> 
    <div id="cuerpo">
     %cont = 1
     %for i in goods:
	 %if cont%5 == 0:
	         <p><img src="{{i}}"></p>
	     %elif cont%10 == 1:
			<h9><p>{{i}}</p></h9>
	     %else: 
			<p>{{i}}</p>
	     %end
	     %cont = cont + 1
	 %end
     </div>
    </p>
   </div>
  </body>
</html>


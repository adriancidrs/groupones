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
	  %for i in occasions:
	  <p><img src="{{i}}"></p>
	  <p>{{i}}</p>
	  %end
	  </div>
	</p>
      </div>
      <a href="/">Return homepage</a> 
    </body>
 </html>
    
    

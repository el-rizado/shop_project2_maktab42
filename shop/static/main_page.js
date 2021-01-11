function httpGet(theUrl)
	{
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
	xmlHttp.send( null );
	return xmlHttp.responseText;
	}

function myFunction(elmnt) {
  kala = elmnt._id
  httpGet("/api/product?id=" + kala.$oid)
}



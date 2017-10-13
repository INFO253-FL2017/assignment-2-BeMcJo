
var postDiv = document.getElementById("posts");

var postForm = document.getElementById("postForm");
//localStorage.curLocation = "";
postForm.addEventListener("submit", function(event) {
	var name = document.getElementById("name").value;
	var message = document.getElementById("message").value;
	var postDiv = document.getElementById("posts");
	var len = localStorage.length

	var p = document.createElement("h3");
	postDiv.appendChild(p);
	p.innerHTML += "Name:" + name;
	localStorage.curLocation += p.innerHTML;
	p = document.createElement("h4");
	postDiv.appendChild(p);
	p.innerHTML += "Comment:" + message;
	localStorage.curLocation += p.innerHTML;
	p.append(document.createElement("br"));
	p.innerHTML += "===============================";
	event.preventDefault();
})
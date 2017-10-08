
var notifDiv = document.getElementById("notification");

var contactForm = document.getElementById("contactForm");
contactForm.addEventListener("submit", function(event) {
	var name = document.getElementById("name").value;
	var subject = document.getElementById("subject").value;
	var message = document.getElementById("message").value;
	var notifDiv = document.getElementById("notification");
	while(notifDiv.hasChildNodes())
		notifDiv.removeChild(notifDiv.lastChild);
	var p = document.createElement("p");
	notifDiv.appendChild(p);
	if (!name)
		p.innerHTML += "Please fill ind your name";
	if (!subject){
		if(p.innerHTML)
			p.appendChild(document.createElement("br"));
		p.innerHTML +="Please fill in the subject";
	}
	if (!message){
		if(p.innerHTML)
			p.appendChild(document.createElement("br"));
		p.innerHTML +="Please enter your message";
	}
	if (name && subject && message){
	
		p.innerHTML += "Hi " + name + ", your message has been sent";
		
	} else{
		event.preventDefault();
	}
})
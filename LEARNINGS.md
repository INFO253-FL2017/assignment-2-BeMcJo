1) 
	i) HTML - Displays the content to the client's browser like text, images, and links.
	
	ii) CSS - Beautifies/decorates the content on the client's browser like change font size or color.

	iii) Javascript - Handles backend aspect of the web page. Used to do calculations and other computations to determine what will happen on the webpage. In this assignment, javascript is used to check if the client input their name, subject, and message to send in the contact page. If they fail to fill in any of them, they get a warning to fill in the missing input. Else they successfully send.

	iv) Python - Used to handle the server requests POST and GET. Used to make webserver.py

	v) Flask - Framework used in python to handle server requests. Used in webserver.py

	vi) HTTP - Used to format and transmit messages and handle actions the web servers and browsers should take.

	vii) GET requests data from the server. So in this assignment, we use GET to obtain the html files of links we want to traverse to (ie. The blogs, contact, about, index). POST requests in this assignment was used to send a message in the contact page. When successfully filling in the name, subject, and message inputs, the client can then send a POST request to send this set of data to the contact's email address.

2) HTML, CSS, and Javascript works together by the following:
	i) HTML displays the contents. So whatever you see on your browser is from the HTML file. 

	ii) CSS makes decorating the contents on the webpage easy. It takes any of the information in between a markup segment and modifies the font, size, color, etc... This will then be visually displayed on the browser. So in the assignment, the about web page has some variations to how CSS affected the content. It has changes in text color, size, and background color.

	iii) Javascript handles any computational aspects of the webpage. As mentioned, it handles ensuring that the client fills in the name, subject, and message before being able to send it in the contact page.

3) Python uses the Flask framework. Flask enables running the server. Python enables us to program the handlers for each request from the server.

4) 
	- "GET /index HTTP/1.1" 200 : This is a successful GET request that fetches the index.html file for the client when the route is "index"

	- "GET /blog/8-experiments-in-motivation HTTP/1.1" 200 : Successful GET request that fetches blog1.html.

	- "GET /blog/a-mindful-shift-of-focus HTTP/1.1" 200 : Successful GET request that fetches blog2.html.

	- "GET /blog/how-to-develop-an-awesome-sense-of-direction HTTP/1.1" 200 : Successful GET request that fetches blog3.html.

	- "GET /blog/training-to-be-a-good-writer HTTP/1.1" 200 : Successful GET request that fetches blog4.html.

	- "GET /blog/what-productivity-systems-wont-solve HTTP/1.1" 200 : Successful GET request that fetches blog5.html.

	- "GET /contact HTTP/1.1" 200 : Successful GET request that fetches contact.html.

	- "POST /contact HTTP/1.1" 200 : Successful POST request that sends an email.

	- "GET /about HTTP/1.1" 200 : Successful GET request that fetches about.html
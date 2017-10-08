"""
webserver.py

File that is the central location of code for your webserver.
"""
import requests
import os
from flask import Flask, request, render_template

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/index', methods=['GET'])
def home_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/about', methods=['GET'])
def about_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("about.html") # Render the template located in "templates/index.html"

@app.route('/contact', methods=['GET'])
def contact_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("contact.html") # Render the template located in "templates/index.html"

@app.route('/blog/8-experiments-in-motivation', methods=['GET'])
def blog1_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("blog1.html") # Render the template located in "templates/index.html"

@app.route('/blog/a-mindful-shift-of-focus', methods=['GET'])
def blog2_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("blog2.html") # Render the template located in "templates/index.html"

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction', methods=['GET'])
def blog3_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("blog3.html") # Render the template located in "templates/index.html"

@app.route('/blog/training-to-be-a-good-writer', methods=['GET'])
def blog4_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("blog4.html") # Render the template located in "templates/index.html"

@app.route('/blog/what-productivity-systems-wont-solve', methods=['GET'])
def blog5_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("blog5.html") # Render the template located in "templates/index.html"

@app.route('/contact', methods=['POST'])
def send_email():
  name = request.form['name']
  subject = request.form['subject']
  message = request.form['message']

  key = os.environ["INFO253_MAILGUN_PASSWORD"]
  #print (key)
  sandbox = os.environ["INFO253_MAILGUN_DOMAIN"]
  #print (sandbox)
  recipient = os.environ["INFO253_MAILGUN_TO_EMAIL"]
  #print(recipient)
  
  request_url = 'https://api.mailgun.net/v2/{}/messages'.format(sandbox)
  api = os.environ["INFO253_MAILGUN_USER"]
  #print (api)
  #print (os.environ["INFO253_MAILGUN_FROM_EMAIL"])
  r = requests.post(request_url, auth=(api, key), data={
      'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
      'to': recipient,
      'subject': subject,
      'text': message
  })

  if r.status_code == requests.codes.ok:
    if name and message and subject:
      s = render_template("contact.html")
      i = s.find("</div>")
      rtn = ""
      for a in range(0,i):
        rtn += s[a]
      rtn += "Hi " + name + ", your message has been semt"
      for a in range(i,len(s)):
        rtn += s[a]
      return rtn

  return render_template("contact.html")
from flask import Flask, render_template, request  #NEW IMPORT -- request
from forms import ContactForm 					# NEW IMPORT LINE
from flask.ext.mail import Message, Mail

mail = Mail()
app = Flask(__name__)    #This is creating a new Flask object

app.secret_key = 'WebDesign'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'greetland1023@gmail.com'
app.config["MAIL_PASSWORD"] = 'x19921023'

mail.init_app(app)

@app.route('/')
def default():
    return render_template("index.html", name = "index", title = "Tiny Planet")

@app.route('/index')
def home():
    return render_template("index.html", name = "index", title = "Tiny Planet")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    msg = Message(form.subject.data, sender='umsiwebdesign@gmail.com', recipients=['dxi@umich.edu'])
    msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
    mail.send(msg)

    msg = Message('Thank you for your message', sender='umsiwebdesign@gmail.com', recipients=[form.email.data])
    msg.body = """
      Thank you for your message. I'll get back to you asap.
      --------------------
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
    mail.send(msg)

    return render_template('contact.html', form=ContactForm(formdata=None, message="information is sent"), success=True, title="CONTACT PAGE")

  elif request.method == 'GET':
    return render_template('contact.html', form=form, name = "contact", title = "Tiny Planet")

if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional

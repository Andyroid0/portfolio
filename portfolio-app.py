#! python3

from flask import Flask, render_template, url_for, request, flash
from forms import SendEmailForm
from portfolio_dicts import Characters_cards, Creatures_cards, Sketchbook_cards, Environment_cards, Motion_cards, Props_cards, Animation_cards, General_cards
import smtplib
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail()
app.config['SECRET_KEY'] = 'l0627ca8e16cd42ue0535a5f0e41c8cc53db57c1f896h011ec9955c240c4ecb85nd09'
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'andyvalley@live.com'
app.config['MAIL_PASSWORD'] = 'Warlock23!'
app.config['MAIL_ASCII_ATTACHMENTS'] = True

mail.init_app(app)




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', cards=General_cards,)



@app.route("/creatures")
def creature_port():
    form = SendEmailForm()
    return render_template('creature_port.html', title="Creatures", cards=Creatures_cards)



@app.route("/characters")
def character_port():
    form = SendEmailForm()
    return render_template('character_port.html', title="Characters", cards=Characters_cards)



@app.route("/sketchbook")
def sketchbook_port():
    form = SendEmailForm()
    return render_template('sketchbook_port.html', title="SketchBook", cards=Sketchbook_cards)



@app.route("/props")
def prop_port():
    form = SendEmailForm()
    return render_template('prop_port.html', title="Prop-Design", cards=Props_cards)



@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = SendEmailForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('UH OH! Check that all fields are filled and Email Addresses matches!', 'alert alert-danger container')
            return render_template('contact.html', title="Contact", form=form)
        else:
            msg = Message('Website=Portfolio Correspondence', sender='andyvalley@live.com', recipients=['andrewpvalley@gmail.com'])
            messagers_email = str(form.email.data) 
            messagers_message = str(form.textBody.data)
            msg.html = render_template('email-layout.html',messagers_email=messagers_email, messagers_message=messagers_message)
               

            
            mail.send(msg)
            flash('Email Sent!', 'alert alert-success container')
            return render_template('contact.html', title="Contact", form=form)
    
    elif request.method == 'GET':
        return render_template('contact.html', title="Contact", form=form)









if __name__ == '__main__':
    app.run(debug=False)
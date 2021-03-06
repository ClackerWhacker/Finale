from application import application, mail
from flask import render_template, url_for, request,redirect, flash
from flask_mail import Message
from application.forms import EmailClass
from application.decorators import asynchronous

@asynchronous
def send_async_email(application, msg):

    with application.app_context():
        mail.send(msg)
 
@application.route("/contact", methods=["GET", "POST"])
def contact():
    
    form = EmailClass()

    if form.validate_on_submit():

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["number"]
        text_body = request.form["msg"]

        msg = Message(subject="Lesson", sender="LearnHackTutoring@gmail.com", recipients=["LearnHackTutoring@gmail.com"])
        msg.body = text_body + phone + email + name

        send_async_email(application, msg)

        flash("The email was recieved! We will respond ASAP!")

        return render_template("index.html")
    return render_template("contact.html", form=form)   

@application.route("/<user>", methods=["GET"])
def user(user):

    return render_template("user.html", user=user)   

@application.route("/faq", methods=["GET"])
def questions():

    return render_template("question.html")   
  
@application.route("/becomeAHacker", methods=["GET"])
def becomeAHacker():

    return render_template("becomeAHacker.html")   

@application.route("/hackers", methods=["GET"])
def hackers():

    return render_template("hackers.html") 

@application.route("/", methods=["GET"])
@application.route("/home", methods=["GET"])
def homeHype():

    return render_template("index.html") 

@application.errorhandler(404)
def fileNotFound(e):

    return (render_template("404.html"), 404)

@application.errorhandler(404)
def serverError(e):
    
    return (render_template("505.html"), 505)
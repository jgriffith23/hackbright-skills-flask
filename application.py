from flask import Flask, render_template, flash, request, redirect
from flask_debugtoolbar import DebugToolbarExtension

import jinja2


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined


#  to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Shows an index page."""

    return render_template("index.html")

@app.route("/application-form")
def application_page():
    """Shows the page containing the job application."""
    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def submit_application():
    """Handles submitting the job application form."""

    print "\n############################"
    print "The raw form: "
    print request.form
    print "############################\n"

    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    desired_position = request.form["position"]
    salary_requirement = request.form["salaryreq"]

    print "###########################"
    print "First Name:", first_name
    print "Last Name: ", last_name
    print "Position: ", desired_position
    print "Desired Salary:", salary_requirement
    print "###########################\n"

    flash("Your application has been submitted! Don't refresh the page.")

    return render_template("application-response.html",
                           first=first_name,
                           last=last_name,
                           position=desired_position,
                           salary_req=salary_requirement)




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

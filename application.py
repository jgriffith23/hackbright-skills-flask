from flask import Flask, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension

import jinja2
import jobs


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined


#  to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Shows an index page containing descriptions of all active job
    postings."""

    job_info_for_jinja = jobs.get_job_info_in_lists()

    return render_template("index.html", joblist=job_info_for_jinja)

@app.route("/application-form")
def application_page():
    """Shows the page containing the job application."""
    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def submit_application():
    """Handles submitting the job application form."""

    # Get all of the user's information from the form.
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    desired_position = request.form["position"]
    salary_requirement = int(request.form["salaryreq"])

    # Prettify the salary with commas.
    prettified_salary_req = "{:,}".format(salary_requirement)

    # Queue a flash message to show the user.
    flash("Your application has been submitted! Don't refresh the page.")

    # Pass Jinja all the user information to fill out the response template.
    return render_template("application-response.html",
                           first=first_name,
                           last=last_name,
                           position=desired_position,
                           salary_req=prettified_salary_req)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

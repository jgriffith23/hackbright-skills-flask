"""A class containing all job posting data, for easy
templating with Jinja."""


class Job(object):
    """A job type."""

    def __init__(self, unique_id, title, description):
        """Initializes class attributes for job title and description
        on new instances of Job."""
        self.unique_id = unique_id
        self.title = title
        self.description = description

    def __repr__(self):
        """Show human-readable info about the job in the console."""
        return "<Job: {}, {}, {}>".format(self.unique_id,
                                          self.title,
                                          self.description)


def read_jobs_from_file(filepath):
    """Read jobs from master list of job text.

    Returned dictionary is formatted as {unique_id: Job object}."""

    jobs = {}
    positions_to_post = []

    # Open the passed file and iterate over it line by line
    for line in open(filepath):

        # Unpack the fields from the file into three variables
        (unique_id, title, description) = line.strip().split("|")
        print "****"
        print title
        print "****"

        if title in positions_to_post:
            print "--------------------------------------------"
            print "ALERT: "
            print "{} already in the list of jobs to be posted.".format(title)
            print "Not adding job with id {} to site.".format(unique_id)
            print "Check job database for duplicate postings."
            print "--------------------------------------------"
            continue

        else:
            # Track the positions we've added so far to help avoid
            # accidental repeat listings.
            positions_to_post.append(title)

            # Cast the job ID to an int to work with it more easily
            unique_id = int(unique_id)

            # Store the job in the dictionary
            jobs[unique_id] = Job(unique_id, title, description)

    return jobs


def get_all_jobs():
    """Get all jobs from database."""

    return jobs_to_post.values()

def get_job_info_in_lists():
    """Gives job attributes as a list of lists, so the display order
    can be controlled.

    Should give a list of the format [[unique_id, title, description], ...]
    """

    # First, get all the job objects available at this time.
    all_jobs = get_all_jobs()

    # Create an empty list to store our lists of job attributes.
    job_info_in_lists = []

    # Iterate over the job objects.
    for job in all_jobs:

        # Add this job's info to the master list.
        job_info_in_lists.append([job.unique_id, job.title, job.description])

    # Sort the list of job attributes before return, so that they appear in
    # order by ID. This should keep postings in order by ID on the site.
    return sorted(job_info_in_lists)

# Used for get_all_jobs().
jobs_to_post = read_jobs_from_file("jobs.txt")

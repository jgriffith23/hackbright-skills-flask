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

    # Open the passed file and iterate over it line by line
    for line in open(filepath):

        # Unpack the fields from the file into three variables
        (unique_id, title, description) = line.strip().split("|")

        if title in jobs.keys():
            print "|{} already in the list of jobs to be posted.|".format(
                  title)
            continue
        else:
            # Cast the job ID to an int to work with it more easily
            unique_id = int(unique_id)

            # Store the job in the dictionary
            jobs[unique_id] = Job(unique_id, title, description)

        return jobs

jobs_to_post = read_jobs_from_file("jobs.txt")
print jobs_to_post

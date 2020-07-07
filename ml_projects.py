# Importing Flask essentials
from flask import Flask, request, render_template, redirect, url_for

# Importing Pandas for Data Reading
import pandas as pd

# Importing own modules
from py_modules import data_extraction as de

# Flask App
ml_app = Flask(__name__)

# Reading my social links data
social = pd.read_csv('data/social-media-links.csv')

# Extraction of social link data
social_data = de.get_social_link_data(social)

# Counting number of Data
number_of_links = len(social_data[0])

# Root or Home page - About Me
@ml_app.route('/')
def all_projects():
	# Reading ML_Projects data
	ml_projects = pd.read_csv('data/ML_Projects.csv')
	# Calculating number of projects
	number_of_projects = ml_projects.shape[0]
	# Calculating rows for UI
	rows = (number_of_projects // 3) + 1
	# Extracting Machine Learning Projects Data
	ml_projects_data = de.get_ml_projects_data(ml_projects)

	# Extracting Libraries links
	libraries = ml_projects_data[8]
	libraries_used = [[str(library) for library in rows.split('|')] for rows in libraries]

	return render_template('all_projects.html',
                        social_data=social_data,
                        n = number_of_links,
                        ml_projects_data = ml_projects_data,
                        rows = rows,
                        libraries_used = libraries_used)


# App Launcher
if __name__ == '__main__':
	ml_app.run(debug = True, port = 3000)
### Date created
2021-12-16

### Project Title
bikeshare data Analysis

### Description
This flask app analyzes bikeshare data for Chicago, New York, and Washington DC and returns a dashboard with statistics.

### Files used
app.py -> contains the flask application<br>
requirements.txt -> contains the dependencies for the project.<br>
raw_data -> contains all CSV data for each city. ⚠️ git ignored for now.<br>
data_analysis -> contains all treatments necessary to transform the CSV's into statistics.<br>
templates -> contains html docs rendered by the app.<br>
Static -> Contains CSS and JS files used by the templates.<br>


### How to install the app
<ol>
    <li>Download the flies and ensure you have the correct python(3.96) version.</li><br>
    <li>Unzip the download folder</li><br>
    <li>Save the folder on a convenient location like desktop.</li><br>
    <li>Open a terminal and change the directory to the project folder.<br>I used a WSL (a linux machine on windows)</li><br>
    <li>Run the command bellow to create a virtual environment:<br><code>$ python3.9 -m venv venv</code></li><br>
    <li>Activate the virtual environment by running:<br><code>$ source venv/bin/activate</code></li><br>
    <li>Install the dependencies on the requirements.txt<br><code>$ pip install -r requirements.txt</code></li><br>
    <li>Run the flask app:<br><code>$ flask run</code></li><br>
    <li>Open the browser and go to:<br><a href="bikeshare data analysis">http://127.0.0.1:5000/</a></li><br>
</ol>
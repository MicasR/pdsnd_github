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
    <li>Download the flies and ensure you have the correct python(3.96) version.<br><a href="bikeshare">https://github.com/MicasR/pdsnd_github.git</a></li>
    <li>Unzip the download folder</li>
    <li>Save the folder on a convenient location like desktop.</li>
    <li>Open a terminal and change the directory to the project folder.<br>I used a WSL (a linux machine on windows)</li>
    <li>Run the command bellow to create a virtual environment:<br>$python3.9 -m venv venv</li>
    <li>Activate the virtual environment by running:<br>$source venv/bin/activate</li>
    <li>Install the dependencies on the requirements.txt<br>$source venv/bin/activate</li>
    <li>Run the flask app:<br>$flask run</li>
    <li>Open the browser and go to:<br><a href="bikeshare data analysis">http://127.0.0.1:5000/</a></li>
</ol>
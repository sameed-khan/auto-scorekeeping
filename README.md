# auto-scorekeeping
Contains scripts in order to automate the eballot to adderpit scorekeeping process.
Contains two scripts:
1. **insert_IDvalidation.py** - loops through all the ballots and inserts the competitor regular expression validation for each one. 
    1. Currently uses a dict of "competition_name":"ballot_url" in order to access ballots. Future improvements would use a specifically formatted .csv file that would be converted into a dict in script.
        1. Example of dict entry would be "2D Islamic Art":"https://forms.google.com/...."

2. **auto_scoreinput.py**
    1. Currently uses a dict of "competition_name":"spreadsheet_url" in order to access eballot scorecards. Future improvements would use a specifically formatted .csv file that would be converted into a dict in script. Is there a way to scrape these from GDrive, or specifically format eballot names to match them with the Adderpit designations?
        1. Example of dict entry would be "2D Islamic Art":"https://spreadsheets.google.com/..."
        2. client_secret.json is required for oauth2client validation/Google Drive API credentials/spreadsheet access credentials

## Other Items
* **mist-registration.csv** contains slightly formatted data pulled from Adderpit. DO NOT CHANGE this file -- all data structural modifications should take place in script. All competition names should match text EXACTLY as is in this spreadsheet. This spreadsheet is used for accessing MIST IDs for competitor by competitions, along with other associated data. 
* Further entries will detail instructions for how to use each script. 

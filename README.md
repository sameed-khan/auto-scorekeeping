# auto-scorekeeping
Contains scripts in order to automate the eballot to adderpit scorekeeping process.
Contains two scripts:
**insert_IDvalidation.py** - loops through all the ballots and inserts the competitor regular expression validation for each one. 
    
1. Currently uses a dict of "competition_name":"ballot_url" in order to access ballots. Future improvements would use a specifically formatted .csv file that would be converted into a dict in script.
    1. Example of dict entry would be "2D Islamic Art":"https://forms.google.com/...."

**auto_scoreinput.py**

1. Currently uses a .csv file for each competition. Refer to sample_comps.csv for an example of what the format looks like.
    1. Example of csv entry would be "2D Islamic Art" in "competition column", "https://spreadsheets.google.com/..." in url column.


## Other Items
* **mist-registration.csv** contains slightly formatted data pulled from Adderpit. DO NOT CHANGE this file -- all data structural modifications should take place in script. All competition names should match text EXACTLY as is in this spreadsheet. This spreadsheet is used for accessing MIST IDs for competitor by competitions, along with other associated data. 
* Further entries will detail instructions for how to use each script. 

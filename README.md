# auto-scorekeeping
Contains selenium scripts in order to automate the eballot to adderpit scorekeeping process.

The scorekeeping process is outlined below to provide direction for the project: 

1. All eballot forms need to be populated with MIST IDs in their regular expression validation section
    1. Navigate to each eballot, pull from **master eballot table**
    2. Fill in regular expression fields with competitor MIST IDs
2. (All competitions besides brackets and KT) eballot results need to be input into Adderpit.
    1. Use gspread to grab results from Google spreadsheets Final Results sheet
    2. Insert results into Adderpit "input scores" page
    3. Same workflow for KT and Brackets, but code will change per the format of the spreadsheet


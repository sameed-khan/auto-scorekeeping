import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


# # use creds to create a client to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)
#
# # Find a workbook by name and open the first sheet
# # Make sure you use the right name here.
# sheet = client.open("test").sheet1
#
# # Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

competitors = pd.read_csv("mist-registration.csv", na_filter=False)
for idx in range(0, len(competitors)):
    competitor = competitors.iloc[idx, :]
    if competitor.gender == "Male":
        if "Quran" in competitor.knowledge:
            competitor.knowledge = competitor.knowledge + "B"
        if competitor.groupProjects == "Nasheed":
            competitor.groupProjects = competitor.groupProjects + "B"
        if competitor.sports == "Soccer" or competitor.sports == "Basketball":
            competitor.sports = competitor.sports + "B"
        if competitor.brackets == "Improv":
            competitor.brackets = competitor.brackets + "B"
    if competitor.gender == "Female":
        if "Quran" in competitor.knowledge:
            competitor.knowledge = competitor.knowledge + "S"
        if competitor.groupProjects == "Nasheed":
            competitor.groupProjects = competitor.groupProjects + "S"
        if competitor.sports == "Soccer" or competitor.sports == "Basketball":
            competitor.sports = competitor.sports + "S"
        if competitor.brackets == "Improv":
            competitor.brackets = competitor.brackets + "S"
comp_list = ["2D Islamic Art", "3D Islamic Art", "Culinary Arts", "Photography", "Scrapbook"]
competitors["competitions"] = competitors[competitors.columns[9:]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1)

foo = competitors.loc[competitors.competitions.str.contains("Business Venture")].mist_id
temp=[]
for element in foo:
    temp.append(element[:4])
fo = "|".join(list(set(temp)))
print(fo)

# for comp in comp_list:
#     for idx in range(0, len(competitors)):
#         if comp in competitors.iloc[idx, :].competitions:
#             print(comp, " was found for this competitor!")

# The purpose of this script is to automatically take information from eballots and automatically input it into the
# Adderpit scorekeeping page

from splinter import Browser
import pandas as pd
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
# Creating and preparing the competitor information table
competitors = pd.read_csv("mist-registration.csv", na_filter=False)
# Creating competitions dataframe for conversion to dictionary
competitions = pd.read_csv("sample_comps.csv")

# Import and clean up the data table
# Each row is a competitor, and each column is a property of the competitor (i.e: competitor has properties (name, etc)
# Each row is parsed so that gender-specific competitions are labeled as such
# Columns are merged so that competitions aren't divided by category but are merged together into one column
# Example: art      writingOratory      groupProjects
#          2D Art   Spoken Word         ImprovS (for sisters improv, ImprovB for brothers improv)
# becomes one column:
#                   competitions
#                   2D Art,Spoken Word,ImprovS
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
competitors["competitions"] = competitors[competitors.columns[9:]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1)

# will be used for the future
SPREADSHEET_URLS = {competitions.iloc[:, 0][idx]:competitions.iloc[:, 1][idx] for idx in range(0, len(competitions))}
# SPREADSHEET_URLS = {
    #the below is a test spreadsheet, do not use
    # "2D Islamic Art":"https://docs.google.com/spreadsheets/d/180W8Jwnp4LQx0x1sTI2HG6tVCqsZ5RzOVG2eSMeZJQM/edit#gid=529048580"
    #"2D Islamic Art":"https://docs.google.com/spreadsheets/d/1y0vycIj3STQ7RHsOlJgTu4X4E2aRQyrhEDDNN6PBYm0/edit#gid=529048580",
    #"3D Islamic Art":"https://docs.google.com/spreadsheets/d/1aBV6hjJ9Zv7btKeR_XcOe2uVik34-rD2_23-riut6R8/edit#gid=1666802291",
    # "Culinary Arts":"https://docs.google.com/spreadsheets/d/1X0BB5rYVoeaBME_kujFhefn1k2QUmjQSy5fa13vynRw/edit#gid=931587849",
    # "Fashion Design":"https://docs.google.com/spreadsheets/d/1kT7uO--Fb5ajEeDkY1n2_7-9F55CW0EXFPKdJFCLGrA/edit#gid=1967765283",
    # "Graphic Design":"https://docs.google.com/spreadsheets/d/16QNLKMCQ8bQhjaYHQVnBalL7flWNSpfloP0bLypXx8U/edit#gid=1759473867",
    # "Photography":"https://docs.google.com/spreadsheets/d/1AxoRcQOi8rdMQQcIZO6r2QmyB4LcFaTksAvm83yIvJw/edit#gid=577905748",
    # "Scrapbook":"https://docs.google.com/spreadsheets/d/1lmZSVagEGo_VP7I7xILQbruuWOPZ1LklEHdkJUzXuRY/edit#gid=1373558960",
    #
    # "American Sign Language":"https://docs.google.com/spreadsheets/d/1odHNFCJ0vBicpXJGnzzgHv-P1a-LZy5BlDlzI6rDqlE/edit",
    # "Extemporaneous Essay":"https://docs.google.com/spreadsheets/d/1BCdWzObv_JKkcK8uB71Z4ILqb3iCnKMeMFWRwAnuZJc/edit#gid=455486567",
    # "Extemporaneous Speaking":"https://docs.google.com/spreadsheets/d/1hikUvleUd4gH15pCVUlPqEMxAZTTPDINnvfteWB5upE/edit#gid=33152967",
    # "Original Oratory":"https://docs.google.com/spreadsheets/d/1NGV6FatuCwirfz50MXWQAB02JM76wDqavRQxoaOool4/edit#gid=408042596",
    # "Poetry Literature":"https://docs.google.com/spreadsheets/d/16vYfuEJL-XlzOPDeTxcgUwtKVaqvpsS-7MPKjCG_euU/edit",
    # "Poetry Spoken Word":"https://docs.google.com/spreadsheets/d/1nC1j6Ete5HyvZqPG9GQxwmaIsn5qZFRRTqJMJgKKRA0/edit",
    # "Prepared Essay":"https://docs.google.com/spreadsheets/d/15MvjS2TTV96TpxKpPeal8JqJH74O00p3CgRSMmeYeng/edit",
    # "Short Fictional Story":"https://docs.google.com/spreadsheets/d/17F1FCHFvo6ORz4TXRxtHRkRn1hg4DdAnqJ1SSgC9zBI/edit",
    #
    # "NasheedB":"https://docs.google.com/spreadsheets/d/1NmYXELe62U1cSUj3QPbO2o    Dcvb6_5DVCDmCs08B5Cy4/edit",
    # "Business Venture":"https://docs.google.com/spreadsheets/d/1xC_EhCz0P3TKO4x-mMfliuQf6nTQzSeuZ-lKcpSTJrk/edit#gid=2083081288",
    # "Community Service":"https://docs.google.com/spreadsheets/d/1WsbRRd_TAtzHjXT9J9NW2BdzF8thC_DP-JAgsxdq4tg/edit#gid=362809383",
    # "Mobile Apps":"https://docs.google.com/spreadsheets/d/1oECHvu_uO3Sk768B0khzA7uCT8kZlXqusSwba-mrGPE/edit#gid=2139371314",
    # "Science Fair":"https://docs.google.com/spreadsheets/d/1T9Qq5X5xIwnN8j5KSF43PQxPktqFixJT-IC82t-xF1M/edit",
    # "Short Film":"https://docs.google.com/spreadsheets/d/1nKmade1woGI3w0BRzPLRI42xBRZBMfkBFLnUFdeLGfg/edit",
    # "NasheedS":"https://docs.google.com/spreadsheets/d/1TlAV63QW3w_TstsfRBb7Hw5AdGv2c6TErq-sTYF0baM/edit#gid=443908018",
    # "Social Media":"https://docs.google.com/spreadsheets/d/12EqjVyvke3X4s94iX9cVMRORg4sFbNnIMXT-Km1TioI/edit#gid=1708494103",
    #
    # "Quran Memorization Level 1B":"https://docs.google.com/spreadsheets/d/1I2TDCuxDqkc27w5D6YfMttuwcZoL3c-ZYdn-sAXfr1w/edit",
    # "Quran Memorization Level 1S":"https://docs.google.com/spreadsheets/d/1_OE5nlCjaTZ0vh4RUlSZ5B9CnHgJvON0QQ9XuHg3DS8/edit#gid=1236883472",
    # "Quran Memorization Level 2B":"https://docs.google.com/spreadsheets/d/1SHPf41rO7JhVCForP5V5YsaaGSHRRo4NlC6VW4_SovI/edit",
    # "Quran Memorization Level 2S":"https://docs.google.com/spreadsheets/d/1RzWichSMvoKXP8d8AcFDf5wu3fLffBxI-mHxTiMeJms/edit",
    # "Quran Memorization Level 3B":"https://docs.google.com/spreadsheets/d/1MCRo-uyMaNrz-mC8z1AYM99eokklXMuWXi0ZsrtziPo/edit#gid=440586875",
    # "Quran Memorization Level 3S":"https://docs.google.com/spreadsheets/d/1m1KFRVyPWsLbsFTEKNaQUs59Tcua6QXuaJqPs1LJeTs/edit#gid=587604772",
    # "Quran Memorization Level 4B":"https://docs.google.com/spreadsheets/d/1qv62Wo81ULciA396Q2owfwZvfDVQW6vpU2R-yzs9iho/edit#gid=400572937",
    # "Quran Memorization Level 4S":"https://docs.google.com/spreadsheets/d/1XDuOLd9NTBRNI4_ytVsyQz6WyUE8sZIzczjUcDFyzcg/edit#gid=1070542050",

# }
GENDER_SPEC_COMPS = ["Quran", "Nasheed", "Improv"]
GROUP_COMPS = ["Nasheed", "Business Venture", "Community Service", "Mobile Apps", "Science Fair", "Short Film"
               "Social Media", "Improv", "Debate", "MIST Bowl"]

def pull_id(comp_name):
    """ @param comp_name: EXACT Adderpit string of the competition name being scored
        @return: list of MIST IDs sorted in ascending order for that competition, as strings
    """
    foo = competitors.loc[competitors.competitions.str.contains(comp_name)].mist_id
    for comp in GROUP_COMPS:
        if comp in comp_name:
            competitor_ids = [int(id[:4]) for id in foo]
            competitor_ids.sort()
            return list(dict.fromkeys([str(id) for id in competitor_ids]))
    competitor_ids = [int(id[5:]) for id in foo]
    competitor_ids.sort()
    return list(dict.fromkeys([str(id) for id in competitor_ids]))


def insert_scores(comp_name, score_dict, gender=None):
    """ @param comp_name: EXACT Adderpit string of the competition name being scored (with B or S at the end if
        gender-specific competition)
        @param score_dict: a string:tuple dictionary matching IDs to a tuple of 3 integers
        Example: MIST_ID:(score1, score2, score3) --> '5107-48972':(98, 65, 89)
        @return: None, function accesses Adderpit and inserts scores into fields
    """
    # Drop the 'B' or the 'S' off the comp_name if the competition is gender-specific
    if gender == 1 or gender == 2:
        comp_name = comp_name[:-1]

    browser = Browser('chrome')
    browser.visit("https://web.adderpit.com/MIST")
    browser.find_by_name('username').fill('skhan@getmistified.com')
    browser.find_by_name('password').fill("s4kJ2L|gw")
    browser.find_by_name('submit').click()
    time.sleep(0.300)
    browser.find_by_css("a[href='/MIST/ScoreKeeping']").click()
    time.sleep(0.300)
    css_selector = "a[title='Input Scores for " + comp_name + "']"
    browser.find_by_css(css_selector).click()
    time.sleep(2.000)

    # caveat to navigate to correct interface for gender-segregated competitions
    for comp in GENDER_SPEC_COMPS:
        if comp in comp_name:
            browser.find_by_css("a[title='Unified']").click()

    css_name_list=["judge_0_", "judge_1_", "judge_2_"]
    for comp_id in score_dict:
        idx = 0
        for css_name in css_name_list:
            css_name = css_name+comp_id
            # more accounting for gender-specific competitions. The CSS title for a gender-specific score entry field is
            # "judge_X_MIST_ID_1 (for a male, 2 at the end for a female)
            if gender == 1:
                css_name = css_name + "_1"
            if gender == 2:
                css_name = css_name + "_2"
            print(css_name)
            browser.find_by_name(css_name).fill(str(score_dict[comp_id][idx]))
            idx += 1
    time.sleep(5.000)
    browser.find_by_name('submit').click()
    time.sleep(3.000)


for competition in SPREADSHEET_URLS:
    print("Opening: ", competition)
    comp_gender = 0  # flag used to specified for male or female gender specific competitions
    for modname_comp in GENDER_SPEC_COMPS:
        if modname_comp in competition:
            if competition[-1:] == "B":
                comp_gender = 1
            if competition[-1:] == "S":
                comp_gender = 2
    print(comp_gender)
    results_id = client.open_by_url(SPREADSHEET_URLS[competition]).worksheet("Final Score & Ranking").range('A4:D40')
    quick_results = [results_id[i] for i in range(0, len(results_id), 4)]
    print(results_id)
    row_dict={}
    id_idx = 0  # index variable for tracking at which point the competitor id is found in results_id
    for id in pull_id(competition):
        id_idx = 0
        for cell in quick_results:
            print(pull_id(competition))
            if id in cell.value:
                row_dict.update({id:(results_id[(id_idx+1)].value, results_id[(id_idx+2)].value, results_id[(id_idx+3)].value)})
                break
            id_idx += 4
    print(row_dict)
    insert_scores(competition, row_dict, comp_gender)
from splinter import Browser
import time

COMPETITION_DICT = {
    "2D Islamic Art": "https://docs.google.com/forms/d/19GW_boa9Wbzf4VMp5FRiogFDNRZFhuQ8S7sRrn_PgVw/edit?usp=sharing",
    "3D Islamic Art": "https://docs.google.com/forms/d/109_8oJBfmgyiFvSiQ9rOcyPYmNmzaco25cpPOjifLDc/edit?usp=sharing",
    "Culinary Arts": "https://docs.google.com/forms/d/1yPSjuWIcsp_pyTmnIMHsq1s_i_ZpEdYj4ipnalfUatc/edit?usp=sharing",
    "Fashion Design": "https://docs.google.com/forms/d/1JAkj8_KG5Lm7lbPxb8ms5VOmZMjt7pnt8vEsYe63SAs/edit?usp=sharing",
    "Graphic Design": "https://docs.google.com/forms/d/10NyfRnqwLg7knOoa02ST52Twk4Fw1C-tNf4b-6OeETs/edit?usp=sharing",
    "Photography": "https://docs.google.com/forms/d/1k69ist95_Y2A0A3XgCS6ccn3qHFPFciUeOOupEQQZ7U/edit?usp=sharing",
    "Scrapbook": "https://docs.google.com/forms/d/14g5SICPmpMXoeGl6C34BrjjrtFj6i15t4dG0M8MnbLw/edit?usp=sharing",

    "Prepared Essay": "https://docs.google.com/forms/d/1hQ5g3nTasTWp6BdxtrFrn7mdAMW2E9ABMsakDWm0v5E/edit?usp=sharing",
    "Extemporaneous Speaking": "https://docs.google.com/forms/d/1KfQd3P_j6-k5TTwfmc9Va_XU-RWWpY7-ZF1KRDKEOg0/edit?usp=sharing",
    "Extemporaneous Essay": "https://docs.google.com/forms/d/149v982uTaYlyWBbDseB72qmQBF-zbmPcGGSPHRsjWeQ/edit?usp=sharing",
    "Original Oratory": "https://docs.google.com/forms/d/1TOkjclZ66ODHtGA5hHIiyy5VKblvrV4Lqka3NMRLDgc/edit?usp=sharing",
    "Poetry Literature": "https://docs.google.com/forms/d/1bmHKzDYKJI9YlHMBVMwHoA1LgeQJcJDUB81jHz4ItQE/edit?usp=sharing",
    "Poetry Spoken Word": "https://docs.google.com/forms/d/1y4s_ToN_70Q0R8H5LJhEsoBEQNySptgEuGtkoP0NpQw/edit?usp=sharing",
    "American Sign Language": "https://docs.google.com/forms/d/1Xo9BtEakShfZlDJMxA0xhDNEv1x0z_Wh68ozsXR_cK4/edit?usp=sharing",
    "Short Fictional Story": "https://docs.google.com/forms/d/1XE1g66JDvOAEhVOYESeQTu1LJXclaNG21yOuiR-qsvQ/edit?usp=sharing",

    "Business Venture": "https://docs.google.com/forms/d/1NBuVoxGVd-4wRb-zoega4eo4P2u55_WmEJxVO3m6dHU/edit?usp=sharing",
    "Community Service": "https://docs.google.com/forms/d/1-2urfxXGdTUgXmHkhDVSsyi-ZeRJTmMwx28y0Eky29M/edit?usp=sharing",
    "Mobile Apps:": "https://docs.google.com/forms/d/14D9Ayb_kcHImC1K4pKX0UxdtIT91CcGDkuLfXRIVfFI/edit?usp=sharing",
    "Science Fair": "https://docs.google.com/forms/d/11k2iBJR2NNiopqgXXNllYdliLpQkeZnVTEtNZKcpdfM/edit?usp=sharing",
    "Short Film": "https://docs.google.com/forms/d/1Zzn2_K14lpaYtjXhdXo45G00vgPiKW5I5qPmqmISQMU/edit?usp=sharing",
    "Social Media": "https://docs.google.com/forms/d/1-upbEuCKLaR59DqMLi0cBSTfYAjO4fPQO4Jq_CWtJqA/edit?usp=sharing",
    "Brothers Nasheed": "https://docs.google.com/forms/d/1YjBfFC6oj4l2Ypj7uuOqD9M3CRyAE7kPvldiwG6EzRg/edit?usp=sharing",
    "Sisters Nasheed": "https://docs.google.com/forms/d/1jshvabSZ2BRF3bi_22EkF6L8G7H5vuzCfZfznUKkQOw/edit?usp=sharing",

    "Quran Memorization Level 1B": "https://docs.google.com/forms/d/1r-WTrezJx9qfUEoGHQljR4Qvm2_Nk1AlbfAFeiQw9GM/edit?usp=sharing",
    "Quran Memorization Level 2B": "https://docs.google.com/forms/d/1WzUopN8Rssw3UMRn2SS9hT_bh4b2Mb85xBci-FmJ7vI/edit?usp=sharing",
    "Quran Memorization Level 3B": "https://docs.google.com/forms/d/1p6t9xeEt7tPXiJaOzHubzZt_pPMUaOxG9WYhP9fxxKg/edit?usp=sharing",
    "Quran Memorization Level 4B": "https://docs.google.com/forms/d/1gjqIkF57GCISFQj361D9ElfKXVns92EJy9OhAjNW0Dw/edit?usp=sharing",

    "Quran Memorization Level 1S": "https://docs.google.com/forms/d/1RTZWP1ZaJGAaahFSXKsjPs26ZxF0bg2xr_VVaXmFRzY/edit?usp=sharing",
    "Quran Memorization Level 2S": "https://docs.google.com/forms/d/1borBRuTtWVhwbF-9RBrLL81Qo8iRG2knN-p49DPv7GM/edit?usp=sharing",
    "Quran Memorization Level 3S": "https://docs.google.com/forms/d/1Z6PCnbzFcqm5u6tCGv14CLCTwjo80rNlaaMlQxmkN0k/edit?usp=sharing",
    "Quran Memorization Level 4S": "https://docs.google.com/forms/d/1Z6ZxgacUvK_wspvTWGq5FYp9W9UQ8YnQEncoJAv5ozs/edit?usp=sharing",
}

browser = Browser('chrome')

for ballot in COMPETITION_DICT:
    print(ballot)
    browser.visit(COMPETITION_DICT[ballot])
#login sequence
# browser.visit('https://accounts.google.com')
# browser.fill('identifier', 'skhan@getmistified.com')
# browser.find_by_id('identifierNext').click()
# while browser.is_element_not_present_by_name('password'):
#     time.sleep(0.300)
# browser.find_by_name('password').fill('N3y50hnWeulk')
# time.sleep(0.300)

#editing Google Form
# browser.visit('https://docs.google.com/forms/d/19GW_boa9Wbzf4VMp5FRiogFDNRZFhuQ8S7sRrn_PgVw/edit?usp=sharing')
# browser.find_by_css('textarea[data-initial-value="MIST ID"]').click()
# browser.find_by_css('input[aria-label="Pattern"]').fill('this is an input')

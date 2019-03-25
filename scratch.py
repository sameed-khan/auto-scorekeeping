from splinter import Browser
import time
browser = Browser('chrome')
browser.visit("https://web.adderpit.com/MIST")
browser.find_by_name('username').fill('skhan@getmistified.com')
browser.find_by_name('password').fill("s4kJ2L|gw")
browser.find_by_name('submit').click()
time.sleep(0.300)
browser.find_by_css("a[href='/MIST/ScoreKeeping']").click()
time.sleep(2.000)
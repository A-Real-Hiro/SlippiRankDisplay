from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://slippi.gg/user/hiro-696")
time.sleep(3)
import pdb
pdb.set_trace()
rank_name = driver.find_element(by="class name", value= "jss7")

print(rank_name)
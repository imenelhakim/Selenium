
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#for the using of docx
from docx import Document
from docx.shared import Inches


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver= webdriver.Chrome(PATH)

driver.get("https://www.marmiton.org/")

print(driver.title)

search = driver.find_element_by_name("aqt") #element search
search.send_keys("gâteaux") #searched word
search.send_keys(Keys.RETURN) 


#recipe-results, in this case, is the element which contains all the needed items 
main = driver.find_element_by_class_name("recipe-results ")
print(main.text)

#create document object
document = Document()
#add the "main" results into the heading
document.add_heading(main.text, 0)
#save to a word file
document.save('test.docx')


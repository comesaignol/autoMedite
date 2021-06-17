# -*- coding: utf-8 -*-

######################
### CONFIGURATIONS ###
######################

import config

# Librairie scrapping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Librairie gestion de fichier
import os
import codecs
import shutil

# Librairie Data Science
import pandas as pd
from bs4 import BeautifulSoup

"""
createDir : create a new dir
"""

def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)
  print("Done", "Create dir : ", path)



"""
readTXT : lecture des fichiers txt 
"""

def readTXT(path):
  with codecs.open(path, "r", encoding="utf-8") as file:
    text = file.read()
    print("Done", "Read TXT file : " + path)
    return text

"""
main :
  @casse
  @separator
  @diacritique
  @word
"""

def main(casse, separator, diacritique, word):
    
  print("")
  print("<><><><><><><><><>")
  print("<> ALIGNMENT RAW <>")
  print("<><><><><><><><><>")
  print("")
    
  # Read text 1
  text1Source = config.text1 + ".txt"
  text1SourcePath = os.path.join(config.dirCorpus, text1Source)
  text1SourceTXT = readTXT(text1SourcePath)
    
  # Read text 2
  text2Source = config.text2 + ".txt"
  text2SourcePath = os.path.join(config.dirCorpus, text2Source)
  text2SourceTXT = readTXT(text2SourcePath)
    
  # Create Web Driver
  browser = webdriver.Firefox()
  browser.get(config.urlMEDITE)
  print("Done", "Access MEDITE")
    
  # Send texts
  commande1 = "document.getElementById('etat1').value='" + text1SourceTXT + "';"
  browser.execute_script(commande1)
  commande2 = "document.getElementById('etat2').value='" + text2SourceTXT + "';"
  browser.execute_script(commande2)
  
  # Passage de l'option casse
  if casse == False:
    checkbox = browser.find_element_by_xpath('//input[@id="pcaseSensitive"]')
    if(checkbox.is_selected()):
      checkbox.click()
  
  # Option separator
  if separator == False:
    checkbox = browser.find_element_by_xpath('//input[@id="pseparatorSensivitive"]')
    if(checkbox.is_selected()):
      checkbox.click()
  
  # Option diacritique
  if diacritique == False:
    checkbox = browser.find_element_by_xpath('//input[@id="pdiacriticSensitive"]')
    if(checkbox.is_selected()):
      checkbox.click()
  
  # Option word
  if word == False:
    checkbox = browser.find_element_by_xpath('//input[@id="pcarOuMot"]')
    if(checkbox.is_selected()):
      checkbox.click()
    
  # Validation
  submit = browser.find_element_by_xpath('//input[@name="submitMedite"]')
  submit.click()
  print("... Comparison ...")
    
  # Waiting the page
  try:
    element = WebDriverWait(browser, 600).until( # 10 minutes maximum
        EC.presence_of_element_located((By.ID, "modifications"))
    )
  finally:
    # Create dir
    createDir(config.dirAlignmentRawName)
    
    # Save HTML raw
    with open(config.alignmentRawHTML, "w+", encoding="utf-8") as out:
      out.write(browser.page_source)
      print("Done", "Save HTML raw : ", config.alignmentRawHTML)
      
    # Correction HTML raw
    with open(config.alignmentRawHTML, "r", encoding="utf-8") as file:
      
      # On parse le document
      soup = BeautifulSoup(file, "lxml")
      
      # Suppression des vieilles librairies
      for elt in soup.find_all("script"):
        elt.decompose()  
      for elt in soup.find_all("link"):
        elt.decompose()
      for elt in soup.find_all("div", attrs = {"id" : "modal-content"}):
        elt.decompose()
      for elt in soup.find_all("div", attrs = {"id": "browser-detection-info"}):
        elt.decompose()
      for elt in soup.find_all("div", attrs = {"id": "button_box"}):
        elt.decompose()
      for elt in soup.find_all("div", attrs = {"id": "modifications"}):
        elt.decompose()
    
    # Export alignment
    with open(config.alignmentRawHTML, "wb") as fichier:
      fichier.write(soup.prettify("utf-8"))
      print("Done", "Correction HTML raw", config.alignmentRawHTML)
      
    # Extraction text
    with open(config.alignmentRawHTML, "r", encoding="utf-8") as file:
      
      # Parse file
      soup = BeautifulSoup(file, "lxml")
    
      # Extract text 1
      for elt in soup.find_all("div", attrs = {"id": "txt_window"}):
        text = elt.extract()
      with open(config.text1AlignRaw, "wb") as fichier:
        fichier.write(text.prettify("utf-8"))
      print("Done", "Export alignment raw : ", config.text1AlignRaw)
      
      # Extract text 2
      for elt in soup.find_all("div", attrs = {"id": "txt_window_2"}):
        text = elt.extract()
      with open(config.text2AlignRaw, "wb") as fichier:
        fichier.write(text.prettify("utf-8"))
      print("Done", "Export alignment raw : ", config.text2AlignRaw)
      
      # End session
      browser.quit()
      print("Done", "Quit MEDITE")
    

"""
Command
"""

main(casse=False, separator=False, diacritique=False, word=True)

   
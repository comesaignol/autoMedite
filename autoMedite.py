# -*- coding: utf-8 -*-

######################
### CONFIGURATIONS ###
######################

import config

##################
### LIBRAIRIES ###
##################

from selenium import webdriver
from bs4 import BeautifulSoup
import os
import codecs
import shutil
import pandas as pd

####################
### INSTRUCTIONS ###
####################

# * Ne pas nommer de script python "selenium" sous peine de bug
# * Télécharger chrome driver en fonction de votre version de Google Chrome : http://chromedriver.chromium.org/downloads (version74)
# * Copier-coller chrome driver dans C:\ProgramData\Anaconda3


#####################
### CREATE OUTPUT ###
#####################

def createOutput():
  if os.path.exists(config.dirOutput):
  	shutil.rmtree(config.dirOutput)
  os.mkdir(config.dirOutput)

def saveOutput(soup):
  pathOutput = os.path.join(config.dirOutput, "out.html")
  with codecs.open(pathOutput, "w+", encoding="utf-8") as out:
    out.write(soup)
  print("Done")

def main():
  
  # Création du dossier de sortie
  createOutput()

  # Création du Web Driver
  """
  chromeOptions = webdriver.ChromeOptions()
  browser = webdriver.Chrome(options=chromeOptions)
  """
  
  df = pd.read_csv("relation.tsv", sep='\t', header=0)
  for i in range(len(df)):
    state1Path = os.path.join(config.dirCorpus, df.loc[i,"Etat 1"])
    state2Path = os.path.join(config.dirCorpus, df.loc[i,"Etat 2"])
    
    with codecs.open(state1Path, "r", encoding="utf-8") as state1:
      state1TXT = state1.read()
      
    with codecs.open(state2Path, "r", encoding="utf-8") as state2:
      state2TXT = state2.read()
  
  """
  # Accéder au site
  browser.get(config.urlMEDITE)
  
  # Envoi dans la zone 1
  browser.find_element_by_id("etat1").send_keys("test 1")
  
  # Envoi dans la zone 2
  browser.find_element_by_id("etat2").send_keys("test 2")
  
  # Validation
  agree = browser.find_element_by_xpath('//input[@name="submitMedite"]')
  agree.click()
  
  # Parsing de la page
  content = browser.page_source
  soup = BeautifulSoup(content, features="lxml")
  soupString = str(soup)
  
  # Sauvegarde du résultat
  saveOutput(soupString)
  
  # Fin de la session
  browser.quit()
  """
main()

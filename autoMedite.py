# -*- coding: utf-8 -*-

######################
### CONFIGURATIONS ###
######################

import config

##################
### LIBRAIRIES ###
##################

# Librairie scrapping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Librairie gestion de fichier
import os
import codecs
import glob
import shutil

# Librairie Data Science
from bs4 import BeautifulSoup
import pandas as pd

####################
### INSTRUCTIONS ###
####################

# * Ne pas nommer de script python "selenium" sous peine de bug ;
# * Attention : la moindre présence d'une apostrophe droite peut faire planter la machine !
# * Télécharger chrome driver en fonction de votre version de Google Chrome : http://chromedriver.chromium.org/downloads (version74)
# * Copier-coller chrome driver dans C:\ProgramData\Anaconda3
# * https://github.com/mozilla/geckodriver/releases

#####################
### CREATE OUTPUT ###
#####################

def createOutput():
  if os.path.exists(config.dirOutput):
  	shutil.rmtree(config.dirOutput)
  os.mkdir(config.dirOutput)
  
def saveTXT(pathFile):
  with codecs.open(pathFile, "r", encoding="utf-8") as file:
    stateTXT = file.read()
    return stateTXT

def main():
  
  # Création du dossier de sortie
  createOutput()
  
  # Lancement du programme pour chaque analyse désirée
  df = pd.read_csv("relation.tsv", sep='\t', header=0)
  for i in range(len(df)):
    
    # Récupération des noms du fichier
    state1Path = os.path.join(config.dirCorpus, df.loc[i,"Etat 1"])
    state2Path = os.path.join(config.dirCorpus, df.loc[i,"Etat 2"])
    
    state1TXT = saveTXT(state1Path)
    state2TXT = saveTXT(state2Path)
      
    # Création du Web Driver
    browser = webdriver.Firefox()
    print("Done", "Ouvrir le navigateur")
  
    # Accéder au site
    browser.get(config.urlMEDITE)
    print("Done", "Accéder au site")
    
    # Envoie des textes
    """
    NOTA BENE : On pourrait les textes par la méthode "send_keys", mais pour les longs textes le passage à l'échelle est rendue difficile. La méthode utilisée par un code javascript ci-dessous permet de gagner considérablement du temps.
    """
    commande1 = "document.getElementById('etat1').value='" + state1TXT + "';"
    browser.execute_script(commande1)
    
    commande2 = "document.getElementById('etat2').value='" + state2TXT + "';"
    browser.execute_script(commande2)
    
    # Validation
    submit = browser.find_element_by_xpath('//input[@name="submitMedite"]')
    submit.click()
    
    # On attend que la page soit affichée
    try:
      element = WebDriverWait(browser, 600).until( # Attente de 10 min
          EC.presence_of_element_located((By.ID, "modifications"))
      )
    finally:
      # Parsing de la page
      """
      content = browser.page_source
      soup = BeautifulSoup(content, features="lxml")
      soupString = str(soup)
      """
      # Sauvegarde du résultat
      nameOutput = df.loc[i,"Name"]
      pathOutput = os.path.join(config.dirOutput, nameOutput)
      
      with codecs.open(pathOutput, "w+", encoding="utf-8") as out:
        out.write(browser.page_source)
      print("Done", "Sauvegarde des résultats")
      
      # Fin de la session
      browser.quit()
      print("Done", "Quitter le navigateur")

main()

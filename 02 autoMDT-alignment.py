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

"""
createDirOutput : création du dossier "output" qui va accueillir les résultats.
"""

def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)
  print("Done", "Création du dossier", path)

"""
"""


def readTXT(path):
  with codecs.open(path, "r", encoding="utf-8") as file:
    text = file.read()
    print("Done", "Lecture du fichier TXT : " + path)
    return text

"""
"""

def main(casse, separator, diacritique, word):
  
  # Lecture du fichier alignement
  df = pd.read_csv("relation.tsv", sep='\t', header=0)
  
  # Lancement du programme pour chaque alignement
  for i in range(len(df)):
    
    print("<><><><><><><><><>")
    print("<> ALIGNMENT " + str(i+1) + " <>")
    print("<><><><><><><><><>")
    
    # Récupération des paths des fichier
    text1Path = os.path.join(config.dirCorpus, str(df.loc[i,"Etat 1"]) + ".txt")
    text2Path = os.path.join(config.dirCorpus, str(df.loc[i,"Etat 2"]) + ".txt")
    
    # Lecture des fichiers TXT
    text1 = readTXT(text1Path)
    text2 = readTXT(text2Path)
    
    # Création du Web Driver
    browser = webdriver.Firefox()
    print("Done", "Ouvrir le navigateur")
    browser.get(config.urlMEDITE)
    print("Done", "Accés au site MEDITE")
    
    # Récupération des textes
    commande1 = "document.getElementById('etat1').value='" + text1 + "';"
    commande2 = "document.getElementById('etat2').value='" + text2 + "';"
    
    # Envoi des textes
    browser.execute_script(commande1)
    browser.execute_script(commande2)
    
    # Passage des options
    if casse == False:
      checkbox = browser.find_element_by_xpath('//input[@id="pcaseSensitive"]')
      if(checkbox.is_selected()):
        checkbox.click()
      
    if separator == False:
      checkbox = browser.find_element_by_xpath('//input[@id="pseparatorSensivitive"]')
      if(checkbox.is_selected()):
        checkbox.click()
        
    if diacritique == False:
      checkbox = browser.find_element_by_xpath('//input[@id="pdiacriticSensitive"]')
      if(checkbox.is_selected()):
        checkbox.click()
        
    if word == False:
      checkbox = browser.find_element_by_xpath('//input[@id="pcarOuMot"]')
      if(checkbox.is_selected()):
        checkbox.click()
    
    # Validation
    submit = browser.find_element_by_xpath('//input[@name="submitMedite"]')
    submit.click()
    print("... Comparaison en cours ...")
    
    # On attend que la page soit affichée
    try:
      element = WebDriverWait(browser, 600).until( # Attente de 10 min maximum
          EC.presence_of_element_located((By.ID, "modifications"))
      )
    finally:
      # Création du dossier de sortie
      nameAlignment = df.loc[i,"Alignement"]
      pathAlignment = os.path.join(config.dirOutputAlignment, nameAlignment)
      createDir(pathAlignment)
      
      # Sauvegarde du résultat
      path = os.path.join(pathAlignment, nameAlignment + ".html")
      with codecs.open(path, "w+", encoding="utf-8") as out:
        out.write(browser.page_source)
      print("Done", "Sauvegarde des résultats")
      
      # Fin de la session
      browser.quit()
      print("Done", "Quitter le navigateur")
      
    print("Done", "autoMDT-alignment.py")
    

main(casse=False, separator=False, diacritique=False, word=False)

   
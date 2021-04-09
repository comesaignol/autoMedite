# -*- coding: utf-8 -*-

######################
### CONFIGURATIONS ###
######################

import config

# Librairie gestion de fichier
import os

# Librairie Data Science
from bs4 import BeautifulSoup
import pandas as pd
import re

"""
"""

def saveTXT(path):
  
  with open(path, "r", encoding="utf-8") as fichier:
    
    # Création du string
    soup = BeautifulSoup(fichier, features="lxml")
    soup = soup.find("text").get_text()
    
    # Correction regex
    soup = re.sub("'", "’", soup)
    soup = re.sub("(\n){1,}"," ", soup)
    soup = re.sub("( ){2,}", " ", soup)
    
    # Enregistrement du TXT
    name = os.path.splitext(path)[0] + ".txt"
    pathTXT = os.path.join(config.dirCorpus, name)
    with open(pathTXT, "w+", encoding="utf8") as txt:
      txt.write(soup)
      print("Done", "Création du fichier TXT : " + name)

"""
"""

def main():
  
  # Lecture du fichier alignement
  df = pd.read_csv("relation.tsv", sep='\t', header=0)
  
  # Lancement du programme pour chaque alignement
  for i in range(len(df)):
    
    # Récupération des paths des fichier
    text1Path = os.path.join(config.dirCorpus, str(df.loc[i,"Etat 1"]) + ".xml")
    text2Path = os.path.join(config.dirCorpus, str(df.loc[i,"Etat 2"]) + ".xml")
    
    saveTXT(text1Path)
    saveTXT(text2Path)
    
  print("Done", "autoMDT-xml2txt.py")
    
main()

   
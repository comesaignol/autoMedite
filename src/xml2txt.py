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
saveTXT : extracting text from XML-TEI file with REGEX
"""

def saveTXT(path):
  
  with open(path, "r", encoding="utf-8") as fichier:
    
    # Create strings
    soup = BeautifulSoup(fichier, features="lxml")
    text = soup.find("text").get_text()
    
    # Correction REGEX
    text = re.sub("'", "’", text)
    text = re.sub("(\n){1,}"," ", text)
    text = re.sub("( ){2,}", " ", text)
    
  # Save TXT
  name = os.path.splitext(os.path.basename(path))[0] + ".txt"
  pathTXT = os.path.join(config.dirCorpusRaw, name)
  with open(pathTXT, "w+", encoding="utf8") as txt:
    txt.write(text)
    print("Done", "Create TXT file : " + pathTXT)


"""
Main fuction
"""

def main(text1,text2):
  
  print("")
  print("<><><><><><><><><><><>")
  print("<> CREATE TXT FILES <>")
  print("<><><><><><><><><><><>")
  print("")
  
  
  # Conversion text 1
  text1Source = text1 + ".xml"
  text1SourcePath = os.path.join(config.dirCorpusTei, text1Source)
  saveTXT(text1SourcePath)
  
  # Conversion text 2
  text2Source = text2 + ".xml"
  text2SourcePath = os.path.join(config.dirCorpusTei, text2Source)
  saveTXT(text2SourcePath)


   
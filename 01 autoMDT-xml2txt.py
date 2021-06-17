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
    soup = soup.find("text").get_text()
    
    # Correction REGEX
    soup = re.sub("'", "’", soup)
    soup = re.sub("(\n){1,}"," ", soup)
    soup = re.sub("( ){2,}", " ", soup)
    
    # Save TXT
    name = os.path.splitext(path)[0] + ".txt"
    pathTXT = os.path.join(config.dirCorpus, name)
    with open(pathTXT, "w+", encoding="utf8") as txt:
      txt.write(soup)
      print("Done", "Create TXT file : " + name)


"""
Principal function
"""

def main():
  
  print("")
  print("<><><><><><><><><><><>")
  print("<> CREATE TXT FILES <>")
  print("<><><><><><><><><><><>")
  print("")
  
  
  # Conversion text 1
  text1Source = config.text1 + ".xml"
  text1SourcePath = os.path.join(config.dirCorpus, text1Source)
  saveTXT(text1SourcePath)
  
  # Conversion text 2
  text2Source = config.text2 + ".xml"
  text2SourcePath = os.path.join(config.dirCorpus, text2Source)
  saveTXT(text2SourcePath)


"""
Command
"""
    
main()

   
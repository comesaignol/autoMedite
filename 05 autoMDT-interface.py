# -*- coding: utf-8 -*-

######################
### CONFIGURATIONS ###
######################

import config

# Librairie gestion de fichier
import os
import shutil

# Librairie Data Science
from bs4 import BeautifulSoup
import pandas as pd
import re
import nltk

############
### MAIN ###
############  
  
def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)
  print("Done", "Make dir : ", path)


"""
makeInterface : création de l'interface
"""

def makeInterface(source, target):
  
  # Recup source data
  with open(source, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    
    # Version 1
    version1 = soup.find("text", attrs = {"id" : "version1"})
    version1.name = "div"
    version1.attrs = {}
    
    # Version 2
    version2 = soup.find("text", attrs = {"id" : "version2"})
    version2.name = "div"
    version2.attrs = {}
    
  
  # Add in interface
  with open(target, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    
    # Version 1
    div1 = soup.find("div", attrs = {"id" : "version1"})
    div1.append(version1)
    
    # Version 2
    div2 = soup.find("div", attrs = {"id" : "version2"})
    div2.append(version2)
    
    """
    Premières corrections REGEX
    """
    # Gestion des éléments blocks
    for elt in config.eltBlock:
      for element in soup.find_all(elt):
        element.name = "p"
        element.attrs = None
    
    # Gestion des éléments inlines
    for elt in config.eltInline:
      for element in soup.find_all(elt):
        element.attrs = None
    
    # Annotations
    for elt in soup.find_all("seg", attrs= {"type" : "start"}):
      elt.name = "start"
    for elt in soup.find_all("seg", attrs= {"type" : "end"}):
      elt.name = "end"
      
  # Sauvegarde du HTML
  with open(target, "wb") as fichier:
    fichier.write(soup.prettify("utf-8"))
    print("Done", "Make interface : ", target)
  

"""
correctionInterface : corrige l'interface
"""
def correctionInterface(source):
  
  with open(source, "r", encoding="utf-8") as file:
    
    # Application des regex
    linesRaw = file.readlines()
    linesCorr = []
    for line in linesRaw:
      
      # Gestion des éléments structurants
      line = re.sub("<p>", "", line)
      line = re.sub("</p>", "<br>", line)
      line = re.sub("<l>", "", line)
      line = re.sub("</l>", "<br>", line)
      
      # Gestion des éléments inlines
      for elt in config.eltInline:
        search = "<" + elt + ">"
        line = re.sub(search, "", line)
        search = "</" + elt + ">"
        line = re.sub(search, "", line)
      
      # Gestion des annotations
      line = re.sub('<start ident="(.*?)" subtype="(.*?)" type="start">', r"<span class='\2' id='\1'>", line)
      line = re.sub("</start>", "", line)
      line = re.sub('<end ident="(.*?)" subtype="(.*?)" type="end">', "", line)
      line = re.sub("</end>", "</span>", line)
      linesCorr.append(line)
  
  # Export du fichier
  with open(source, "w+", encoding="utf-8") as file:
    for line in linesCorr:
      file.write(line)
    print("Done", "Correction regex : ", source)


"""
madkeDataAbsolute : création des données absoilues
"""

def makeDataAbsolute(source, target):
  with open(source, "r", encoding="utf-8") as file:
    
    # Parsing du document
    soup = BeautifulSoup(file, "html.parser")
    
    data = []
    
    # Data insertion
    dataInsertion = []
    eltList = soup.find_all("span", attrs = {"class" : "insertion"})
    for elt in eltList:
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        for tok in tokens:
          dataInsertion.append(tok)
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        for tok in tokens:
          dataInsertion.append(tok)
    data.append(len(dataInsertion))
    
    # Data suppression
    dataSuppression = []
    eltList = soup.find_all("span", attrs = {"class" : "suppression"})
    for elt in eltList:
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        for tok in tokens:
          dataSuppression.append(tok)
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        for tok in tokens:
          dataSuppression.append(tok)
    data.append(len(dataSuppression))

    # Data remplacement
    dataRemplacement = []
    eltList = soup.find_all("span", attrs = {"class" : "remplacement"})
    for elt in eltList:
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        for tok in tokens:
          dataRemplacement.append(tok)
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        for tok in tokens:
          dataRemplacement.append(tok)
    data.append(len(dataRemplacement)/2)

    # Data deplacement
    dataDeplacement = []
    eltList = soup.find_all("span", attrs = {"class" : "deplacement"})
    for elt in eltList:
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        for tok in tokens:
          dataDeplacement.append(tok)
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        for tok in tokens:
          dataDeplacement.append(tok)
    data.append(len(dataDeplacement)/2)
    
    # Création des datas
    data = [data]
    columns = ["Insertion", "Suppression", "Remplacement", "Déplacement"]   
    
    # Création du Dataframe
    df = pd.DataFrame(data=data, columns=columns)
    df.to_json(target, orient="records", force_ascii=False, lines=True)
    print("Done", "Make data absolute : ", target)

""" 
Function principal : fonction principale
"""

def main():
    
  print("")
  print("<><><><><><><>")
  print("<> INTERFACE <>")
  print("<><><><><><><>")
  print("")
 
  # Créate dir
  createDir(config.dirInterfaceName)
  createDir(config.dirInterfaceData)
  createDir(config.dirInterfaceResource)
  
  # Deplace resource files
  shutil.copy(config.dirSourceCSS, config.dirInterfaceResource)
  shutil.copy(config.dirSourceJS, config.dirInterfaceResource)
  shutil.copy(config.dirSourceHTML, config.dirInterfaceName)
  
  # Create interface
  makeInterface(config.finalTei, config.finalHTML)
  
  # Correction interface
  correctionInterface(config.finalHTML)
  
  # Création des données absolues
  makeDataAbsolute(config.finalHTML, config.dataAbsoluteCSV)
    
""" 
Command
""" 

main()


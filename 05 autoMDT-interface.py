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
import statistics

############
### MAIN ###
############  
  
def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)
  print("Done", "Make dir : ", path)


"""
moveFiles: 
"""

def moveFiles():
  
  # Move resource files
  createDir(config.dirInterfaceData)
  createDir(config.dirInterfaceTei)
  shutil.copytree(config.dirSourceCSS, config.dirInterfaceCSS)
  shutil.copytree(config.dirSourceJS, config.dirInterfaceJS)
  
  # Move fichier interface
  shutil.copy(config.dirSourceIndex, config.dirInterfaceName)
  
  # Move
  shutil.copy(config.text1AlignStatisticTei, config.dirInterfaceTei)
  shutil.copy(config.text2AlignStatisticTei, config.dirInterfaceTei)
  shutil.copy(config.finalTei, config.dirInterfaceTei)
  print("Done", "Move dir and files in interface")


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
    
    # Modification
    versions = [version1, version2]
    for version in versions:
      
      # Bug ponctuel
      for elt in version.find_all("text"):
        elt.name = "div"
      
      # Dive type set
      for elt in version.find_all("div", attrs = {"type" : "set"}):
        elt.name = "p"
        elt.attrs = None
      
      # Gestion des éléments blocks
      for elt in config.eltBlock:
        for element in version.find_all(elt):
          element.name = "p"
          element.attrs = None
      
      # Gestion des éléments inlines
      for elt in config.eltInline:
        for element in version.find_all(elt):
          element.attrs = None
      
      # Annotations
      for elt in version.find_all("seg", attrs= {"type" : "start"}):
        elt.name = "start"
      for elt in version.find_all("seg", attrs= {"type" : "end"}):
        elt.name = "end"
    
  
  # Add in interface
  with open(target, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    
    # Version 1
    div1 = soup.find("div", attrs = {"id" : "version1"})
    div1.append(version1)
    
    # Version 2
    div2 = soup.find("div", attrs = {"id" : "version2"})
    div2.append(version2)
    
    # Ajout lien téléchargement
    downloadTEI = soup.find("a", attrs = {"id" : "downloadTEI"})
    downloadTEI["href"] = "xml-tei/" + config.alignmentName + "_align-tei.xml"
      
  # Sauvegarde du HTML
  with open(target, "wb") as fichier:
    fichier.write(soup.prettify("utf-8"))
    print("Done", "Make interface : ", target)
  

"""
correctionInterface : corrige l'interface
"""
def correctionInterface(source):
  
  with open(source, "r", encoding="utf-8") as file:
    
    # text = file.read()
    # text = re.sub('<start ident="(.*?)" subtype="(.*?)" type="start">', r"<span class='\2' id='\1'>", text)
    # print(text)
    # Application des regex
    linesRaw = file.readlines()
    linesCorr = []
    for line in linesRaw:
      
      # Gestion des éléments structurants
      line = re.sub("<p>", "", line)
      line = re.sub("</p>", "<br>", line)
      
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
    index = [config.alignmentName]
    columns = ["Insertion", "Suppression", "Remplacement", "Déplacement"]   
    
    # Création du Dataframe
    df = pd.DataFrame(data=data, index=index, columns=columns)
    df = df.transpose()
    df.to_json(target, orient="split")
    print("Done", "Make data absolute : ", target)


def makeDataMoyenne(source, target):
  
  with open(source, "r", encoding="utf-8") as file:
    # Parsing du document
    soup = BeautifulSoup(file, "html.parser")
    
    data = []
    
    # Data insertion
    dataInsertion = []
    eltList = soup.find_all("span", attrs = {"class" : "insertion"})
    for elt in eltList:
      dataInsertionNB = 0 
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        for tok in tokens:
          dataInsertionNB += 1
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        for tok in tokens:
          dataInsertionNB += 1
      dataInsertion.append(dataInsertionNB)
    data.append(statistics.mean(dataInsertion))
    
    # Data suppression
    dataSuppression = []
    eltList = soup.find_all("span", attrs = {"class" : "suppression"})
    for elt in eltList:
      dataSuppressionNB = 0
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        for tok in tokens:
          dataSuppressionNB += 1
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        for tok in tokens:
          dataSuppressionNB += 1
      dataSuppression.append(dataSuppressionNB)
    data.append(statistics.mean(dataSuppression))

    # Data remplacement
    dataRemplacement = []
    eltList = soup.find_all("span", attrs = {"class" : "remplacement"})
    for elt in eltList:
      dataRemplacementNB = 0 
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        for tok in tokens:
          dataRemplacementNB += 1
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        for tok in tokens:
          dataRemplacementNB += 1
      dataRemplacement.append(dataRemplacementNB)
    data.append(statistics.mean(dataRemplacement))

    # Data deplacement
    dataDeplacement = []
    eltList = soup.find_all("span", attrs = {"class" : "deplacement"})
    for elt in eltList:
      dataDeplacementNB = 0 
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        for tok in tokens:
          dataDeplacementNB += 1
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        for tok in tokens:
          dataDeplacementNB += 1
      dataDeplacement.append(dataDeplacementNB)
    data.append(statistics.mean(dataDeplacement))
    
    # Création des datas
    data = [data]
    index = [config.alignmentName] 
    columns = ["Insertion", "Suppression", "Remplacement", "Déplacement"]   
    
    # Création du Dataframe
    df = pd.DataFrame(data, index=index, columns=columns)
    df = df.transpose()
    df.to_json(target, orient="split")
    print("Done", "Make data moyenne : ", target)


"""
makeDataPersonnage : moyenne for each scripture operation
  @source : tei with 
  @target : json file with data
"""

def makeDataPersonnage(source, target):
  
  with open(source, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    
    personnage = soup.find_all("sp")
    
    # Make list personnage
    persoList = []
    for perso in personnage:
      who = str(perso.get("who"))
      persoList.append(who)
    # persoList = persoList.sort()  
    persoList = set(persoList)
    persoList = list(persoList)
    
    # Make data
    insertionData = []
    suppressionData = []
    remplacementData = []
    deplacementData = []
    
    # Count Data
    for who in persoList:
      
      # Initialize count
      insertionNb = 0
      suppressionNb = 0
      remplacementNb = 0
      deplacementNb = 0
      
      # Each personnage
      personnage = soup.find_all("sp", attrs = {"who" : who})
      for perso in personnage:
        # Insertion
        insertion = perso.find_all("seg", attrs = {"subtype" : "insertion"})
        insertionNb = insertionNb + len(insertion)
        # Suppression
        suppression = perso.find_all("seg", attrs = {"subtype" : "suppression"})
        suppressionNb = suppressionNb + len(suppression)
        # Remplacement
        remplacement = perso.find_all("seg", attrs = {"subtype" : "remplacement"})
        remplacementNb = remplacementNb + len(remplacement)
        # Deplacement
        deplacement = perso.find_all("seg", attrs = {"subtype" : "deplacement"})
        deplacementNb = deplacementNb + len(deplacement)
      
      # Ajout des données
      insertionData.append(insertionNb)
      suppressionData.append(suppressionNb)
      remplacementData.append(remplacementNb/2)
      deplacementData.append(deplacementNb/2)
    
    # Création DataFrame
    data = [insertionData, suppressionData, remplacementData, deplacementData]
    index = ["insertion", "suppression", "remplacement", "deplacement"]
    columns = persoList
    df = pd.DataFrame(data, index=index, columns=columns)
    df.to_json(target, orient="split")
    
  print("Done", "Make data personnage : ", target)

"""
Function principal : fonction principale
"""

def main():
    
  print("")
  print("<><><><><><><>")
  print("<> INTERFACE <>")
  print("<><><><><><><>")
  print("")
 
  # Create dir
  createDir(config.dirInterfaceName)
  
  # Move dir and files in interface
  moveFiles()
  
  # Create interface
  makeInterface(config.finalTei, config.finalHTML)
  
  # Correction interface
  correctionInterface(config.finalHTML)
  
  # Make data absolute
  makeDataAbsolute(config.finalHTML, config.dataAbsoluteCSV)
  
  # Make data moyenne
  makeDataMoyenne(config.finalHTML, config.dataMoyenneCSV)
  
  # Make data personnage
  makeDataPersonnage(config.finalStatisticTei, config.dataPersonnageCSV)
  
    
""" 
Command
""" 

main()


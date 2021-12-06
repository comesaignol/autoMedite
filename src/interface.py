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

def moveFiles(text1, text2, alignmentName):
  
# 
# dirInterfaceTemplate = os.path.join(dirInterface, alignmentName, "template")
  # Create dir DATA 
  dirInterfaceData = os.path.join(config.dirInterface, text1 + "-" + text2, "data")
  createDir(dirInterfaceData)
  
  # Move XML-TEI
  dirInterfaceTei = os.path.join(config.dirInterface, text1 + "-" + text2, "xml-tei")
  createDir(dirInterfaceTei)
  fileText1 = os.path.join(config.dirCorpusTei, text1 + ".xml")
  shutil.copy(fileText1, dirInterfaceTei)
  fileText2 = os.path.join(config.dirCorpusTei, text2 + ".xml")
  shutil.copy(fileText2, dirInterfaceTei)
  fileAlignment = os.path.join(config.dirAlignmentTei, alignmentName, alignmentName + "_final.xml")
  shutil.copy(fileAlignment, dirInterfaceTei)
  
  # Move CSS
  dirSourceCSS = os.path.join(config.dirInterface, "resource", "css")
  dirInterfaceCSS = os.path.join(config.dirInterface, text1 + "-" + text2, "css")
  shutil.copytree(dirSourceCSS, dirInterfaceCSS)
  
  # Move JS
  dirSourceJS = os.path.join(config.dirInterface, "resource", "js")
  dirInterfaceJS = os.path.join(config.dirInterface, text1 + "-" + text2, "js")
  shutil.copytree(dirSourceJS, dirInterfaceJS)
  
  # Move INDEX
  dirSourceIndex = os.path.join(config.dirInterface, "resource", "index.html")
  dirInterfaceName = os.path.join(config.dirInterface, text1 + "-" + text2)
  shutil.copy(dirSourceIndex, dirInterfaceName)
  
  
  
  # Move
  # shutil.copy(config.text1AlignStatisticTei, config.dirInterfaceTei)
  # shutil.copy(config.text2AlignStatisticTei, config.dirInterfaceTei)
  # shutil.copy(config.finalTei, config.dirInterfaceTei)
  # print("Done", "Move dir and files in interface")


"""
makeInterface : création de l'interface
"""

def makeInterface(text1, text2, alignmentName, source, target):
  
  # Recup source data
  with open(source, "r", encoding="utf-8") as file:
    
    # Parsing file
    soup = BeautifulSoup(file, "html.parser")
    
    # Text 1
    version1 = soup.find("text", attrs = {"id" : "version1"})
    version1.name = "div"
    version1.attrs = {}
    
    # Text 2
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
    
    # Add download file
    downloadTEI = soup.find("a", attrs = {"id" : "downloadText1"})
    downloadTEI["href"] = "xml-tei/" + text1 + ".xml"
    downloadTEI = soup.find("a", attrs = {"id" : "downloadText2"})
    downloadTEI["href"] = "xml-tei/" + text2 + ".xml"
    downloadTEI = soup.find("a", attrs = {"id" : "downloadAlignment"})
    downloadTEI["href"] = "xml-tei/" + alignmentName + "_final.xml"
      
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
    print("Done", "Correction interface : ", source)


"""
madkeDataAbsolute : création des données absoilues
"""

def makeDataAbsolute(alignmentName, source, target):
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
    index = [alignmentName]
    columns = ["Insertion", "Suppression", "Remplacement", "Déplacement"]   
    
    # Création du Dataframe
    df = pd.DataFrame(data=data, index=index, columns=columns)
    df = df.transpose()
    
    # Export JSON
    path = os.path.join(target, "dataAbsolute.json")
    df.to_json(path, orient="split")
    print("Done", "Make data absolute JSON : ", path)
    
    # Export CSV
    path = os.path.join(target, "dataAbsolute.tsv")
    df.to_csv(path, sep="\t")
    print("Done", "Make data absolute CSV : ", path)


def makeDataMoyenne(alignmentName, source, target):
  
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
    index = [alignmentName] 
    columns = ["Insertion", "Suppression", "Remplacement", "Déplacement"]   
    
    # Création du Dataframe
    df = pd.DataFrame(data, index=index, columns=columns)
    df = df.transpose()
    
    # Export JSON
    path = os.path.join(target, "dataMoyenne.json")
    df.to_json(path, orient="split")
    print("Done", "Make data moyenne JSON : ", path)
    
    # Export CSV
    path = os.path.join(target, "dataMoyenne.tsv")
    df.to_csv(path, sep="\t")
    print("Done", "Make data moyenne CSV : ", path)


"""
makeDataPersonnage : moyenne for each scripture operation
  @source : tei with 
  @target : json file with data
"""

def makeDataPersonnage(alignmentName, source, target):
  
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
    
    # Export JSON
    path = os.path.join(target, "dataPersonnage.json")
    df.to_json(path, orient="split")
    print("Done", "Make data personnage JSON : ", path)
    
    # Export CSV
    path = os.path.join(target, "dataPersonnage.tsv")
    df.to_csv(path, sep="\t")
    print("Done", "Make data personnage CSV : ", path)
    
  print("Done", "Make data personnage : ", target)

"""
Function principal : fonction principale
"""

def main(text1, text2):
    
  print("")
  print("<><><><><><><>")
  print("<> INTERFACE <>")
  print("<><><><><><><>")
  print("")
  
  # Variable
  alignmentName = text1 + "-" + text2
  finalStatisticTei = os.path.join(config.dirAlignmentTei, text1 + "-" + text2, text1 + "-" + text2 + "_stats-final.xml")
  
  # Create dir
  path = os.path.join(config.dirInterface, text1 + "-" + text2)
  createDir(path)
  
  # Move dir and files in interface
  moveFiles(
    text1=text1,
    text2=text2,
    alignmentName = alignmentName
    )
  
  # Create interface
  finalTei = os.path.join(config.dirAlignmentTei, alignmentName, alignmentName + "_final.xml")
  finalHTML = os.path.join(config.dirInterface, alignmentName, "index.html")
  makeInterface(
    text1=text1,
    text2=text2,
    alignmentName=alignmentName,
    source=finalTei,
    target=finalHTML,
    )
  
  # Correction interface
  correctionInterface(finalHTML)
  
  # Make data absolute
  finalHTML = os.path.join(config.dirInterface, alignmentName, "index.html")
  dataAbsolute = os.path.join(config.dirInterface, alignmentName, "data")
  makeDataAbsolute(
    alignmentName=alignmentName,
    source=finalHTML,
    target=dataAbsolute
    )
  
  # Make data moyenne
  finalHTML = os.path.join(config.dirInterface, alignmentName, "index.html")
  dataMoyenne = os.path.join(config.dirInterface, alignmentName, "data")
  makeDataMoyenne(
    alignmentName=alignmentName,
    source=finalHTML,
    target=dataMoyenne
    )
  
  # Make data personnage
  dataPersonnage = os.path.join(config.dirInterface, alignmentName, "data")
  makeDataPersonnage(
    alignmentName=alignmentName,
    source=finalStatisticTei,
    target=dataPersonnage
    )
  


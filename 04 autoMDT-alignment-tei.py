# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:35:10 2021

@author: Saignol
"""

import config

import os
import shutil
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import nltk
import re

import time
import datetime

"""
On va le traiter le fichier aligné brut
"""

def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)
  print("Done", "Create dir", path)


def normalised(tok):
    list1 = []
    list2 = []
    list3 = []
    for elt in list(tok.partition("-")):
        if elt != "":
            list1.append(elt)
    for elt in list1:
        for elt2 in list(elt.partition("-")):
            if elt2 != "":
                list2.append(elt2)
    for elt in list2:
        for elt2 in list(elt.partition(".")):
            if elt2 != "":
                list3.append(elt2)
    return list3

"""
Tokenization du texte aligné : renvoi une liste de token comportant pour chacun l'annotation en TEI correspondante. Les blocs communs ne sont pas encore traités.
"""

def tokenizeAlign(source):
      
  # Ouverture du fichier
  with open(source, "r", encoding="utf-8") as file:
    
    # On parse le fichier
    tree = etree.parse(file)
    
    # On parcoure le fichier
    tokensAlign = []
    for elt in tree.iter():
      
      # Récupération du type d'annotation
      attribut = str(elt.get("class"))
      ident = str(elt.get("id"))
      
      """
      Gestion des têtes dans les balises
      """
      if elt.text:
        
        # Tokenisation
        tokens = nltk.word_tokenize(elt.text)
        
        # Normaliser la tokenization
        newTokensList = []
        for tok in tokens:
          normList = normalised(tok)
          for norm in normList:
            newTokensList.append(norm)
        
        # Ajouter des balises
        for newToken in newTokensList:
          
          # Gestion des insertions
          if attribut == "span_i":
            if newTokensList.index(newToken) == 0:
              if len(newTokensList) == 1:
                newToken = "<seg type='start' subtype='insertion' ident='" + ident +"'/>" + newToken +  "<seg type='end' subtype='insertion' ident='" + ident +"'/>"
              else:
                newToken = "<seg type='start' subtype='insertion' ident='" + ident +"'/>" + newToken
            else:
              newToken = newToken + "<seg type='end' subtype='insertion' ident='" + ident + "'/>"
          
          # Gestion des suppressions
          if attribut == "span_s":
            if newTokensList.index(newToken) == 0:
              if len(newTokensList) == 1:
                newToken = "<seg type='start' subtype='suppression' ident='" + ident +"'/>" + newToken +  "<seg type='end' subtype='suppression' ident='" + ident +"'/>"
              else:
                newToken = "<seg type='start' subtype='suppression' ident='" + ident +"'/>" + newToken
            else:
              newToken = newToken + "<seg type='end' subtype='suppression' ident='" + ident + "'/>"
          
          # Gestion des remplacements
          if attribut == "span_r":
            if newTokensList.index(newToken) == 0:
              if len(newTokensList) == 1:
                newToken = "<seg type='start' subtype='remplacement' ident='" + ident +"'/>" + newToken +  "<seg type='end' subtype='remplacement' ident='" + ident +"'/>"
              else:
                newToken = "<seg type='start' subtype='remplacement' ident='" + ident +"'/>" + newToken
            else:
              newToken = newToken + "<seg type='end' subtype='remplacement' ident='" + ident + "'/>"
          
          # Gestion des déplacement
          if attribut == "span_d":
            if newTokensList.index(newToken) == 0:
              if len(newTokensList) == 1:
                newToken = "<seg type='start' subtype='deplacement' ident='" + ident +"'/>" + newToken +  "<seg type='end' subtype='deplacement' ident='" + ident +"'/>"
              else:
                newToken = "<seg type='start' subtype='deplacement' ident='" + ident +"'/>" + newToken
            else:
              newToken = newToken + "<seg type='end' subtype='deplacement' ident='" + ident + "'/>"
          
          # Ajout des tokens
          tokensAlign.append(newToken)
      
      """
      Gestion des queux dans les balises
      """
      if elt.tail:
        
        # Tokenisation
        tokens = nltk.word_tokenize(elt.tail)
        
        # Normaliser la tokenization
        newTokensList = []
        for tok in tokens:
          normList = normalised(tok)
          for norm in normList:
            newTokensList.append(norm)
        
        # Ajouter des balises
        for newToken in newTokensList:
          
          # Gestion des insertions
          if attribut == "span_i":
            if newTokensList.index(newToken) == 0:
              if len(newTokensList) == 1:
                newToken = "<seg type='start' subtype='insertion' ident='" + ident +"'/>" + newToken +  "<seg type='end' subtype='insertion' ident='" + ident +"'/>"
              else:
                newToken = "<seg type='start' subtype='insertion' ident='" + ident +"'/>" + newToken
            else:
              newToken = newToken + "<seg type='end' subtype='insertion' ident='" + ident + "'/>"
          
          # Gestion des suppressions
          if attribut == "span_s":
            if newTokensList.index(newToken) == 0:
              if len(newTokensList) == 1:
                newToken = "<seg type='start' subtype='suppression' ident='" + ident +"'/>" + newToken +  "<seg type='end' subtype='suppression' ident='" + ident +"'/>"
              else:
                newToken = "<seg type='start' subtype='suppression' ident='" + ident +"'/>" + newToken
            else:
              newToken = newToken + "<seg type='end' subtype='suppression' ident='" + ident + "'/>"
          
          # Gestion des remplacements
          if attribut == "span_r":
            if newTokensList.index(newToken) == 0:
              if len(newTokensList) == 1:
                newToken = "<seg type='start' subtype='remplacement' ident='" + ident +"'/>" + newToken +  "<seg type='end' subtype='remplacement' ident='" + ident +"'/>"
              else:
                newToken = "<seg type='start' subtype='remplacement' ident='" + ident +"'/>" + newToken
            else:
              newToken = newToken + "<seg type='end' subtype='remplacement' ident='" + ident + "'/>"
          
          # Gestion des déplacement
          if attribut == "span_d":
            if newTokensList.index(newToken) == 0:
              if len(newTokensList) == 1:
                newToken = "<seg type='start' subtype='deplacement' ident='" + ident +"'/>" + newToken +  "<seg type='end' subtype='deplacement' ident='" + ident +"'/>"
              else:
                newToken = "<seg type='start' subtype='deplacement' ident='" + ident +"'/>" + newToken
            else:
              newToken = newToken + "<seg type='end' subtype='deplacement' ident='" + ident + "'/>"
          
          # Ajout des tokens
          tokensAlign.append(newToken)
    
  return tokensAlign


"""
Transferts des Tokens de la version alignée dans la version source
@source : source XML
@tokensAlign : tokens alignés issus de la version précédente
@target : chemin d'écriture du fichier'
"""

def transferToken(source, tokensAlign, target):
      
  # Ouverture du fichier
  with open(source, "r", encoding="utf-8") as file:
    
    # On parse le fichier
    tree = etree.parse(file)
    
    # Suppresion des balises TEI
    for elt in tree.xpath("//tei:teiHeader", namespaces={'tei' : 'http://www.tei-c.org/ns/1.0'}):
      elt.getparent().remove(elt)
    
    # On parcoure le fichier
    tokensSource = []
    allTokens = 0
    for elt in tree.iter():
      
      """
      Gestion des têtes
      """
      # Tête du texte
      if elt.text:
        
        # On tokenize le texte
        tokens = nltk.word_tokenize(elt.text)
        
        # On sépare les tokens et on calcule leur nombre
        newTokensList = []
        nbTokens = 0
        for tok in tokens:
          normList = normalised(tok)
          for norm in normList:
            newTokensList.append(norm)
            nbTokens += 1
        
        # Remplacement des tokens
        elt.text = ""
        start = allTokens
        end = allTokens + nbTokens
        for indice in range(start, end):
          if indice < len(tokensAlign):
            elt.text = elt.text + tokensAlign[indice] + " "
        # On itère
        allTokens += nbTokens
        
        # On ajoute les tokens à la liste finale (utile pour débugger)
        for tok in newTokensList:
          tokensSource.append(tok)
        
      """
      Gestion des queux
      """
      # Gestion des queux
      if elt.tail:
        
        # On tokenize le texte
        tokens = nltk.word_tokenize(elt.tail)
        
        # On sépare les tokens et on calcule leur nombre
        newTokensList = []
        nbTokens = 0
        for tok in tokens:
          normList = normalised(tok)
          for norm in normList:
            newTokensList.append(norm)
            nbTokens += 1
        
        # Remplacement des tokens
        elt.tail = ""
        start = allTokens
        end = allTokens + nbTokens
        for indice in range(start, end):
          if indice < len(tokensAlign):
            elt.tail = elt.tail + tokensAlign[indice] + " "
        # On itère
        allTokens += nbTokens
        
        # On ajoute les tokens à la liste finale (utile pour débugger)
        for tok in newTokensList:
          tokensSource.append(tok)
    
    # Export du fichier
    with open(target, "ab") as file:
      file.write(etree.tostring(tree, encoding="utf-8"))
      print("Done", "Export align TEI", target)
      
    return tokensSource

"""
Multiples corrections pour obtenir document correct du point de vue de la TEI
"""

def correction(source):
  
  
  '''
  Correction des caractères XML
  '''
  
  # Lecture du fichier
  with open(source, "r", encoding="utf-8") as file:
    
    # Application des regex
    linesRaw = file.readlines()
    linesCorr = []
    for line in linesRaw:
      line = re.sub("&lt;", "<", line)
      line = re.sub("&gt;", ">", line)
      linesCorr.append(line)
  
  # Export du fichier
  with open(source, "w+", encoding="utf-8") as file:
    for line in linesCorr:
      file.write(line)
    print("Done", "Correction cararacter XML : ", source)
  
  
  '''
  Suppression des doublons d'annotations dus à la tokenization
  '''
  
  # Lecture du fichier
  with open(source, "r", encoding="utf-8") as file:
    
    # Parser le document
    soup = BeautifulSoup(file, features="lxml")
    
    # Lister identifiants <START>
    identList = []
    for elt in soup.find_all("seg", attrs= {"type" : "start"}):
      identList.append(elt["ident"])
    identList = list(set(identList))
    
    # Supprimer les doublons <START>
    for ident in identList:
      doublonList = soup.find_all("seg", attrs = {"type" : "start", "ident": ident})
      size = len(doublonList)
      if size > 1:
        i = 1
        while i < size:
          doublonList[i].decompose()
          i += 1
      print("Suppression des doublons <START> : ", str(identList.index(ident)) + " / " + str(len(identList)))
    
    # Lister identifiants <END>
    identList = []
    listSegEnd = soup.find_all("seg", attrs = {"type" : "end"})
    for elt in listSegEnd:
      identList.append(elt["ident"])
    identList = list(set(identList))
    
    # Supprimer doublons <END>
    for ident in identList:
      doublonList = soup.find_all("seg", attrs = {"type":"end", "ident" : ident})
      size = len(doublonList)
      for elt in doublonList:
        if doublonList.index(elt) != size - 1: # sauf le dernier doublon de la liste
          elt.decompose()
      print("Suppression des doublons <END> : ", str(identList.index(ident)) + " / " + str(len(identList)))
   
  # Export du résultat
  with open(source, "w+", encoding="utf-8") as file:
    file.write(str(soup))
    print("Done", "Suppression des doublons : ", source)
  
  
  '''
  Passage de REGEX pour corriger le texte d'un point de vue typographique
  '''
  
  # Lecture du fichier
  with open(source, "r+", encoding="utf-8") as file:
    
    # Application des regex
    linesRaw = file.readlines()
    linesCorr = []
    for line in linesRaw:
      line = re.sub(" ’ ", "’", line) # Correction des apostrophes
      line = re.sub(" ,", ",", line) # Correction des traits d'unions
      line = re.sub(" \.", ".", line) # Correction des points
      line = re.sub(" - ", "-", line) # Correction des tirets
      line = re.sub("\( ", "(", line) # Correction des parenthèses ouvrantes
      line = re.sub(" \)", ")", line) # Correction des parenthèses fermantes
      linesCorr.append(line)
  
  # Export du fichier
  with open(source, "w+", encoding="utf-8") as file:
    for line in linesCorr:
      file.write(line)
    print("Done", "Corrections typographiques : ", source)


"""
fusionTei : associe les deux textes dnas un unique fichier tei interprétable dans l'interface
@text1 : texte 1 aligné en XML-TEI
@text2 ! texte 2 aligné en XML-TEI
@target : fichier final en XML-TEI
"""

def fusionTei(text1, text2, target):
  
  # Lecture du text 1
  with open(text1, "r+", encoding="utf-8") as file:
    soup = BeautifulSoup(file, features="lxml")
    align1 = soup.find("text")
  
  # Lecture du text 2
  with open(text2, "r+", encoding="utf-8") as file:
    soup = BeautifulSoup(file, features="lxml")
    align2 = soup.find("text")
  
  # Fusion des deux fichiers en suivant syntaxe de la TEI
  with open(target, "w+", encoding="utf-8") as file:
    
    # Ajout de la balise TEI
    tei = soup.new_tag("TEI")
    tei["xmlns"] = "http://www.tei-c.org/ns/1.0"
    
    # Ajout de la balise TeiHeader
    teiHeader = soup.new_tag("teiHeader")
    tei.append(teiHeader)
    
    # Ajout de la balise Body
    body = soup.new_tag("body")
    tei.append(body)
    
    # Ajout du texte 1
    text1 = soup.new_tag("text")
    text1["id"] = "version1"
    text1.append(align1)
    body.append(text1)
    
    # Ajout du texte 2
    text2 = soup.new_tag("text")
    text2["id"] = "version2"
    text2.append(align2)
    body.append(text2)
    
    # Écriture des modifications
    file.write(str(tei))
    print("Done", "Fusion TEI : ", target)

"""
main : function principal
"""

def main():
  
  print("")
  print("<><><><><><><><><>")
  print("<> ALIGNMENT TEI <>")
  print("<><><><><><><><><>")
  print("")
  
  # Temps de départ
  startTime = time.time()
  
  # Création du fichier de sortie
  createDir(config.dirAlignmentTeiName)
  
  # Alignement tei text 1
  tokens1Align = tokenizeAlign(config.text1AlignRaw)
  transferToken(config.text1Source, tokens1Align, config.text1AlignTei)
  correction(config.text1AlignTei)
  
  # Alignement tei text 2
  tokens2Align = tokenizeAlign(config.text2AlignRaw)
  tokenSource = transferToken(config.text2Source, tokens2Align, config.text2AlignTei)
  correction(config.text2AlignTei)
  
  # debuggage
  # df = pd.DataFrame(list(zip(tokenSource, tokens2Align)), columns =["tokensSource", "tokens2Align"])
  # path = os.path.join(config.dirAlignmentTeiName, "test.csv")
  # df.to_csv(path, sep="\t")
  
  # Fusion des deux textes
  fusionTei(config.text1AlignTei, config.text2AlignTei, config.finalTei)
  
  # Calcul de la durée du programme
  endTime = time.time()
  intervalTime = str(datetime.timedelta(seconds=endTime - startTime))
  print("Durée d'exécution du programme", intervalTime)
    
main()
  
  
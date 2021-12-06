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
from lxml import etree

import time
import datetime



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
getTokens : récupérer les tokens pour un fichier donné avec l'étape de la normalisation
"""

def getTokens(path):
  with open(path, "r+", encoding="utf-8") as file:
    
    tokensList = []
    
    # Parse file
    tree = etree.parse(file)
    
    # Check file
    for elt in tree.iter():
      
      if elt.text:
        tokens = nltk.word_tokenize(elt.text)
        
        # Normalise tokenisation
        newTokensList = []
        for tok in tokens:
          normList = normalised(tok)
          for norm in normList:
            newTokensList.append(norm)
            
        for token in newTokensList:
          tokensList.append(token)
        
      if elt.tail:
        tokens = nltk.word_tokenize(elt.tail)
        
        # Normalise tokenisation
        newTokensList = []
        for tok in tokens:
          normList = normalised(tok)
          for norm in normList:
            newTokensList.append(norm)
        
        for token in newTokensList:
          tokensList.append(token)
  
    print("Done", "Get tokens : " + path)
  return tokensList


"""
main : principal function
"""

def main(text1, text2):
  
  print("")
  print("<><><><><><><><><><><><><>")
  print("<> CORRECTION ALIGNMENT <>")
  print("<><><><><><><><><><><><><>")
  print("")
  
  # Alignment name
  alignmentName = text1 + "-" + text2
  
  # # List de tokens
  text1Source = os.path.join(config.dirCorpusTei, text1 + ".xml")
  tokens1Source = getTokens(text1Source)
  
  text1AlignRaw = os.path.join(config.dirAlignmentRaw, alignmentName, text1 + ".xml")
  tokens1AlignRaw = getTokens(text1AlignRaw)
  
  text2Source = os.path.join(config.dirCorpusTei, text2 + ".xml")
  tokens2Source = getTokens(text2Source)
  
  text2AlignRaw = os.path.join(config.dirAlignmentRaw, alignmentName, text2 + ".xml")
  tokens2AlignRaw = getTokens(text2AlignRaw)
  
  # Correct dataframe size
  mylist = [tokens1Source, tokens1AlignRaw, tokens2Source, tokens2AlignRaw]
  maxSize = max(len(lst) for lst in mylist)
  for lst in mylist:
    while len(lst) < maxSize:
      lst.append("")
  print("Done", "Correct dataframe size")
  
  # Create dataframe
  df = pd.DataFrame(list(zip(tokens1Source, tokens1AlignRaw, tokens2Source, tokens2AlignRaw)), columns =["tokens1Source", "tokens1AlignRaw", "tokens2Source", "tokens2AlignRaw"])
  
  # Looping dataframe
  problem1 = ""
  problem2 = ""
  for index, row in df.iterrows():
    if row["tokens1Source"] != row["tokens1AlignRaw"]:
      if problem1 == "":
        problem1 = index
    if row["tokens2Source"] != row["tokens2AlignRaw"]:
      if problem2 == "":
        problem2 = index
        
  if problem1 == "" and problem2 == "":
    print("")
    print("\t" + "<><><><><><><><><><><><><>")
    print("\t" + "<><> There is no bug ! <><>")
    print("\t" + "<><><><><><><><><><><><><>")
    print("")
  else:
    if problem1 != "":
      print("")
      print("\t" + "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
      print("\t" + "<><> There is a bug in '" + text1 + "' alignment : check token " + str(problem1) + " <><>")
      print("\t" + "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
      print("")
    
    if problem2 != "":
      print("")
      print("\t" + "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
      print("\t" + "<><> There is a bug in '" + text2 + "' alignment : check token " + str(problem2) + " <><>")
      print("\t" + "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
      print("")
  
  # Export dataframe
  path = os.path.join(config.dirAlignmentRaw, alignmentName, "alignmentCorr.tsv")
  df.to_csv(path, sep="\t")
  print("Done", "Export Dataframe : ", path)
  
  
  
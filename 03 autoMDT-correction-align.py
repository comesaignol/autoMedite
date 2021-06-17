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
    soup = BeautifulSoup(file, features="lxml")
    
    # Extraction des données textuelles
    if soup.find("text"):
      text = soup.find("text").get_text()
    else:
      text = soup.get_text()
      
    # Tokenization
    tokens = nltk.word_tokenize(text)
    
    # Normaliser la tokenization
    newTokens = []
    for tok in tokens:
      normList = normalised(tok)
      for norm in normList:
        newTokens.append(norm)
  
    print("Done", "Get tokens : " + path)
  return newTokens


"""
main : principal function
"""

def main():
  
  print("")
  print("<><><><><><><><><><><><><>")
  print("<> CORRECTION ALIGNMENT <>")
  print("<><><><><><><><><><><><><>")
  print("")
  
  # List de tokens
  tokens1Source = getTokens(config.text1Source)
  tokens1AlignRaw = getTokens(config.text1AlignRaw)
  tokens2Source = getTokens(config.text2Source)
  tokens2AlignRaw = getTokens(config.text2AlignRaw)
  
  # Correct dataframe size
  mylist = [tokens1Source, tokens1AlignRaw, tokens2Source, tokens2AlignRaw]
  maxSize = max(len(lst) for lst in mylist)
  for lst in mylist:
    while len(lst) < maxSize:
      lst.append("")
  print("Done", "Correct dataframe size")
  
  # Create dataframe
  df = pd.DataFrame(list(zip(tokens1Source, tokens1AlignRaw, tokens2Source, tokens2AlignRaw)), columns =["tokens1Source", "tokens1AlignRaw", "tokens2Source", "tokens2AlignRaw"])
  
  # Export dataframe 
  df.to_csv(config.correctionAlign, sep="\t")
  print("Done", "Export Dataframe : ", config.correctionAlign)
  
  
  
"""
Command
"""
    
main()
  
  
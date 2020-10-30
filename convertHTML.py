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
import glob
import shutil

# Librairie Data Science
from bs4 import BeautifulSoup
import pandas as pd

############
### MAIN ###
############  

def main():
  pathList = os.path.join(config.dirOutput,"*.html")
  fileList = glob.glob(pathList)

  for file in fileList:
    
    # Modification du HTML
    with open(file, "r", encoding="utf-8") as fichier:
      # Parser le document
      soup = BeautifulSoup(fichier, features="lxml")
      
      # Changer feuille de style
      style = soup.find('link', attrs = {'rel' : 'stylesheet'})
      style['href'] = '../css/style.css'
      
      ############################
      ### AJOUT DES LIBRAIRIES ###
      ############################
      
      # Librairie Bootstrap
      bootstrap = soup.new_tag("link")
      bootstrap["rel"] = "stylesheet"
      bootstrap["href"] = "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
      bootstrap["integrity"] = "sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
      bootstrap["crossorigin"] = "anonymous"
      style.insert_before(bootstrap)
      
      # Librairie CHART JS
      chart = soup.new_tag("script")
      chart["src"] = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"
      
      ####################################
      ### Ajouter colonne de bootstrap ###
      ####################################
      
      # Suppression des informations complémentaires (modal)
      soup.find("div", id="modal-content").decompose()
      soup.find("div", id="browser-detection-info").decompose()
      soup.find("div", id="button_box").decompose()
      soup.find("div", id="modifications").decompose()
      
      # Container
      eltContainer = soup.find("div", attrs = {"id" : "container"})
      eltContainer["class"] = "container-fluid h-100 d-flex flex-column"
      
      # Row
      eltRow = soup.find("div", attrs = {"id" : "windows"})
      eltRow["class"] = "row flex-fill"
      eltRow["style"] = "min-height:0;"
      
      # Colonne de gauche
      eltColLeft = soup.find("div", attrs = {"class" : "txt_container left"})
      eltColLeft["class"] = "col-4 border mh-100 order-1"
      
      # Colonne du milieu
      eltColCenter = soup.find("div", attrs = {"class" : "txt_container right"})
      eltColCenter["class"] = "col-4 border mh-100 order-2"
      
      # Colonne de droite
      eltColRight = soup.new_tag("div")
      eltColRight.append("Lorem ipsum")
      eltColRight["class"] = "col-4 border mh-100 order-3"
      eltColRight["id"] = "test"
      eltColCenter.insert_after(eltColRight)
      
      ####################################
      ### GESTION DES DATAS ###
      ####################################
      
      def makeData(name):
        i = 0
        eltList = soup.find_all("span", attrs = {"class" : name})
        for elt in eltList:
          i = i + len(elt)
        return i
      
      dataList = ["span_i", "span_c", "span_r", "span_d"]
      dataResult = []
      
      for elt in dataList:
        dataResult.append(makeData(elt))
      
      print(dataResult)
    
    # Sauvegarde du HTML
    with open(file, "wb") as fichier:
      fichier.write(soup.prettify("utf-8"))
      print("done")
      
main()
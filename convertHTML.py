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

def createDirJson():
  path = os.path.join(config.dirCurrent,"ressource/json")
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)
  
def createDirFile(name):
  path = os.path.join(config.dirCurrent,"ressource/json", name)
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)

def main():
  
  # Création du dossier ressource
  createDirJson()
  
  # Traitement de chaque fichier
  pathList = os.path.join(config.dirOutput,"*.html")
  fileList = glob.glob(pathList)
  for file in fileList:
    
    # Modification du HTML
    with open(file, "r", encoding="utf-8") as fichier:
      # Parser le document
      soup = BeautifulSoup(fichier, features="lxml")
      
      ############################
      ### AJOUT DES LIBRAIRIES ###
      ############################
      
      # Suppression des vieilles librairies
      for elt in soup.find_all("script"):
        elt.decompose()  
      for elt in soup.find_all("link"):
        elt.decompose()
      
      # Titre du document
      title = soup.find("title")
      
      # Style CSS
      css = soup.new_tag("link")
      css["rel"] = "stylesheet"
      css["href"] = "../ressource/css/style.css"
      title.insert_after(css)
      
      # Librairie Bootstrap
      bootstrap = soup.new_tag("link")
      bootstrap["rel"] = "stylesheet"
      bootstrap["href"] = "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
      bootstrap["integrity"] = "sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
      bootstrap["crossorigin"] = "anonymous"
      css.insert_after(bootstrap)
      
      # Librairie JQUERY
      jquery = soup.new_tag("script")
      jquery["src"] = "https://code.jquery.com/jquery-3.5.1.min.js"
      jquery["integrity"] = "sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
      jquery["crossorigin"] = "anonymous"
      bootstrap.insert_after(jquery)
      
      # Librairie CHART JS
      chart = soup.new_tag("script")
      chart["src"] = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"
      jquery.insert_after(chart)
      
      # Script JS
      js = soup.new_tag("script")
      js["type"] = "text/javascript"
      js["src"] = "../ressource/js/script.js"
      chart.insert_after(js)
      
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
      eltColRight["class"] = "col-4 border mh-100 order-3"
      eltColRight["id"] = "test"
      
      canvas = soup.new_tag("canvas")
      canvas["id"] = "dataVizCar"
      
      eltColRight.append(canvas)
      
      eltColCenter.insert_after(eltColRight)
      
      ####################################
      ### GESTION DES DATAS ###
      ####################################
      
      
      # Création du dossier json correspondant au nom du fichier
      fileName = os.path.splitext(os.path.basename(file))[0]
      createDirFile(fileName)
      
      def makeDataCar(name):
        i = 0
        eltList = soup.find_all("span", attrs = {"class" : name})
        for elt in eltList:
          i = i + len(elt)
        return i
      
      # Création des datas
      balise = ["span_c", "span_i", "span_s", "span_r", "span_d"]
      data = []
      for elt in balise:
        data.append(makeDataCar(elt))
      data = [data]
      
      # Création des labels
      label = ["Communs", "Insertion", "Suppression", "Remplacement", "Déplacement"]
      
      # Création du Dataframe
      df = pd.DataFrame(data, columns=label)
      
      # Export Json
      pathJson = os.path.join(config.dirCurrent,"ressource/json", fileName, "datavizCar.json")
      df.to_json(pathJson, orient="records", force_ascii=False)
    
    # Sauvegarde du HTML
    with open(file, "wb") as fichier:
      fichier.write(soup.prettify("utf-8"))
      print("done")
      
main()
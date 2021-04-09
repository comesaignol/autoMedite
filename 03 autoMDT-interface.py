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

############
### MAIN ###
############  
  
def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)
  print("Done", "Création du dossier", path)


"""
Création de l'interface pour consulter les résultats de l'interface
"""

def main():
  
  # Lecture du fichier alignement
  df = pd.read_csv("relation.tsv", sep='\t', header=0)
  
  # Lancement du programme pour chaque alignement
  for i in range(len(df)):
    
    print("<><><><><><><><><>")
    print("<> ALIGNMENT " + str(i+1) + " <>")
    print("<><><><><><><><><>")
    
    # Création du nom de fichier
    alignmentName = df.loc[i, "Alignement"]
   
    # Création du dossier de sortie
    alignmentDir = os.path.join(config.dirOutputInterface, alignmentName)
    createDir(alignmentDir)
    
    # Création du dossier data
    dirData = os.path.join(alignmentDir, "data")
    createDir(dirData)
    
    # Création du dossier ressource
    dirRessource = os.path.join(alignmentDir, "ressource")
    createDir(dirRessource)
    
    # Déplace les fichiers ressources
    shutil.copy(config.dirSourceCSS, dirRessource)
    shutil.copy(config.dirSourceJS, dirRessource)
      
    # Modification du HTML
    path = os.path.join(config.dirOutputAlignment, alignmentName, alignmentName + ".html")
    with open(path, "r", encoding="utf-8") as file:
      
      # Parser le document
      soup = BeautifulSoup(file, features="lxml")
      
      ##############################
      ### GESTION DU HEADER HTML ###
      ##############################
      
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
      css["href"] = "ressource/style.css"
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
      js["src"] = "ressource/script.js"
      chart.insert_after(js)
      
      # Déclencher script
      script = soup.new_tag("script")
      script.append("createDatavizCar('" + alignmentName + "');")
      body = soup.find("body")
      body.insert_after(script)
      
      ############################
      ### GESTION DU MAIN HTML ###
      ############################
      
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
      eltColRight = soup.new_tag("div", attrs = {"id" : "test"})
      eltColRight["class"] = "col-4 border mh-100 order-3"
      
      canvas = soup.new_tag("canvas")
      canvas["id"] = "dataVizCar"
      canvas["height"] = "50px"
      canvas["width"] = "50px"
      
      eltColRight.append(canvas)
      
      eltColCenter.insert_after(eltColRight)
      
      #########################
      ### GESTION DES DATAS ###
      #########################
      
      def makeDataAbsolute(name):
        j = 0
        eltList = soup.find_all("span", attrs = {"class" : name})
        for elt in eltList:
          j = j + len(elt.string)
        return str(j)
      
      # Création des datas
      data = []
      balise = ["span_c", "span_i", "span_s", "span_r", "span_d"]
      for elt in balise:
        data.append(makeDataAbsolute(elt))
      data = [data]
      
      # Création des labels
      label = ["Communs", "Insertion", "Suppression", "Remplacement", "Déplacement"]
      
      # Création du Dataframe
      df2 = pd.DataFrame(data, columns=label)
      
      # Export Data Json
      path = os.path.join(dirData, "datavizCar.json")
      df2.to_json(path, orient="records", force_ascii=False, lines=True)
    
    # Sauvegarde du HTML
    path = os.path.join(alignmentDir, alignmentName + ".html")
    with open(path, "wb") as fichier:
      fichier.write(soup.prettify("utf-8"))
      print("Done", "Création de l'interface", path)
    soup = ""
    
main()
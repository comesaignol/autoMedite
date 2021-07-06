# -*- coding: utf-8 -*-

import os

# Name
text1 = "1654"
text2 = "1878"
alignmentName = text1 + "-" + text2
urlMEDITE = "http://obvil.lip6.fr/medite/"

# Paramètre du corpus
dirCorpus = os.path.abspath("corpus")
text1Source = os.path.join(dirCorpus, text1 + ".xml")
text2Source = os.path.join(dirCorpus, text2 + ".xml")

# Paramètre pour l'alignement raw
dirAlignmentRaw = os.path.abspath("alignment-raw")
dirAlignmentRawName = os.path.join(dirAlignmentRaw, alignmentName)
alignmentRawHTML = os.path.join(dirAlignmentRaw, alignmentName, alignmentName + "_raw.html")
text1AlignRaw = os.path.join(dirAlignmentRaw, alignmentName, text1 + "_raw.xml")
text2AlignRaw = os.path.join(dirAlignmentRaw, alignmentName, text2 + "_raw.xml")

# Paramètre pour correction-align
correctionAlign = os.path.join(dirAlignmentRaw, alignmentName, alignmentName + "_correction-align.csv")

# Paramètre pour alignment-tei
dirAlignmentTei = os.path.abspath("alignment-tei")
dirAlignmentTeiName = os.path.join(dirAlignmentTei, alignmentName)
text1AlignTei = os.path.join(dirAlignmentTei, alignmentName, text1 + "_tei.xml")
text2AlignTei = os.path.join(dirAlignmentTei, alignmentName, text2 + "_tei.xml")
finalTei = os.path.join(dirAlignmentTei, alignmentName, alignmentName + "_tei-final.xml")

text1AlignStatisticTei = os.path.join(dirAlignmentTei, alignmentName, text1 + "_tei-stat-final.xml")
text2AlignStatisticTei = os.path.join(dirAlignmentTei, alignmentName, text2 + "_tei-stat-final.xml")
finalStatisticTei = os.path.join(dirAlignmentTei, alignmentName, alignmentName + "_tei-stat-final.xml")


# Paramètre des dossiers pour l'interface
dirSourceIndex = os.path.abspath("resource/index.html")

dirSourceCSS = os.path.abspath("resource/css")
dirSourceJS = os.path.abspath("resource/js")

dirInterface = os.path.abspath("interface")
dirInterfaceName = os.path.join(dirInterface, alignmentName)
dirInterfaceTei = os.path.join(dirInterface, alignmentName, "xml-tei")
dirInterfaceData = os.path.join(dirInterface, alignmentName, "data")
dirInterfaceCSS = os.path.join(dirInterface, alignmentName, "css")
dirInterfaceJS = os.path.join(dirInterface, alignmentName, "js")
dirInterfaceTemplate = os.path.join(dirInterface, alignmentName, "template")

finalHTML = os.path.join(dirInterface, alignmentName, "index.html")

# Paramètre pour les statistiques
dataAbsoluteCSV = os.path.join(dirInterface, alignmentName, "data/dataAbsolute.json")
dataMoyenneCSV = os.path.join(dirInterface, alignmentName, "data/dataMoyenne.json")
dataPersonnageCSV = os.path.join(dirInterface, alignmentName, "data/dataPersonnage.json")

# Liste des balises TEI
eltBlock = ["speaker", "sp", "div1", "div2", "head", "castlist", "castitem", "stage", "l"]
eltInline = ["front", "role", "foreign", "hi", "title", "persName"]
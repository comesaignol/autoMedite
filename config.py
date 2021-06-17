# -*- coding: utf-8 -*-

import os

# Name
text1 = "1654"
text2 = "1899"
alignmentName = text1 + "-" + text2
urlMEDITE = "http://obvil.lip6.fr/medite/"

# Paramètre du corpus
dirCorpus = os.path.abspath("corpus")
text1Source = os.path.join(dirCorpus, text1 + ".xml")
text2Source = os.path.join(dirCorpus, text2 + ".xml")

# Paramètre pour l'alignement raw
dirAlignmentRaw = os.path.abspath("alignment-raw")
dirAlignmentRawName = os.path.join(dirAlignmentRaw, alignmentName)
alignmentRawHTML = os.path.join(dirAlignmentRaw, alignmentName, alignmentName + "_align-raw.html")
text1AlignRaw = os.path.join(dirAlignmentRaw, alignmentName, text1 + "_align-raw.xml")
text2AlignRaw = os.path.join(dirAlignmentRaw, alignmentName, text2 + "_align-raw.xml")

# Paramètre pour correction-align
correctionAlign = os.path.join(dirAlignmentRaw, alignmentName, alignmentName + "_correction-align.csv")

# Paramètre pour alignment-tei
dirAlignmentTei = os.path.abspath("alignment-tei")
dirAlignmentTeiName = os.path.join(dirAlignmentTei, alignmentName)
text1AlignTei = os.path.join(dirAlignmentTei, alignmentName, text1 + "_align-tei.xml")
text2AlignTei = os.path.join(dirAlignmentTei, alignmentName, text2 + "_align-tei.xml")
finalTei = os.path.join(dirAlignmentTei, alignmentName, alignmentName + "_align-tei.xml")

# Paramètre des dossiers pour l'interface
dirSourceCSS = os.path.abspath("resource/style.css")
dirSourceJS = os.path.abspath("resource/script.js")
dirSourceHTML = os.path.abspath("resource/interface.html")
dirInterface = os.path.abspath("interface")
dirInterfaceName = os.path.join(dirInterface, alignmentName)
dirInterfaceData = os.path.join(dirInterface, alignmentName, "data")
dirInterfaceResource = os.path.join(dirInterface, alignmentName, "resource")
finalHTML =  os.path.join(dirInterface, alignmentName, "interface.html")
dataAbsoluteCSV = os.path.join(dirInterface, alignmentName, "data/dataAbsolute.json")

# Liste des balises TEI
eltBlock = ["speaker", "sp", "div1", "div2"]
eltInline = ["foreign", "hi", "title", "persName"]
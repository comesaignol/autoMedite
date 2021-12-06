# -*- coding: utf-8 -*-

import os

# Name
urlMEDITE = "http://obvil.lip6.fr/medite/"

# Paramètre
dirCorpusTei = os.path.abspath("../data/corpus-tei")
dirCorpusRaw = os.path.abspath("../data/corpus-raw")
dirAlignmentRaw = os.path.abspath("../data/alignment-raw")
dirAlignmentTei = os.path.abspath("../data/alignment-tei")
dirInterface = os.path.abspath("../interface")

# Liste des balises TEI
eltBlock = ["speaker", "sp", "div1", "div2", "head", "castlist", "castitem", "stage", "l"]
eltInline = ["front", "role", "foreign", "hi", "title", "persName"]



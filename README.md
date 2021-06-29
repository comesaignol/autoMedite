# Introduction

AutoMEDITE est un ensemble de modules développés en Python 3 approfondissant les résultats obtenus par MEDITE, un logiciel d’alignement textuel comparant automatiquement deux versions d’une même œuvre.

Là où MEDITE offre une première exploration des corpus, AutoMEDITE rend les résultats de l’alignement interopérables en proposant une interface d’édition et de recherche utile pour les chercheurs. En ce sens, AutoMEDITE est une surcouche applicative au logiciel MEDITE.

Le tableau suivant compare leurs fonctionnalités  :

| Fonctions                                | MEDITE | AutoMEDITE |
|------------------------------------------|--------|------------|
| Exploration de corpus                    | +      | +          |
| Alignement au format brut (TXT)          | +      | +          |
| Alignement au format structuré (XML-TEI) | -      | +          |
| Interface locale                         | -      | +          |
| Outil d'édition de texte                 | -      | +          |
| Statistiques dynamiques                  | -      | +          |

# Démo

Vous souhaitez intégrer AutoMEDITE dans votre projet ? Explorez rapidement vos corpus textuels ? Le code source est disponible au téléchargement à l’adresse suivante :  https://github.com/comesaignol/autoMedite.

Une fois le dossier téléchargé et décompressé, vous obtiendrez le répertoire suivant :

        autoMedite/
        ├── alignment-raw/
        ├── alignment-tei/
        ├── corpus/
        ├── demo/
        ├── interface/
        ├── resource/
        │01 autoMDT-xml2txt
        │02 autoMDT-alignment-raw.py
        │03 autoMDT-correction-align.py
        │04 autoMDT-alignment-tei.py
        │05 autoMDT-interface.py
        │config.py
        │geckodriver.log
        │README.md
        │requirements.txt

Le moyen le plus simple pour tester l’interface est d’installer le répertoire « demo » dans un serveur local configuré avec la dernière version de PHP. L’interface peut ensuite être consultée à l’adresse suivante :

    http://localhost/autoMedite/demo/index.php

# Contenus

AutoMedite se fonde sur une série de modules Python gérant les différentes étapes de l’alignement textuel dans un contexte de textes structurés. Ils sont à utiliser successivement, on en trouvera ci-dessous une rapide présentation :

* **01 autoMDT-xml2txt.py**. Module convertissant les fichiers XML-TEI au formats TXT ;
* **02 autoMDT-alignment-raw.py**. Module utilisant automatiquement MEDITE et récupérant les résultats au format HTML ;
* **03 autoMDT-correction-align.py**. Module de débogage accompagnant l’utilisateur à la correction de l’alignement issu de MEDITE ;
* **04 autoMDT-alignment-tei.py**. Module transférant les résultats de l’alignement de MEDITE dans les fichiers XML-TEI de départ ;
* **05 autoMDT-interface.py**. Module générant à partir des fichiers XML-TEI alignés une interface de consultation locale et les données statistiques ;

Ces modules sont accompagnés de fichiers de configuration et d’installation :

* **config.py**. Fichier de configuration fournissant pour chacun des modules les chemins relatifs des fichiers ;
* **geckodriver.log**. Fichier permettant d’utiliser à distance le navigateur web Mozilla ;
* **README.md**. Fichier de documentation présentant le projet ;
* **requirements.txt**. Fichier listant les librairies python à installer ;

# Installation et utilisation

De manière générale, l’utilisation d’AutoMedite nécessite l’installation :

1. D’un serveur local de type WAMP ou MAMP suivant votre OS ;
2. D’un IDE Python 3 avec les libraires présentées dans **requirements.txt**.
3. Du navigateur web Mozilla Firefox ;
4. Du fichier **geckodriver.log** installés à la racine de votre installation Python.

Il est ensuite nécessaire de copierez-collez les fichiers XML-TEI utilisés pour l’alignement dans le répertoire « corpus ».

Puis, les variables « text1 » et « text2 » du fichier **config.py**  seront édités avec le nom exact des fichiers sans leurs extensions. Par défaut, ils sont notés avec les fichiers fournis en démo :

    text1 = "1654"
    text2 = "1878"
    

## 01 autoMDT-xml2txt.py

### Présentation

**01 autoMDT-xml2txt.py** est un module convertissant les fichiers XML-TEI que l’on souhaite aligner en fichier au formats TXT. Ce sont ces derniers qui sont utilisés pour l’alignement dans MEDITE, ils sont générés dans le dossier « corpus » au côté des fichiers XML-TEI source.

### Utilisation

L’utilisation de **01 autoMDT-xml2txt.py** ne nécessite pas de configuration particulière.

## 02 autoMDT-alignment-raw.py

### Présentation

**02 autoMDT-alignment-raw.py** est un module utilisant à distance le logiciel MEDITE : il récupère les résultats bruts de l’alignement au format HTML en supprimant une partie des annotations HTML superflus et en séparant les textes dans deux fichiers XML distincts.

Les résultats de l’alignement sont alors enregistrés dans le répertoire « alignment-raw ».

### Utilisation

**02 autoMDT-alignment-raw.py**nécessite l’installation du fichier **geckodriver.log** à la racine du répertoire d’installation de Python. Il est nécessaire afin de faire fonctionner à distance le navigateur web Mozilla Firefox.

Dans l’état actuel du développement, **02 autoMDT-alignment-raw.py**autorise le passage des quatre principaux paramètres de MEDITE : 

1. **casse**. Sélectionne le paramètre « Sensible à la casse » ;
2. **separator**. Sélectionne le paramètre « Sensible aux séparateurs » ;
3. **diacritique**.  Sélectionne le paramètre « Sensible aux signes diacritiques (éêçè...) » ;
4. **word**. Sélectionne le paramètre « Algorithme mots (cochée) ou caractères (non cochée) » ;

Par exemple, la commande par défaut sélectionne seulement l’algorithme « mot ».

    main(casse=False, separator=False, diacritique=False, word=True)

Pour modifier les paramètres de l’alignement, changer le booléens « False » par « True ».

## 03 autoMDT-correction-align.py

### Présentation

**03 autoMDT-correction-align.py** est un module de débogage accompagnant l’utilisateur à la correction des résultats de l’alignement. En effet, MEDITE ajoute ponctuellement de nouveaux blocs de texte absents des fichiers sources dans les textes alignés. Ces blocs doivent être supprimés afin de permettre le transfert des annotations dans les fichiers XML-TEI de départ.

Le module génère un fichier CSV dans le répertoire « alignment-raw » qui comporte, pour chacune des versions, la liste des textes tokenisés. Dans le cas où un décalage se produit dans la liste des tokens, signe qu’un bloc de texte a été ajouté, une correction manuelle est rendue nécessaire dans les fichiers XML présents« alignment-raw ».

Sans cette étape cruciale, l’application des modules ultérieurs prennent le risque d’être défectueuses.

### Utilisation

L’utilisation de **03 autoMDT-correction-align.py** ne nécessite pas de configuration particulière.

## 04 autoMDT-alignment-tei.py

### Présentation

**04 autoMDT-alignment-tei.py** est un module reportant les résultats de l’alignement de MEDITE  présents dans « alignment-raw » dans les fichiers XML-TEI. Le processus est rendu possible grâce à une tokenization des textes qui génère deux types de fichiers :

* Des fichiers XML valide du point de vue de la TEI : les annotations y sont notées à l’aide de balises auto-fermantes. Le nom de fichier comporte le suffixe **tei** ;
* Des fichiers XML utiles pour les statistiques : chaque tokens est annoté à l’aide d’une balise dédiée. Le nom de fichier comporte le suffixe **tei_stat** ;

Chacun de ces fichiers est enregistré dans le répertoire « alignment-tei ».

### Utilisation

L’utilisation de **04 autoMDT-alignment-tei.py** ne nécessite pas de configuration particulière.

## 05 autoMDT-interface.py

### Présentation

**05 autoMDT-interface.py** est un module générant à partir des fichiers XML-TEI alignés une interface de consultation locale accompagnée de nombreux fichiers statistiques. Cette interface est créée à partir des fichiers PHP, JS, CSS présents dans le répertoire « resource ».

L’exécution du module entraîne la création d’une interface indépendante dans le répertoire « interface ». Pour la consulter, ouvrez le fichier  **index.php** dans le navigateur de votre choix à l’aide d’un serveur local.

### Utilisation

L’utilisation de **05 autoMDT-interface.py** ne nécessite pas de configuration particulière.


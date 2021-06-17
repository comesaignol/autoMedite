# autoMedite

## Introduction

AutoMedite est un ensemble de modules développés en Python 3 permettant le téléchargement et l’alignement automatique de deux versions d’une même œuvre à partir du logiciel MEDITE utilisable à cette adresse : http://obvil.lip6.fr/medite/.

Si la version en ligne propose déjà la comparaison des variantes, AutoMedite approfondie ces fonctionnalités de plusieurs manières :

*  **Gestion des fichiers par lots**. Là où Médite propose l’alignement de deux versions d’une même œuvre, AutoMedite réalise successivement plusieurs alignement à partir d’une liste établie en amont.
*  **Gestion des XML**. Alors que Médite propose uniquement le traitement de fichiers TXT en amont, AutoMedite reporte les annotations TXT dans le fichier XML de départ.
*  **Interface de lecture**. AutoMedite propose enfin une interface de lecture des alignement en local permettant l’étude des textes au cours de sessions de travail.

## Structure du dossier

Ce répertoire comporte plusieurs modules à utiliser successivement ou de manière indépendante :

1. **autoMDT-xml2txt.py**. Module convertissant un fichier XML en TXT, utile si les documents du corpus sont au format XML-TEI par exemple.
2. **autoMDT-alignment-raw.py**. Module réalisant automatiquement les alignements listés dans un fichier CSV.
3. **autoMDT-alignment-tei.py**. Module réalisant automatiquement les alignements listés dans un fichier CSV.
4. **autoMDT-interface.py**. Module générant pour chaque alignement une interface web locale.

Le répertoire comporte aussi plusieurs fichiers nécessaires à  l’installation et la configuration des modules :
* **config.py**. Fichier de configuration comportant la liste de paramètres utilisés par chaque module.
* **relation.csv**. Fichier listant les paires d’alignements qu’AutoMedite réalise.
* **requiremnts.txt**. Fichier listant la liste des packages utilisés.
* **ressource**. Dossier comportant les fichiers CSS et JS pour l’interface locale.

## Installation des librairies

AutoMedite nécessite une installation Python 3 avec plusieurs package décrits dans **requirements.txt**.

Pour vérifier les packages installées :

    pip freeze
    
Pour installer les packages manquants :

    pip install -r path\to\requirements.txt
    
avec le chemin absolu correspondant au fichier **requirements.txt** présent dans cet outil.

## autoMDT-xml2txt.py

### Pré-requis

**autoMDT-xml2txt.py** ne nécessite pas de pré-requis.

### Usage

Le fichier « relation.csv » doit d’abord être être configuré avec les noms de fichiers que l’on souhaite convertir. Pour cela, insérer dans les colonnes « État 1 » et « État 2 », les noms des fichiers sans l’extension.

L’exécution du module entraîne la conversion des fichier XML en TXT dans le répertoire « corpus ».

## autoMDT-alignment.py

### Pré-requis

**autoMDT-alignment.py** nécessite l’installation du driver Mozilla Firefox pour fonctionner correctement. Ce fichier permet en effet d’activer à distance le navigateur qui sera utilisé pour aligner successivement les versions listées dans le fichier « relation.csv ».

* Télécharger geckodriver en fonction de votre version de Mozilla : https://github.com/mozilla/geckodriver/releases
* Copier-coller geckodriver dans le répertoire d’installation d’Anaconda C:\\ProgramData\\Anaconda3

### Usage

Le fichier « relation.csv » doit d’abord être être configuré avec les noms de fichiers que l’on souhaite aligner. Pour cela, insérer dans les colonnes « État 1 » et « État 2 », les noms des fichiers sans l’extension.

Le module **autoMDT-alignment.py** doit ensuite être configuré puisqu’il gèrent les options natives à MEDITE. Dans la fonction d’exécution du module, vous constaterez en effet la ligne suivante :

    main(casse=False, separator=False, diacritique=False, word=False)
    
Chacun des paramètres de cette fonction correspond à une option de MEDITE disponible en ligne :

* **Casse**. Correspond à l’option « Sensible à la casse ».
* **Separator**. Correspond à l’option « Sensible aux séparateurs ».
* **Diacritique**. Correspond à l’option « Sensible aux diacritiques ».
* **Word**. Correspond à l’option « Algorithme mots (cochée) ou caractères (non cochée) ».

Pour changer les options, insérer le booléen « True » à la place de « False ».

Par exemple, si vous souhaitez que MEDITE compare les versions en étant uniquement sensible à la casse, il vous faut rentrer la ligne suivante :

    main(casse=True, separator=False, diacritique=False, word=False)

L’exécution du module entraîne le téléchargement des versions alignées dans le répertoire « alignment  ».

## autoMDT-interface.py

### Pré-requis

**autoMDT-interface.py** nécessite l’installation d’un serveur pour afficher correctement les graphiques. 

Pour Windows, on utilisera de préférence un serveur Wamp64.

### Usage

**autoMDT-interface.py** ne nécessite pas de configuration particulière.

L’exécution du module entraîne la création d’une interface disponible dans le répertoire « interface ». Pour la consulter, ouvrez le fichier HTML correspondant dans le navigateur de votre choix. Un bug, en cours de résolution, empêche la consultation du graphique : les données brutes sont toutefois présentes dans le répertoire « data ».
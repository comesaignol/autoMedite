<html>
  <head>
    <meta charset="utf-8"/>

    <!--PLUGIN CSS-->
    <link type="text/css" crossorigin="anonymous" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" rel="stylesheet"/>
    <link type="text/css" href="resource/OverlayScrollbars-master/css/OverlayScrollbars.css" rel="stylesheet"/>
    <link type="text/css" href="css/style.css" rel="stylesheet"/>

    <!--PLUGIN JS-->
    <script crossorigin="anonymous" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script type="text/javascript" src="resource/OverlayScrollbars-master/js/jquery.overlayScrollbars.js"></script>
    <script crossorigin="anonymous" src="https://kit.fontawesome.com/786f99c904.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.3.2/dist/chart.min.js"></script>
    <script src="js/script.js"></script>
  </head>

  <body class="container-fluid h-100 d-flex flex-column p-0 m-0" id="container">

    <!------------>
    <!-- HEADER -->
    <!------------>

    <header class="row navbar navbar-expand-lg m-0 p-0" id="header">
      <h1 class="col-2 m-0 py-2 text-center">AutoMEDITE</h1>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="col-10 collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li>
            <a type="button" class="btn" data-toggle="modal" data-target="#statisticModal">Statistique</a>
          </li>
          <li class="nav-item">
            <a type="button" class="btn" data-toggle="modal" data-target="#documentationModal">Documentation</a>
          </li>
          <li class="nav-item">
            <a type="button" class="btn" data-toggle="modal" data-target="#researchModal">Unités de recherche</a>
          </li>
          <li class="nav-item">
            <a type="button" class="btn" data-toggle="modal" data-target="#contactModal">Contact</a>
          </li>
        </ul>
        <!--<form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>-->
      </div>
    </header>

    <!---------->
    <!-- MAIN -->
    <!---------->

    <main class="row flex-fill m-0" style="min-height:0;">

      <!----------------->
      <!-- INFORMATION -->
      <!----------------->

      <div class="col-2 mh-100 order-1 p-3 collapse show" id="information">

        <hr/>

        <!---------->
        <!--LEGEND-->
        <!---------->

        <div class="container px-4" id="legend">
          <div class="row">
            <div class="col-12 px-0">
              <h5><i class="fas fa-house-user"/>Légende</h5>
            </div>
          </div>
          <div class="row">
            <div class="circle" id="circle-insertion"/>
            <div class="col-auto">Insertion</div>
          </div>
          <div class="row">
            <div class="circle" id="circle-suppression"/>
            <div class="col-auto">Suppression</div>
          </div>
          <div class="row">
            <div class="circle" id="circle-remplacement"/>
            <div class="col-auto">Remplacement</div>
          </div>
          <div class="row">
            <div class="circle" id="circle-deplacement"/>
            <div class="col-auto">Déplacement</div>
          </div>
        </div>

        <hr/>

        <!------------>
        <!--DOWNLOAD-->
        <!------------>
        
        <div class="container px-4" id="download">
          <div class="row">
            <div class="col-12 px-0">
              <h5><i class="fas fa-cloud-download-alt"/>Téléchargement</h5>
            </div>
          </div>
          <div class="row">
            <div class="col-6 px-0">
              <a href="" id="downloadTEI" download>
                <i class="fas fa-file-code"/>
              </a>
              <p>XML-TEI</p>
            </div>
            <div class="col-6 px-0">
              <i class="fas fa-file-csv"/>
              <p>CSV</p>
            </div>
          </div>
        </div>

        <hr/>

      </div>

      <!--------------->
      <!-- VERSION 1 -->
      <!--------------->

      <div class="col-5 mh-100 order-2 p-5" id="version1"/>

      <!--------------->
      <!-- VERSION 2 -->
      <!--------------->

      <div class="col-5 mh-100 order-3 p-5" id="version2"/>

      <!--------------------->
      <!-- MODAL STATISTIC -->
      <!--------------------->

      <div class="modal fade" id="statisticModal" tabindex="-1" role="dialog" aria-labelledby="statisticModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title" id="statisticModalLabel">Analyse statistique</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-12">
                    <h5 class="modal-title">Échelle du texte</h5>
                  </div>
                </div>
                <div class="row">
                  <div class="col-4">
                    <canvas id="dataAbsolute" height=250></canvas>
                  </div>
                  <div class="col-4">
                    <canvas id="dataMoyenne" height=250></canvas>
                  </div>
                </div>
                <div class="row">
                  <div class="col-12">
                    <h5 class="modal-title">Échelle des personnages</h5>
                  </div>
                </div>
                <div class="row">
                  <div class="col-8">
                    <canvas id="dataPersonnage" height=250></canvas>
                  </div>
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" data-dismiss="modal">Fermer</button>
            </div>
          </div>
        </div>
      </div>

      <!------------------------->
      <!-- MODAL DOCUMENTATION -->
      <!------------------------->

      <div class="modal fade" id="documentationModal" tabindex="-1" role="dialog" aria-labelledby="documentationModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title" id="documentationModalLabel">Documentation</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <div class="container-fluid">
                <div class="row">
                  <section class="col-12" id="introductionLabel">
                    <h4>Introduction</h4>
                    <p>AutoMEDITE est un ensemble de modules développés en Python 3 approfondissant les fonctionnalités de MEDITE, un logiciel d’alignement textuel comparant automatiquement de deux versions d’une même œuvre.</p>
                    <p>Là où MEDITE offre une première exploration des corpus, AutoMEDITE la rend interropérable en proposant une interface d’édition et de recherche utile pour les chercheurs en Humanités numériques.</p>
                  </section>
                </div>
                <div class="row">
                  <section class="col-12" id="quickStartLabel">
                    <h4>Démarage rapide</h4>
                    <p>Vous souhaitez intégrer AutoMEDITE dans votre projet ? Explorez rapidement vos corpus textuels ? Le code source est disponible au téléchargement à l’adresse suivante :  <a href="https://github.com/comesaignol/autoMedite" target="_blank">https://github.com/comesaignol/autoMedite</a>.</p>
                    <pre>
├── css/
│   ├── bootstrap-grid.css
│   ├── bootstrap-grid.css.map
│   ├── bootstrap-grid.min.css
│   ├── bootstrap-grid.min.css.map
│   ├── bootstrap-grid.rtl.css
│   ├── bootstrap-grid.rtl.css.map
│   ├── bootstrap-grid.rtl.min.css
│   ├── bootstrap-grid.rtl.min.css.map
│   ├── bootstrap-reboot.css
│   ├── bootstrap-reboot.css.map
│   ├── bootstrap-reboot.min.css
│   ├── bootstrap-reboot.min.css.map
│   ├── bootstrap-reboot.rtl.css
│   ├── bootstrap-reboot.rtl.css.map
│   ├── bootstrap-reboot.rtl.min.css
│   ├── bootstrap-reboot.rtl.min.css.map
│   ├── bootstrap-utilities.css
│   ├── bootstrap-utilities.css.map
│   ├── bootstrap-utilities.min.css
│   ├── bootstrap-utilities.min.css.map
│   ├── bootstrap-utilities.rtl.css
│   ├── bootstrap-utilities.rtl.css.map
│   ├── bootstrap-utilities.rtl.min.css
│   ├── bootstrap-utilities.rtl.min.css.map
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── bootstrap.rtl.css
│   ├── bootstrap.rtl.css.map
│   ├── bootstrap.rtl.min.css
│   └── bootstrap.rtl.min.css.map
└── js/
    ├── bootstrap.bundle.js
    ├── bootstrap.bundle.js.map
    ├── bootstrap.bundle.min.js
    ├── bootstrap.bundle.min.js.map
    ├── bootstrap.esm.js
    ├── bootstrap.esm.js.map
    ├── bootstrap.esm.min.js
    ├── bootstrap.esm.min.js.map
    ├── bootstrap.js
    ├── bootstrap.js.map
    ├── bootstrap.min.js
    └── bootstrap.min.js.map


                      </pre>
                    </div>
                  </section>
                </div>
                <div class="row">
                  <section class="col-12" id="contentLabel">
                    <h4>Contenus</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Et non ex maxima parte de tota iudicabis? Si longus, levis; </p>
                    <p>Eadem nunc mea adversum te oratio est. Ostendit pedes et pectus. Sed tamen intellego quid velit. Laboro autem non sine causa; Quamquam te quidem video minime esse deterritum. Non potes, nisi retexueris illa. </p>
                    <p>Scrupulum, inquam, abeunti; Ait enim se, si uratur, Quam hoc suave! dicturum. Primum Theophrasti, Strato, physicum se voluit; Nemo igitur esse beatus potest. Duo Reges: constructio interrete. At, si voluptas esset bonum, desideraret. </p>
                  </section>
                </div>
                <div class="row">
                  <div class="col-8">
                  </div>
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" data-dismiss="modal">Fermer</button>
            </div>
          </div>
        </div>
      </div>



      <!-- # Introduction




# Démarrage rapide



Il fonctionne 

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

L’exécution du module entraîne la création d’une interface disponible dans le répertoire « interface ». Pour la consulter, ouvrez le fichier HTML correspondant dans le navigateur de votre choix. Un bug, en cours de résolution, empêche la consultation du graphique : les données brutes sont toutefois présentes dans le répertoire « data ». -->
      
    </main>
  </body>

  <script type="text/javascript">

    ///////////////////////
    // OVERLAY SCROLLBAR //
    ///////////////////////
    
    // Make 
    $(function() {
      $("#information").overlayScrollbars({
        className: "os-theme-dark ",
      });
      $("#version1").overlayScrollbars({
        className: "os-theme-dark ",
      });
      $("#version2").overlayScrollbars({
        className: "os-theme-dark ",
      });
    });

    //////////
    // DATA //
    //////////

    $(document).ready(function () {
      makeDataAbsolute();
      makeDataMoyenne();
      makeDataPersonnage();
    });

  </script>
</html>
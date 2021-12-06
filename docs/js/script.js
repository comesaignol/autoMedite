
// 
// $(document).ready(function(){
//   $("span").on("click", function() {
//     var id = "#" + $(this).attr('id');
//     $("div.order-1").animate({
//       scrollTop: $(id).offset().top
//     }, 200);
//   });
// });

// Waypoint FONCTIONNEL
//var waypoint = new Waypoint({
//  element: document.getElementById("c_00002"),
//  handler: function(direction) {
//    console.log('Scrolled to waypoint!')
//  },
//  context: document.getElementById('version1')
//})

// Waypoint
// var continuousElements = document.getElementsByClassName('span_s')
// for (var i = 0; i < continuousElements.length; i++) {
//     new Waypoint({
//         element: continuousElements[i],
//         handler: function() {
//             // Log de l'élément
//             console.log(this.element.id + " hit !");
//         },
//         context: document.getElementById('version1'),
//     })
// }

////////////////////////
// MAKE DATA ABSOLUTE //
////////////////////////

function makeDataAbsolute() {
  var requestURL = "data/dataAbsolute.json";
  $.getJSON(requestURL, function(result) {
    // Récupération des données JSON
    var myKeys = [];
    var myValues = [];
    $.each(result, function(key, value){
      myKeys.push(key)
      myValues.push(value)
    });
    
    // Création du Graph
    var dataGraph = {
      type: "bar",
      data: {
        labels: [], // Données Json à importer ici
        datasets: [
          {
            label: "Insertion",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(0, 180, 120, 0.2)",
            borderColor: "rgb(0, 180, 120)",
            borderWidth: 1,
          },
          {
            label: "Suppression",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgb(255, 99, 132)",
            borderWidth: 1,
          },
          {
            label: "Déplacement",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            borderColor: "rgb(54, 162, 235)",
            borderWidth: 1,
          },
          {
            label: "Remplacement",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(255, 159, 64, 0.2)",
            borderColor: "rgb(255, 159, 64)",
            borderWidth: 1,
          },
        ]
      },
      options: {
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0
          }
        },
        scales: {
          y: {
            ticks: {
              color: "#a5adc6",
            }
          },
          x: {
            ticks: {
              color: "#a5adc6",
            }
          }
        },
        plugins: {
          legend: {
            display: true,
          },
          title: {
            display: true,
            text: "Volume total des réécritures (token)",
            color: "#a5adc6",
            font: {
              weight: "normal"
            }
          }
        },
        responsive: true,
      }
    };
    //Ajout des datas issues du Json
    dataGraph.data.labels = myValues[0];
    dataGraph.data.datasets[0].data = myValues[2][0];
    dataGraph.data.datasets[1].data = myValues[2][1];
    dataGraph.data.datasets[2].data = myValues[2][2];
    dataGraph.data.datasets[3].data = myValues[2][3];
    // Création du diagramme
    var myBarChart = new Chart($("#dataAbsoluteCanvas"), dataGraph);
  });
}


///////////////////////
// MAKE DATA MOYENNE //
///////////////////////

function makeDataMoyenne() {
  var requestURL = "data/dataMoyenne.json";
  $.getJSON(requestURL, function(result) {
    // Récupération des données JSON
    var myKeys = [];
    var myValues = [];
    $.each(result, function(key, value){
      myKeys.push(key)
      myValues.push(value)
    });

    console.log(myValues)
    // Création du Graph
    var dataGraph = {
      type: "bar",
      data: {
        labels: [], // Données Json à importer ici
        datasets: [
          {
            label: "Insertion",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(0, 180, 120, 0.2)",
            borderColor: "rgb(0, 180, 120)",
            borderWidth: 1,
          },
          {
            label: "Suppression",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgb(255, 99, 132)",
            borderWidth: 1,
          },
          {
            label: "Déplacement",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            borderColor: "rgb(54, 162, 235)",
            borderWidth: 1,
          },
          {
            label: "Remplacement",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(255, 159, 64, 0.2)",
            borderColor: "rgb(255, 159, 64)",
            borderWidth: 1,
          },
        ]
      },
      options: {
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0
          }
        },
        scales: {
          y: {
            ticks: {
              color: "#a5adc6",
            }
          },
          x: {
            ticks: {
              color: "#a5adc6",
            }
          }
        },
        plugins: {
          legend: {
            display: true,
          },
          title: {
            display: true,
            text: "Taille moyenne d'une réécriture (token)",
            color: "#a5adc6",
            font: {
              weight: "normal"
            }
          }
        },
        responsive: true,
      }
    };
    //Ajout des datas issues du Json
    dataGraph.data.labels = myValues[0];
    dataGraph.data.datasets[0].data = myValues[2][0];
    dataGraph.data.datasets[1].data = myValues[2][1];
    dataGraph.data.datasets[2].data = myValues[2][2];
    dataGraph.data.datasets[3].data = myValues[2][3];
    // Création du diagramme
    var myBarChart = new Chart($("#dataMoyenneCanvas"), dataGraph);
  });
}

//////////////////////////
// MAKE DATA PERSONNAGE //
//////////////////////////

function makeDataPersonnage() {
  var requestURL = "data/dataPersonnage.json";
  $.getJSON(requestURL, function(result) {
    // Récupération des données JSON
    var myKeys = [];
    var myValues = [];
    $.each(result, function(key, value){
      myKeys.push(key)
      myValues.push(value)
    });

    console.log(myValues)
    // Création du Graph
    var dataGraph = {
      type: "bar",
      data: {
        labels: [], // Données Json à importer ici
        datasets: [
          {
            label: "Insertion",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(0, 180, 120, 0.2)",
            borderColor: "rgb(0, 180, 120)",
            borderWidth: 1,
          },
          {
            label: "Suppression",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgb(255, 99, 132)",
            borderWidth: 1,
          },
          {
            label: "Déplacement",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            borderColor: "rgb(54, 162, 235)",
            borderWidth: 1,
          },
          {
            label: "Remplacement",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(255, 159, 64, 0.2)",
            borderColor: "rgb(255, 159, 64)",
            borderWidth: 1,
          },
        ]
      },
      options: {
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0
          }
        },
        scales: {
          y: {
            ticks: {
              color: "#a5adc6",
            }
          },
          x: {
            ticks: {
              color: "#a5adc6",
            }
          }
        },
        plugins: {
          legend: {
            display: true,
          },
          title: {
            display: true,
            text: "Volume total des réécritures par personnage (token)",
            color: "#a5adc6",
            font: {
              weight: "normal"
            }
          }
        },
        responsive: true,
      }
    };
    //Ajout des datas issues du Json
    dataGraph.data.labels = myValues[0];
    dataGraph.data.datasets[0].data = myValues[2][0];
    dataGraph.data.datasets[1].data = myValues[2][1];
    dataGraph.data.datasets[2].data = myValues[2][2];
    dataGraph.data.datasets[3].data = myValues[2][3];
    // Création du diagramme
    var myBarChart = new Chart($("#dataPersonnageCanvas"), dataGraph);
  });
}

// 
$(document).ready(function(){
  $("span").on("click", function() {
    var id = "#" + $(this).attr('id');
    $("div.order-1").animate({
      scrollTop: $(id).offset().top
    }, 200);
  });
});

// Waypoint FONCTIONNEL
//var waypoint = new Waypoint({
//  element: document.getElementById("c_00002"),
//  handler: function(direction) {
//    console.log('Scrolled to waypoint!')
//  },
//  context: document.getElementById('version1')
//})

// Waypoint
var continuousElements = document.getElementsByClassName('span_s')
for (var i = 0; i < continuousElements.length; i++) {
    new Waypoint({
        element: continuousElements[i],
        handler: function() {
            // Log de l'élément
            console.log(this.element.id + " hit !");
        },
        context: document.getElementById('version1'),
    })
}

function createDatavizCar(id) {
  var requestURL = "http:localhost/autoMedite/interface/" + id + "/data/datavizCar.json"
  $.getJSON(requestURL, function(result) {
    // Récupération des données JSON
    var myKeys = [];
    var myValues = [];
    $.each(result, function(key, value){
      myKeys.push(key)
      myValues.push(value)
    });
    
    console.log(myKeys)
    // Création du Graph
    var dataGraph = {
      type: "bar",
      data: {
        labels: [], // Données Json à importer ici
        datasets: [
          {
            label: "Nombre de caractères ",
            data: [], // Données Json à importer ici
            backgroundColor: ["rgba(0, 180, 120, 0.2)",
            									"rgba(255, 99, 132, 0.2)",
            									"rgba(54, 162, 235, 0.2)",
            									"rgba(255, 159, 64, 0.2)"],
            borderColor: ["rgb(0, 180, 120)",
            							"rgb(255, 99, 132)",
            							"rgb(54, 162, 235)",
            							"rgb(255, 159, 64)"],
            borderWidth: 1,
          }
        ]
      },
      options: {
        backgroundColor: "#F5DEB3",
        title: {
          display: false,
          fontFamily: "Liberation Serif",
          fontSize: 14,
          fontStyle: "normal",
          position: "top",
          text: "",  // Données Json à importer ici
        },
        scales: {
          xAxes: [{
            gridLines: {
              display: true,
            },
            ticks: {
              beginAtZero: true,
            },
          }],
          yAxes: [{
            gridLines: {
              display: false,
            },
            ticks: {
              beginAtZero: true,
            }
          }],
        },
        layout: {
          padding: {
            left: 30,
            right: 30,
            top: 30,
            bottom: 30
          }
        },
        legend: {
          display: false,
          position: "bottom"
        },
        responsive: true,
      }
    };
    //Ajout des datas issues du Json
    dataGraph.data.labels = myKeys;
    dataGraph.data.datasets["0"].data = myValues;
    // Création du diagramme
    var myBarChart = new Chart($("#dataVizCar"), dataGraph);
  });
}
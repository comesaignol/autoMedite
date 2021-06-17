
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

function makeDataAbsolute(id) {
  var requestURL = "data/dataAbsolute.json";
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
            label: "Nb. de tokens ",
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
            display: false,
          },
          title: {
            display: true,
            text: "Nombre de tokens",
            color: "#a5adc6", 
          }
        },
        responsive: true,
      }
    };
    //Ajout des datas issues du Json
    dataGraph.data.labels = myKeys;
    dataGraph.data.datasets["0"].data = myValues;
    // Création du diagramme
    var myBarChart = new Chart($("#dataAbsolute"), dataGraph);
  });
}
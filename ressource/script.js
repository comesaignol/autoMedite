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
            label: "Nombre d'occurences ",
            data: [], // Données Json à importer ici
            backgroundColor: "rgba(0, 153, 59, 0.60)",
            borderColor: "rgba(0, 153, 59, 1)",
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
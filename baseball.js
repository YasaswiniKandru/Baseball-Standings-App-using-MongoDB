$(document).ready(function() {
  var url = 'http://localhost:5000/baseball/standings/';
  $.ajax({
    url: url,
    type: 'GET',
    success: function(response) {
      var standings = response.standings;
      var htmlCode = "<table border=\"2\">\n";
      htmlCode += "<tr><th>TEAM</th><th>WINS</th><th>LOSSES</th><th>TIES</th><th>PERCENT</th></tr>\n";
      for (var i=0; i<standings.length; i++) {
        htmlCode += "<tr>";
        htmlCode += "<td><a href=\"#\""+
                    " id=\""+standings[i].tcode+"\" onClick=\"getResults(this.id)\" >"+
                    standings[i].tname+"</a></td>\n";
        htmlCode += "<td>"+standings[i].wins+"</td>\n";
        htmlCode += "<td>"+standings[i].losses+"</td>\n";
        htmlCode += "<td>"+standings[i].ties+"</td>\n";
        htmlCode += "<td>"+standings[i].percent+"</td>\n";
        htmlCode += "</tr>\n";
      }
      htmlCode += "</table>";
      $("#standings_section").html(htmlCode);
    },
    error: function(error) {
      alert("ERROR");
      console.log(error);
    }
  });
});

function getResults(tcode) {
  var url = 'http://localhost:5000/baseball/results/'+tcode+"/";
  $.ajax({
    url: url,
    type: 'GET',
    success: function(response) {
      var results = response.results;
      var htmlCode = "<h3>" + response.tloc + " " + response.tname + "</h3>";
      htmlCode += "<table border=\"2\">\n";
      htmlCode += "<tr><th>DATE</th><th>OPPONENT</th><th>US</th><th>THEM</th><th>RESULT</th></tr>\n";
      for (var i=0; i<results.length; i++) {
        htmlCode += "<tr>";
        htmlCode += "<td>"+results[i].gdate+"</td>\n";
        htmlCode += "<td>"+results[i].opponent+"</td>\n";
        htmlCode += "<td>"+results[i].us+"</td>\n";
        htmlCode += "<td>"+results[i].them+"</td>\n";
        htmlCode += "<td>"+results[i].result+"</td>\n";
        htmlCode += "</tr>\n";
      }
      htmlCode += "</table>";
      $("#results_section").html(htmlCode);
    },
    error: function(error) {
      alert("ERROR");
      console.log(error);
    }
  });
};
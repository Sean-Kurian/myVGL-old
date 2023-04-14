function sortTable(col) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("games-table");
  switching = true;
  dir = "asc"; 
  while (switching) {
    switching = false;
    rows = table.getElementsByTagName("tr");
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("td")[col];
      y = rows[i + 1].getElementsByTagName("td")[col];
      if (col == 1) { // check if sorting by Date column
        var dateX = new Date(x.innerHTML.trim().replace(/(\w+)\. (\d+), (\d+)/, "$1 $2, $3"));
        var dateY = new Date(y.innerHTML.trim().replace(/(\w+)\. (\d+), (\d+)/, "$1 $2, $3"));
        if (dir == "asc") {
          if (dateX > dateY || isNaN(dateY)) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (dateX < dateY || isNaN(dateX)) {
            shouldSwitch = true;
            break;
          }
        }
      } else { // sorting by non-Date column
        if (dir == "asc") {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase() || y.innerHTML == "") {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase() || x.innerHTML == "") {
            shouldSwitch = true;
            break;
          }
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++; 
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

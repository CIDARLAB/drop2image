$(document).ready(function() {
  $('#colors td').click(function() {
    var color = $(this).css('background-color');
    $(':root').css('--current-color', color);
    console.log(color)
  });
});

$('#pixs').on('click', 'td', function() {
  $(this).css('background-color', $(':root').css('--current-color'));
});

document.getElementById("save").addEventListener("click", function() {
  html2canvas(document.body).then(function(canvas) {
    var screenshot = canvas.toDataURL("image/png");
    var link = document.createElement('a');
    link.download = 'screenshot.png';
    link.href = screenshot;
    link.click();
  });
});

$(document).ready(function(){
  $('#update').click(function(){
    var num_cols = $('#col').val();
    var num_rows = $('#row').val();
    var table_rows = $('#pixs tr');

    table_rows.remove();

    for (var i=0; i<num_rows; i++){
      var new_row = $('<tr>');
      for (var j=0; j<num_cols; j++){
        new_row.append('<td></td>');
      }
      $('#pixs').append(new_row);
    }
  });
});

$(document).ready(function(){
  $('#add').click(function(){
    var selected_color = $('#newcolor').val();
    var new_cell = $('<td></td>').css('background-color', selected_color);
    $('#colors tr:last-child').append(new_cell);
  });
});

// document.getElementById("fetch").addEventListener("click", ()=>{eel.fetch()}, false);
// document.getElementById("fetch").onclick = ()=>

// document.getElementById("")

// black with white outline
// button smaller
// dark mode
// mouse down and mouse click might help do the click and drag coloring
// dynamically changing dimention
// title


// img size & table size fixed 50x50
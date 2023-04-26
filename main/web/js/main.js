document.getElementById("black").onclick = function(){
  document.querySelector(":root").style.setProperty('--current-color', 'black')
};
document.getElementById("blue").onclick = function(){
  document.querySelector(":root").style.setProperty('--current-color', 'blue')
};
document.getElementById("red").onclick = function(){
  document.querySelector(":root").style.setProperty('--current-color', 'red')
};
document.getElementById("green").onclick = function(){
  document.querySelector(":root").style.setProperty('--current-color', 'green')
};
document.getElementById("yellow").onclick = function(){
  document.querySelector(":root").style.setProperty('--current-color', 'yellow')
};
document.getElementById("pink").onclick = function(){
  document.querySelector(":root").style.setProperty('--current-color', 'pink')
};
document.getElementById("cyan").onclick = function(){
  document.querySelector(":root").style.setProperty('--current-color', 'cyan')
};
document.getElementById("white").onclick = function(){
  document.querySelector(":root").style.setProperty('--current-color', 'white')
};

var pixs = document.getElementById("pixs");
pixs.onclick = function(evt){
  var target = evt.target || event.srcElement;
  if ((target.tagName || "").match(/td/i)){
    target.style.backgroundColor = getComputedStyle(document.querySelector(':root')).getPropertyValue('--current-color');
  }
};

document.getElementById("save").addEventListener("click", function() {
  html2canvas(document.body).then(function(canvas) {
    var screenshot = canvas.toDataURL("image/png");
    var link = document.createElement('a');
    link.download = 'screenshot.png';
    link.href = screenshot;
    link.click();
  });
});

let cv = require('./opencv.js')

document.getElementById("fetch").addEventListener("change", function(){
  let upload_file = document.getElementById("uploaded_image").files[0];
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

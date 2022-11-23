document.getElementById("button-name").addEventListener("click", ()=>{eel.get_random_name()}, false);
document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-date").addEventListener("click", ()=>{eel.get_date()}, false);
document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);

document.getElementById("blue").onclick = function(){this.style.backgroundColor = getComputedStyle(document.querySelector(':root')).getPropertyValue('--current-color');};

function set_current_color(color){
    document.querySelector(':root').style.setProperty('--current-color', color);
    console.log(getComputedStyle(document.querySelector(':root')).getPropertyValue('--current-color'));
}

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}
function tostr(j){
    return JSON.stringify(j);
}
function log(msg){
    var d = crt('div');apd($('result'),d);
    d.innerHTML = msg;
}
function loginfo(msg){
    var d = crt('div');apd($('info'),d);
    d.innerHTML = msg;
}

function crt(tn){
    return document.createElement(tn);
}
function $(id){
    return document.getElementById(id);
}
function apd(n1, n2){
    n1.appendChild(n2);
}


function two(n){
    return Math.round(n * 100) / 100;
}


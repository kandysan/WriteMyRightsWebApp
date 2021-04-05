window.onload = function() {
    let key = document.getElementsByName("key")
    let value = getCookie(key[0].value)
    let checked = false

    let buttons = document.getElementsByClassName("radioButtons"); 
    for (k = 0; k < buttons.length; k++) {
        if (buttons[k].value == value) {
            buttons[k].checked = true
        }
    }
}

function getCookie(cname) {
var name = cname + "=";
var decodedCookie = decodeURIComponent(document.cookie);
var ca = decodedCookie.split(';');
for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
    c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
    return c.substring(name.length, c.length);
    }
}
return "";
}
window.onload = function() {
    let key = document.getElementsByName("key")
    let value = getCookie(key[0].value)

    let dropdown = document.getElementsByClassName("dropdown"); 
    for (k = 0; k < dropdown.length; k++) {
        for (i = 0; i < 101; i++) {
            let number = document.createElement("option")
            number.text = i;
            number.value = i;
            dropdown[k].options[i + 1] = number;
            if (i == value && value != "") {
                dropdown[k].options[i + 1].selected = true
            }
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
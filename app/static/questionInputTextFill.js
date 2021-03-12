window.onload = (event) => {
    let key = document.getElementsByName("key")
    let value = getCookie(key[0].value)
    value = value.replace(/['"]+/g, '')
    let fields = document.getElementsByClassName("questionInput")
    if (value.length > 0) {
        for (var i=0; i < fields.length; i++) {
            fields[i].value = value;
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
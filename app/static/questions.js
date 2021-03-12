var width = 0;
var clicks = 0; 
var id = setInterval(frame, 40); 
window.onload = (event) => {
    var elem = document.getElementById("myBar");   
    elem.style.width = "0%";
}
function frame() {
  if (width >= 100) {
      clearInterval(id);
      location.href="/paymentDone"
  } 
  else {
      width ++; 
      var elem = document.getElementById("myBar"); 
      elem.style.width = width + '%'; 
      if (width == 30) {
        document.getElementById("writingLetterText").innerHTML = "Cracking our knuckles ..."
      }
      else if (width == 60) {
        document.getElementById("writingLetterText").innerHTML = "Typing your letter ..."
      }
      else if (width == 90) {
        document.getElementById("writingLetterText").innerHTML = "Finishing touches ..."
      }
  }
}

function buttonOnClick() { 
    clicks += 1; 
    if (clicks % 2 == 1) { 
        document.getElementsByClassName(questionButton).style.backgroundColor = 'grey';
    } 
    else if (clicks % 2 == 0) { 
        document.getElementsByClassName(questionButton).style.backgroundColor = '#e1e1e1';
    } 
};
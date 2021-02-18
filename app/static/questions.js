var clicks = 0; 
function buttonOnClick() { 
    clicks += 1; 
    if (clicks % 2 == 1) { 
        document.getElementsByClassName(questionButton).style.backgroundColor = 'grey';
    } 
    else if (clicks % 2 == 0) { 
        document.getElementsByClassName(questionButton).style.backgroundColor = '#e1e1e1';
    } 
};

function progressBarMove() {
    location.href='fetchLetter.html'
    var elem = document.getElementById("myBar");   
    var width = 1;
    var id = setInterval(frame, 20);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
      } else {
        width++; 
        elem.style.width = width + '%'; 
      }
    }
  }
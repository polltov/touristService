theads = document.querySelectorAll('thead')
tbodies = document.querySelectorAll('tbody')

for (var i = 0; i < theads.length; i++) {
  theads[i].addEventListener("click", bindClick(i));
}

function bindClick(i) {
  return function () {
    if(tbodies[i].classList.contains('tbody-none')) {
      tbodies[i].classList.remove('tbody-none')
    } else {
      tbodies[i].classList.add('tbody-none')
    }
  };
}

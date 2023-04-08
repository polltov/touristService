rating = document.querySelectorAll('.rating');
stars = document.querySelectorAll('.star-fill');

for(let i = 0; i < rating.length; ++i) {
  for(let j = 0; j < rating[i].innerHTML; ++j) {
    stars[i * 5 + j].style.fill = "#0089e2";
  }
}
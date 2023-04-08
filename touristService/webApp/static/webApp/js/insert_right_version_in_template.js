window.addEventListener('resize', function() {
const width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

const title_of_rergion = document.querySelector('.title-of-rergion').innerHTML;
const short_definition_of_region = document.querySelector('.short-definition-of-region').innerHTML;
const region_image = document.querySelector('.region-image').src;

const profile_element = document.querySelector('.single-title');

if (width <= 768) {
  const html_for_modile = `<div class="profile-mobile"><img src="${region_image}"" class="region-image" alt=""><h4 class="title-of-rergion title-of-rergion-mobile">${title_of_rergion}</h4></div><p class="short-definition-of-region"> ${short_definition_of_region} </p>`;
  profile_element.classList.add('single-title-mobile')
  profile_element.innerHTML = html_for_modile;
} else {
  const html_for_desktop = `<img src="${region_image}" class="region-image" alt=""><div class="text-of-region"><h4 class="title-of-rergion">${title_of_rergion}</h4><p class="short-definition-of-region"> ${short_definition_of_region} </p></div>`;
  profile_element.classList.remove('single-title-mobile')
  profile_element.innerHTML = html_for_desktop;
}
})
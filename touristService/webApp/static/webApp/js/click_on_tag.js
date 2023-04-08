tags = document.querySelectorAll('.tag')
tagsSelected = []

for (var i = 0; i < tags.length; i++) {
  tags[i].addEventListener("click", bindClick(i));
}

function bindClick(i) {
  return function () {
    id = tags[i].getAttribute('data-id');
    if(tags[i].classList.contains('tags_on_click')) {
      tags[i].classList.remove('tags_on_click');
      const index = tagsSelected.indexOf(id);
      if (index > -1) {
        tagsSelected.splice(index, 1);
      }
    } else {
      tags[i].classList.add('tags_on_click');
      tagsSelected.push(id)
    }
  };
}

q_form = document.getElementsByClassName('search-form')[0]

q_form.addEventListener("submit", (e) => formQ(e));

function formQ(e) {
  e.preventDefault();
  q = document.querySelector('.form-control').value;
  idsOfTags = tagsSelected.toString();
  href="/";
  if (q != "" && tagsSelected.length > 0) {
    href = "?q=" + q + '&tags=' + idsOfTags;
  } else if (q != "") {
    href="?q=" + q;
  } else {
    href="?tags=" + idsOfTags;
  }
  window.location.href = href
}

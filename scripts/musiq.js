const genres = document.querySelectorAll("h2");

genres.forEach(g => g.addEventListener("click", show));

function show(e) {
  location.href = `/game?genre=${e.currentTarget.innerHTML}`;
}

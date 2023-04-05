const titleInput = document.querySelector("input[name=product_name]");
const slugInput = document.querySelector("input[name=slug]");

const slugify = (val) => {
  return val
    .toString()
    .toLowerCase()
    .trim()
    .replace(/&/g, "-and-") // replace & with '-and-''
    .replace(/[\s\d-\W]+/g, "-"); // replaces spaces, non word chars and dashes with dashes
};

titleInput.addEventListener("keyup", (e) => {
  slugInput.setAttribute("value", slugify(titleInput.value));
});

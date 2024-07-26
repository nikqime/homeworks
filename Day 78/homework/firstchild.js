let firstChild = parentElement.firstChild;
console.log(firstChild.textContent);

// მაგალითი 2:
if (firstChild) {
  firstChild.textContent = 'First child changed';
}
let parentElement = document.getElementById('parent');
let childNodes = parentElement.childNodes;
childNodes.forEach(node => {
  if (node.nodeType === Node.ELEMENT_NODE) {
    node.textContent = 'Changed content';
  }
});

// მაგალითი 2:
while (parentElement.firstChild) {
  parentElement.removeChild(parentElement.firstChild);
}
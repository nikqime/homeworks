if (parentElement.hasChildNodes()) {
    console.log('Element has children');
  } else {
    console.log('Element has no children');
  }
  
  // მაგალითი 2:
  if (parentElement.hasChildNodes()) {
    parentElement.innerHTML = '';
  }
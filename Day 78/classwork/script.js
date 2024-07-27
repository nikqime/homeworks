//აიდით ვკითხულობთ
const paragraph = document.getElementById('myParagraph');

// ფუნქცია, რომელიც შეიცვლის პარაგრაფის ფერს დსა ტექსტსს
function changeParagraph() {
    paragraph.style.color = 'white';
    paragraph.style.backgroundColor = 'black'; 
    paragraph.textContent = 'პარაგრაფის ტექსტი'; 
}

// სამწამიანი დაყოვნება და შემდეგ ფუნქციის გამოძახება
setTimeout(changeParagraph, 3000);
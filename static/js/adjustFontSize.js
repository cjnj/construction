window.addEventListener('load', function() {
    adjustFontSize();
});

window.addEventListener('resize', function() {
    adjustFontSize();
});

function adjustFontSize() {
    const image = document.querySelector('.responsive-img');
    const paragraph = document.querySelector('.about2 p');
    const imageHeight = image.clientHeight;
    
    // Adjust font size to be 80% of image height (adjustable as needed)
    paragraph.style.fontSize = imageHeight * 0.1 + 'px';
}

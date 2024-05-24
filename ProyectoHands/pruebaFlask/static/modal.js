// Función para mostrar el modal con la imagen seleccionada
function showModal(index) {
    const modal = document.getElementById('myModal');
    const modalImg = document.getElementById("img01");
    const captionText = document.getElementById("caption");
    const images = document.querySelectorAll(".card img");
    const totalImages = images.length;

    modal.style.display = "block";

    // Obtener la URL de la imagen, ya sea GIF o estática
    let imageUrl = images[index].src;
    if (images[index].dataset.gif) {
        imageUrl = images[index].dataset.gif;
    }

    modalImg.src = imageUrl; // Mostrar la imagen en el modal
    captionText.innerHTML = images[index].alt;

    // Cerrar el modal al hacer clic fuera de él
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Navegación entre imágenes
    function nextImage() {
        index = (index + 1) % totalImages;
        let nextImageUrl = images[index].src;
        if (images[index].dataset.gif) {
            nextImageUrl = images[index].dataset.gif;
        }
        modalImg.src = nextImageUrl; // Mostrar la imagen siguiente en el modal
    }

    function prevImage() {
        index = (index - 1 + totalImages) % totalImages;
        let prevImageUrl = images[index].src;
        if (images[index].dataset.gif) {
            prevImageUrl = images[index].dataset.gif;
        }
        modalImg.src = prevImageUrl; // Mostrar la imagen anterior en el modal
    }

    // Agregar eventos de clic para la navegación en el modal
    document.getElementById('prevBtn').addEventListener('click', prevImage);
    document.getElementById('nextBtn').addEventListener('click', nextImage);
}

document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll(".card img");

    images.forEach(function (image, index) {
        image.addEventListener('click', function () {
            showModal(index);
        });
    });
});

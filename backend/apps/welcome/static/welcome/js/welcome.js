window.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.welcome-img');
    const photoContainer = document.querySelector('.photo-container');
    const photoContainerRect = photoContainer.getBoundingClientRect();

    const centerX = photoContainerRect.width / 2;
    const centerY = photoContainerRect.height / 2;

    images.forEach((img, index) => {
        // const imgWidth = img.width;
        // const imgHeight = img.height;

        // const offsetX = (Math.random() - 0.5);
        // const offsetY = (Math.random() - 0.5);

        // img.style.left = `${centerX - imgWidth / 2 + offsetX}px`;
        // img.style.top = `${centerY - imgHeight / 2 + offsetY}px`;

        // const randomRotation = (Math.random() * 60) - 30;
        // img.style.transform = `rotate(${randomRotation}deg)`;

        // img.style.zIndex = index + 1;
    });
});
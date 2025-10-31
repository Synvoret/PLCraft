window.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.welcome-img');
    const container = document.querySelector('.photo-container');
    const containerRect = container.getBoundingClientRect();

    const centerX = containerRect.width / 2;
    const centerY = containerRect.height / 2;

    images.forEach((img, index) => {
        const imgWidth = img.width;
        const imgHeight = img.height;

        img.style.position = 'absolute';

        const offsetX = (Math.random() - 0.5) * 300;
        const offsetY = (Math.random() - 0.5) * 300;

        // set position relative to center
        img.style.left = `${centerX - imgWidth / 2 + offsetX}px`;
        img.style.top = `${centerY - imgHeight / 2 + offsetY - 150}px`;

        // random rotation from -15 to +15
        const randomRotation = (Math.random() * 60) - 25;
        img.style.transform = `rotate(${randomRotation}deg)`;

        img.style.zIndex = index + 1;

    });
});

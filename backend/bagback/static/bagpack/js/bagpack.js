document.getElementById('bagpacks-show').addEventListener('click', () => {
    fetch('/api/v1/bagpacks/')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const photoContainer = document.getElementById('photoContainer');

            data.forEach((bagpack, index) => {
                const img = document.createElement('img');
                img.src = bagpack.image;
                img.alt = bagpack.name;
                img.classList.add('welcome-img', 'bagpack-img');
                img.style.position = 'absolute';

                const offsetX = (Math.random() - 0.5) * 300;
                const offsetY = (Math.random() - 0.5) * 300;
                const centerX = window.innerWidth / 2;
                const centerY = window.innerHeight / 2;

                img.style.left = `${centerX + offsetX}px`;
                img.style.top = `${centerY + offsetY}px`;
                img.style.transform = `rotate(0deg)`;
                img.style.zIndex = index + 1;

            });
        })
        .catch(error => {
            console.error(error);
        });
});
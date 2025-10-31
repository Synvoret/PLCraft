// document.addEventListener("DOMContentLoaded", function (e) {
//     const container = document.querySelector(".photo-container");
//     e.preventDefault();

//     if (!container) return;

//     const images = container.querySelectorAll("img");
//     images.forEach(img => {
//         if (!img.classList.contains("bagpack-img")) {
//             img.remove();
//         } else {
//             // Usuń klasę 'welcome-img'
//             img.classList.remove("welcome-img");
//         }
//     });

//     container.style.display = "flex";
//     container.style.flexDirection = "column";
//     container.style.alignItems = "center";
// });



document.addEventListener('DOMContentLoaded', function () {
    const bagpacksLink = document.getElementById('bagpacks-link');
    const photoContainer = document.querySelector('.photo-container');

    if (bagpacksLink && photoContainer) {
        bagpacksLink.addEventListener('click', function (e) {
            e.preventDefault(); // zapobiega przeładowaniu strony
            fetch('/bagpacks/') // endpoint Django zwracający HTML z obrazkami
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Błąd sieci: ' + response.status);
                    }
                    return response.text(); // odbieramy HTML
                })
                .then(html => {
                    photoContainer.innerHTML = html;

                    // Ustawiamy układ kolumnowy
                    photoContainer.style.display = 'flex';
                    photoContainer.style.flexDirection = 'column';
                    photoContainer.style.alignItems = 'center';

                    const images = photoContainer.querySelectorAll('.bagpack-img');
                    images.forEach(img => {
                        img.style.width = '300px';
                        img.style.marginBottom = '10px';
                    });
                })
                .catch(error => {
                    console.error('Wystąpił błąd:', error);
                });
        });
    }
});
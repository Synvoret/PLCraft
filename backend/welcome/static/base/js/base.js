document.addEventListener("DOMContentLoaded", function () {

    // season determination (only north hemisphere)
    const body = document.body;
    let month = (new Date().getMonth() + 1);
    let day = new Date().getDate();

    let season;
    
    if ((month === 3 && day >= 21) || (month === 4) || (month === 5) || (month === 6 && day < 22)) {
        season = 'spring';
    } else if ((month === 6 && day >= 22) || (month === 7) || (month === 8) || (month === 9 && day < 23)) {
        season = 'summer';
    } else if ((month === 9 && day >= 23) || (month === 10) || (month === 11) || (month === 12 && day < 22)) {
        season = 'autumn';
    } else {
        season = 'winter';
    }

    body.style.background = getComputedStyle(document.documentElement).getPropertyValue(`--${season}`);

});
document.addEventListener("DOMContentLoaded", function () {

    const body = document.body;
    let month = (new Date().getMonth() + 1);
    let day = new Date().getDate();

    let season;

    // Determine season based on month, only for north hemisphere
    // Winter - December(12), January(1), February(2)
    // Spring - March(3), April(4), May(5)
    // Summer - June(6), July(7), August(8)
    // Autumn - September(9), October(10), November(11)
    
    if ((month === 3 && day >= 21) || (month === 4) || (month === 5) || (month === 6 && day < 22)) {
        season = 'spring';
    } else if ((month === 6 && day >= 22) || (month === 7) || (month === 8) || (month === 9 && day < 23)) {
        season = 'summer';
    } else if ((month === 9 && day >= 23) || (month === 10) || (month === 11) || (month === 12 && day < 22)) {
        season = 'autumn';
    } else {
        season = 'winter';
    }

    // season = 'winter';
    // season = 'autumn';
    // season = 'spring';
    // season = 'summer';

    body.style.background = getComputedStyle(document.documentElement).getPropertyValue(`--${season}`);

});
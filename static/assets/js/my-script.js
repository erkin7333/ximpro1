const printTender = document.querySelector('.print-js');

$(document).ready(function () {
    $('.fancybox').fancybox({
        loop: true,
        openEffect  : 'elastic'
    });
});

if (printTender) {
    printTender.addEventListener('click', () => {
        window.print();
        return false;
    })
}

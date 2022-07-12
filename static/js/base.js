const btnScrollToTop = document.querySelector('#btnScrollToTop');
btnScrollToTop.addEventListener('click', function() {
    // window.scrollTo(0, 0);

    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth",
    });
});
// ....... Adding PAGE YEAR ..................  //
let date = new Date().getFullYear();
let dateTag = document.getElementById("date");
dateTag.innerHTML = "©" + " " + date;

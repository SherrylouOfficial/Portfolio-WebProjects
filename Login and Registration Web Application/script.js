const buttons = document.querySelectorAll(".btn");

buttons.forEach((button) => {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        button.classList.add("animate");

        setTimeout(() => {
            button.classList.remove("animate");
        }, 600);
    });
});

const LogRegBox = document.querySelector('.logreg-box');
const LoginLink = document.querySelector('.log-link');
const RegLink = document.querySelector('.reg-link');

RegLink.addEventListener('click', () => {
    LogRegBox.classList.add('active');
});

LoginLink.addEventListener('click', () => {
    LogRegBox.classList.remove('active');
});
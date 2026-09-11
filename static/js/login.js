// Input Focus Effect
const inputs = document.querySelectorAll("input");

inputs.forEach((input) => {
    input.addEventListener("focus", () => {
        input.style.border = "2px solid #2563eb";
    });

    input.addEventListener("blur", () => {
        input.style.border = "none";
    });
});

// Login Form
const form = document.querySelector("form");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    const email = document.querySelector("input[type='email']").value.trim();
    const password = document.querySelector("input[type='password']").value.trim();

    if(email === "" || password === ""){
        alert("Please fill all fields!");
        return;
    }

    alert("Login Successful!");

    // Dashboard Page
    window.location.href = "/dashboard";

});

// Button Animation
const button = document.querySelector("button");

button.addEventListener("mouseenter", () => {
    button.style.transform = "scale(1.05)";
});

button.addEventListener("mouseleave", () => {
    button.style.transform = "scale(1)";
});
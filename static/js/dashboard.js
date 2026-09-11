console.log("AI Workspace Dashboard Loaded Successfully");
const words = [
    "Full Stack Python Developer",
    "AI & ML Enthusiast",
    "Flask Developer",
    "Data Science Learner"
];

let wordIndex = 0;
let charIndex = 0;
let typing = true;

const typingText = document.getElementById("typing");

function typeEffect() {
    if (typing) {
        typingText.textContent = words[wordIndex].substring(0, charIndex++);
        if (charIndex > words[wordIndex].length) {
            typing = false;
            setTimeout(typeEffect, 1500);
            return;
        }
    } else {
        typingText.textContent = words[wordIndex].substring(0, charIndex--);
        if (charIndex < 0) {
            typing = true;
            wordIndex = (wordIndex + 1) % words.length;
        }
    }
    setTimeout(typeEffect, typing ? 100 : 50);
}

typeEffect();
const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {
    const update = () => {
        const target = +counter.getAttribute("data-target");
        const count = +counter.innerText.replace("+","");

        const inc = Math.ceil(target / 50);

        if(count < target){
            counter.innerText = count + inc + "+";
            setTimeout(update,30);
        }else{
            counter.innerText = target + "+";
        }
    };

    update();
});
const themeToggle = document.getElementById("theme-toggle");

themeToggle.addEventListener("click", function(e){
    e.preventDefault();

    document.body.classList.toggle("light-mode");

    if(document.body.classList.contains("light-mode")){
        this.innerHTML='<i class="fa-solid fa-sun"></i> Light Mode';
    }else{
        this.innerHTML='<i class="fa-solid fa-moon"></i> Dark Mode';
    }
});
const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("keypress", function(e){

    if(e.key === "Enter"){

        let value = this.value.toLowerCase().trim();

        if(value === "home"){
            document.getElementById("home").scrollIntoView({behavior:"smooth"});
        }

        else if(value === "about"){
            document.getElementById("about").scrollIntoView({behavior:"smooth"});
        }

        else if(value === "skills"){
            document.getElementById("skills").scrollIntoView({behavior:"smooth"});
        }

        else if(value === "projects"){
            document.getElementById("projects").scrollIntoView({behavior:"smooth"});
        }

        else if(value === "ai"){
            document.getElementById("aihub").scrollIntoView({behavior:"smooth"});
        }

        else if(value === "certificate"){
            document.getElementById("certificates").scrollIntoView({behavior:"smooth"});
        }

        else if(value === "contact"){
            document.getElementById("contact").scrollIntoView({behavior:"smooth"});
        }

        else{
            alert("Section Not Found");
        }

    }

});
const bell = document.getElementById("bell");
const notificationBox = document.getElementById("notificationBox");

bell.addEventListener("click", () => {

    if(notificationBox.style.display === "block"){
        notificationBox.style.display = "none";
    }else{
        notificationBox.style.display = "block";
    }

});
const progress = document.getElementById("progress");
const percent = document.getElementById("percent");
const statusText = document.getElementById("status");

const statusList = [
    "Initializing Neural Engine...",
    "Loading AI Modules...",
    "Verifying Security...",
    "Connecting Database...",
    "Preparing Workspace...",
    "Finalizing System..."
];

let value = 0;
let statusIndex = 0;

const loader = setInterval(() => {

    value++;

    progress.style.width = value + "%";
    percent.innerHTML = value + "%";

    // Status Change
    if (value % 20 === 0 && statusIndex < statusList.length - 1) {
        statusIndex++;
        statusText.innerHTML = statusList[statusIndex];
    }

    if (value >= 100) {

        clearInterval(loader);

        statusText.innerHTML = "✅ ACCESS GRANTED";
        percent.innerHTML = "WELCOME AYUSH";

        // Zoom Effect
        document.querySelector(".loading-box").style.transition = "1s";
        document.querySelector(".loading-box").style.transform = "scale(1.15)";
        document.querySelector(".loading-box").style.boxShadow =
            "0 0 120px cyan";

        setTimeout(() => {

            document.body.style.transition = "1s";
            document.body.style.opacity = "0";

            setTimeout(() => {

                window.location.href = "/landing";

            }, 1000);

        }, 1800);

    }

}, 50);
// CLOCK

function updateClock(){

let now = new Date();

document.getElementById("clock").innerHTML =
now.toLocaleTimeString();

document.getElementById("date").innerHTML =
now.toDateString();

}

setInterval(updateClock,1000);

updateClock();


// TERMINAL LOGS

const logs=[

"Initializing AI...",
"Loading Flask Server...",
"Connecting SQLite...",
"Loading Portfolio...",
"Verifying User...",
"Neural Engine Online...",
"Security Enabled...",
"System Ready..."

];

let index=0;

setInterval(()=>{

if(index<logs.length){

document.getElementById("logs").innerHTML +=
"> "+logs[index]+"<br>";

index++;

}

},700);
setTimeout(()=>{

document.getElementById("flash").style.transition=".3s";

document.getElementById("flash").style.opacity=".9";

setTimeout(()=>{

document.getElementById("flash").style.opacity="0";

},250);

},4000);
setTimeout(()=>{

document.getElementById("welcome").innerHTML="WELCOME AYUSH";

},3000);
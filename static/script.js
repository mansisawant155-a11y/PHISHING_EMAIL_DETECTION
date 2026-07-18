// ==========================
// ELEMENTS
// ==========================

const form = document.getElementById("emailForm");
const emailText = document.getElementById("emailText");

const loading = document.getElementById("loading");
const resultCard = document.getElementById("resultCard");

const prediction = document.getElementById("prediction");
const progressBar = document.getElementById("progressBar");
const confidenceText = document.getElementById("confidenceText");


// ==========================
// SUBMIT FORM
// ==========================

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    const email = emailText.value.trim();

    if (email === "") {

        alert("Please enter an email.");

        return;
    }

    // Hide previous result
    resultCard.classList.add("hidden");

    // Show loading
    loading.classList.remove("hidden");

    try {

        // Send email to Flask backend
        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email: email
            })

        });

        const data = await response.json();

        // Hide loading
        loading.classList.add("hidden");

        // Show result card
        resultCard.classList.remove("hidden");

        // Prediction
        prediction.textContent = data.prediction;

        // Confidence
        const confidence = Math.round(data.confidence);

        confidenceText.textContent = confidence + "%";

        progressBar.style.width = confidence + "%";

        // Change colors based on prediction

        if (data.prediction === "Phishing") {

            prediction.style.color = "#ff3b3b";

            progressBar.style.background =
                "linear-gradient(90deg,#ff4b2b,#ff0000)";

        }

        else {

            prediction.style.color = "#00ff88";

            progressBar.style.background =
                "linear-gradient(90deg,#00ff88,#00d9ff)";
        }

    }

    catch (error) {

        loading.classList.add("hidden");

        alert("Server Error! Please try again.");

        console.log(error);

    }

});


// ==========================
// CLEAR RESULT WHEN USER TYPES
// ==========================

emailText.addEventListener("input", function () {

    resultCard.classList.add("hidden");

});


// ==========================
// SAMPLE EMAILS
// ==========================

const phishingExample =
`Congratulations!

You have won ₹10,00,000.

Click the link below immediately to claim your prize.

http://fake-bank-login.com

Verify your account now.`;

const safeExample =
`Hello Team,

Tomorrow's project meeting is scheduled at 10:30 AM.

Please bring your progress report.

Thank you.`;


// ==========================
// KEYBOARD SHORTCUTS
// ==========================

document.addEventListener("keydown", function (event) {

    // Ctrl + Enter = Analyze

    if (event.ctrlKey && event.key === "Enter") {

        form.requestSubmit();

    }

    // Alt + 1 = Load phishing example

    if (event.altKey && event.key === "1") {

        emailText.value = phishingExample;

    }

    // Alt + 2 = Load safe example

    if (event.altKey && event.key === "2") {

        emailText.value = safeExample;

    }

});
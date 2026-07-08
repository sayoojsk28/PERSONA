const questions = [

    {
        question: "How should your friend support you when you're feeling low?",
        image: "/static/images/support.jpg",
        options: [
            "Listen first",
            "Give advice",
            "Motivate me",
            "Make me laugh",
            "Stay calm with me"
        ]
    },

    {
        question: "How honest should your friend be?",
        image: "/static/images/honesty.png",
        options: [
            "Always honest",
            "Be gentle",
            "Challenge me",
            "Agree most of the time"
        ]
    },

    {
        question: "What kind of humor do you like?",
        image: "/static/images/humor.png",
        options: [
            "Wholesome",
            "Sarcastic",
            "Dry humor",
            "Minimal humor"
        ]
    },

    {
        question: "What energy should your friend have?",
        image: "/static/images/energy.png",
        options: [
            "Calm",
            "Balanced",
            "Energetic"
        ]
    },

    {
        question: "How should conversations feel?",
        image: "/static/images/talk.png",
        options: [
            "Deep and meaningful",
            "Casual and light",
            "Mix of both"
        ]
    },

    {
        question: "What role should your friend play in your life?",
        image: "/static/images/role.png",
        options: [
            "Best Friend",
            "Mentor",
            "Study Buddy",
            "Emotional Support",
            "Motivator"
        ]
    }

];

let current = 0;
let answers = [];

function loadQuestion() {

    document.getElementById("progress-text").innerHTML =
        `Question ${current + 1} of ${questions.length}`;

    document.getElementById("question").innerHTML =
        questions[current].question;

    document.getElementById("question-image").src =
        questions[current].image;

    document.getElementById("progress-fill").style.width =
        ((current + 1) / questions.length) * 100 + "%";

    let html = "";

    questions[current].options.forEach((option, index) => {

        html += `
            <button class="option-card" onclick="selectOption(${index})">
            ${option}
        </button>
        `;

    });

    document.getElementById("options").innerHTML = html;

    if (answers[current] != null) {

        document.querySelectorAll(".option-card")[answers[current]]
            .classList.add("selected");

    }

}

function selectOption(index) {

    answers[current] = index;

    document.querySelectorAll(".option-card").forEach(card => {

        card.classList.remove("selected");

    });

    document.querySelectorAll(".option-card")[index]
        .classList.add("selected");

}

document.getElementById("prevBtn").onclick = () => {

    if (current > 0) {

        current--;

        loadQuestion();

    }

}

document.getElementById("nextBtn").onclick = async () => {

    if (answers[current] == null) {

        alert("Please select an option.");

        return;

    }

    if (current < questions.length - 1) {

        current++;

        loadQuestion();

    }

    else {

        const response = await fetch("/analyze", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                answers: answers
            })

        });

        const data = await response.json();

        console.log(data);

        window.location.href="/friend";

    }

}

loadQuestion();
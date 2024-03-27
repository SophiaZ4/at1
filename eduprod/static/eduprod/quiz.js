document.addEventListener("DOMContentLoaded", function() {
    let currentQuestionIndex = 0;
    const questions = JSON.parse(document.getElementById('content').getAttribute('data-questions'));
    const content = document.getElementById('content');
    const btn = document.getElementById('revealBtn');

    function displayQuestion() {
        if (currentQuestionIndex < questions.length) {
            const question = questions[currentQuestionIndex].fields.question_text;
            const answer = questions[currentQuestionIndex].fields.answer_text;
            content.innerHTML = `<div class='question'>Question: ${question}</div><div class='answer' style='display: none;'>Answer: ${answer}</div>`;
            btn.textContent = "Reveal Answer";
        } else {
            content.innerHTML = "No more questions.";
            btn.style.display = "none";
        }
    }

    displayQuestion();

    btn.addEventListener("click", function() {
        const answerElement = content.querySelector('.answer');
        if (btn.textContent === "Reveal Answer") {
            answerElement.style.display = "block";
            btn.textContent = "Next Question";
        } else {
            currentQuestionIndex++;
            displayQuestion();
        }
    });
});

function markDone(taskId) {
    fetch(`/mark_done/${taskId}`, {method: 'POST'})
        .then(response => {
            if (response.ok) {
                window.location.reload(); // Reload the page after marking task as done
            }
        })
        .catch(error => {
            console.error('Error marking task as done:', error); // Error message
        });
}

function removeTask(taskId) {
    fetch(`/remove_task/${taskId}`, {method: 'POST'})
        .then(response => {
            if (response.ok) {
                window.location.reload(); // Reload the page after removing task
            }
        })
        .catch(error => {
            console.error('Error removing task:', error); // Error message
        });
}

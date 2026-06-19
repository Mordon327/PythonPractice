function validateAndSubmit(event) {
    const a = document.getElementById("field1").value;
    const b = document.getElementById("field2").value;
    const result = document.getElementById("result");

    if (a !== b) {
        event.preventDefault(); // stop form submission
        result.textContent = "The fields do not match.";
        result.style.color = "red";
    } else {
        result.textContent = ""; // clear message
        // allow form to submit normally
    }
}
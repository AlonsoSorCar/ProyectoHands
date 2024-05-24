document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("start_detection_button").addEventListener("click", function () {
        fetch("/start_detection", {
            method: "POST"
        }).then(response => response.json())
            .then(data => {
                console.log(data.message);
            })
            .catch(error => console.error("Error:", error));
    });

});

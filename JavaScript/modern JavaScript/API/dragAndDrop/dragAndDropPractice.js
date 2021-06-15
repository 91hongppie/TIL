window.onload = function() {
    var dragbox = document.getElementById("dragbox"),
        dropbox = document.getElementById("dropbox");

        dropbox.addEventListener("dragenter", function(e) {
            e.target.style.borderColor = "red";
        }, false);
        dropbox.addEventListener("dragleave", function(e) {
            e.target.style.borderColor = "gray";
        }, false);
        dropbox.addEventListener("drop", function(e) {
            e.target.style.borderColor = "blue";
        }, false);
}
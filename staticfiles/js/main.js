var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        // Close all other accordion panels
        var panel = this.nextElementSibling;
        var otherPanels = document.getElementsByClassName("panel");
        for (var j = 0; j < otherPanels.length; j++) {
            if (otherPanels[j] !== panel && otherPanels[j].style.maxHeight) {
                otherPanels[j].style.maxHeight = null;
                otherPanels[j].previousElementSibling.classList.remove("active");
            }
        }

        // Toggle the clicked accordion panel
        this.classList.toggle("active");
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}
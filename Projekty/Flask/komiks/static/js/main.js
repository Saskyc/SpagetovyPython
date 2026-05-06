// Klávesová navigace mezi stranami
document.addEventListener("keydown", (e) => {
    const dal = document.querySelector(".nav-dal");
    const zpet = document.querySelector(".nav-zpet");

    if ((e.key === "ArrowRight" || e.key === "d") && dal) {
        dal.click();
    }
    if ((e.key === "ArrowLeft" || e.key === "a") && zpet) {
        zpet.click();
    }
});

// Animace panelů při načtení stránky
document.querySelectorAll(".panel").forEach((panel, i) => {
    panel.style.opacity = "0";
    panel.style.transform = "translateY(20px)";
    setTimeout(() => {
        panel.style.transition = "opacity 0.4s ease, transform 0.4s ease";
        panel.style.opacity = "1";
        panel.style.transform = "translateY(0)";
    }, 100 + i * 80);
});

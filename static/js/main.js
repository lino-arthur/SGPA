
document.addEventListener("DOMContentLoaded", function () {

    const contrastButton = document.getElementById("contrast-toggle");

    if (!contrastButton) {
        return;
    }

    function applyContrast(enabled) {
        document.body.classList.toggle("high-contrast", enabled);

        contrastButton.setAttribute("aria-pressed", String(enabled));

        contrastButton.textContent = enabled
            ? "◐ Desativar alto contraste"
            : "◐ Alto contraste";

        contrastButton.setAttribute(
            "aria-label",
            enabled
                ? "Desativar modo de alto contraste"
                : "Ativar modo de alto contraste"
        );
    }

    let savedPreference = false;

    try {
        savedPreference = localStorage.getItem("sgpa-high-contrast") === "true";
    } catch (error) {
        savedPreference = false;
    }

    applyContrast(savedPreference);

    contrastButton.addEventListener("click", function () {

        const enabled = !document.body.classList.contains("high-contrast");

        applyContrast(enabled);

        try {
            localStorage.setItem("sgpa-high-contrast", String(enabled));
        } catch (error) {
            // O recurso continua funcionando durante a página atual.
        }
    });

});

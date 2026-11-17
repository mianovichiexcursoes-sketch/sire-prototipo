// Acrescenta um botão "Mostrar" a cada campo de senha.
// Sem este script os formulários continuam funcionando; a senha só fica oculta.
(function () {
    "use strict";

    document.querySelectorAll('input[type="password"]').forEach(function (campo) {
        var botao = document.createElement("button");
        botao.type = "button"; // não envia o formulário
        botao.className = "secundario mostrar-senha";
        botao.textContent = "Mostrar";
        botao.setAttribute("aria-pressed", "false");
        botao.setAttribute("aria-label", "Mostrar a senha digitada");

        botao.addEventListener("click", function () {
            var visivel = campo.type === "text";
            campo.type = visivel ? "password" : "text";
            botao.textContent = visivel ? "Mostrar" : "Ocultar";
            botao.setAttribute("aria-pressed", visivel ? "false" : "true");
            botao.setAttribute(
                "aria-label",
                visivel ? "Mostrar a senha digitada" : "Ocultar a senha digitada"
            );
        });

        campo.insertAdjacentElement("afterend", botao);

        // Ao enviar, a senha volta a ficar oculta (evita que o navegador a
        // memorize como texto comum).
        if (campo.form) {
            campo.form.addEventListener("submit", function () {
                campo.type = "password";
            });
        }
    });
})();

// Confere a foto ANTES do envio: tipo (JPG, PNG ou WebP) e tamanho (até 5 MB).
// Sem isso, um vídeo ou arquivo grande seria enviado inteiro ao servidor e a
// tela ficaria "carregando" até a recusa. O servidor confere de novo.
(function () {
    "use strict";

    var TIPOS = ["image/jpeg", "image/png", "image/webp"];
    var EXTENSOES = /\.(jpe?g|png|webp)$/i;

    function megas(bytes) {
        return (bytes / (1024 * 1024)).toFixed(1).replace(".", ",") + " MB";
    }

    function problema(arquivo, limite) {
        if (!arquivo) {
            return "Escolha uma foto antes de enviar.";
        }
        var tipoOk = TIPOS.indexOf(arquivo.type) !== -1 ||
            (!arquivo.type && EXTENSOES.test(arquivo.name));
        if (!tipoOk) {
            var oQue = (arquivo.type || "").indexOf("video/") === 0 ? "um vídeo" : "um arquivo que não é foto";
            return "\"" + arquivo.name + "\" é " + oQue + ". Envie somente fotos JPG, PNG ou WebP.";
        }
        if (arquivo.size > limite) {
            return "\"" + arquivo.name + "\" tem " + megas(arquivo.size) +
                ". O limite é " + megas(limite) + ". Reduza a foto e tente de novo.";
        }
        if (arquivo.size === 0) {
            return "O arquivo escolhido está vazio.";
        }
        return "";
    }

    document.querySelectorAll("input[type=file][data-limite-bytes]").forEach(function (campo) {
        var limite = parseInt(campo.getAttribute("data-limite-bytes"), 10) || 5 * 1024 * 1024;
        var aviso = document.createElement("p");
        aviso.className = "aviso-arquivo";
        aviso.setAttribute("role", "alert");
        aviso.hidden = true;
        campo.insertAdjacentElement("afterend", aviso);

        function conferir() {
            var msg = problema(campo.files && campo.files[0], limite);
            aviso.textContent = msg;
            aviso.hidden = !msg;
            return msg;
        }

        campo.addEventListener("change", function () {
            var msg = conferir();
            if (msg && campo.files && campo.files.length) {
                window.alert(msg);
                campo.value = "";
            }
        });

        if (campo.form) {
            campo.form.addEventListener("submit", function (evento) {
                var msg = conferir();
                if (msg) {
                    evento.preventDefault();
                    window.alert(msg);
                    return;
                }
                var botao = campo.form.querySelector("button[type=submit], button:not([type])");
                if (botao) {
                    botao.disabled = true;
                    botao.textContent = "Enviando foto… aguarde";
                }
            });
        }
    });
})();

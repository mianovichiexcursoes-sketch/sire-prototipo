// Controle complementar; o formulário numérico continua funcionando sem JavaScript.
(() => {
    const slider = document.getElementById('teto-preco');
    const maximo = document.getElementById('id_preco_max');
    if (!slider || !maximo) return;
    slider.parentElement.hidden = false;
    const sincronizar = () => {
        const n = Number(maximo.value);
        slider.value = maximo.value !== '' && Number.isFinite(n) ? n : slider.max;
    };
    slider.addEventListener('input', () => { maximo.value = slider.value; });
    maximo.addEventListener('input', sincronizar);
    sincronizar();
})();

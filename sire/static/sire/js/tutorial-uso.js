/* EVO-USO-01: orientação contextual; nunca envia formulários ou altera dados. */
(() => {
  'use strict';
  const role = document.body.dataset.sireRole || 'visitante';
  const key = 'sire-tutorial-v2-' + role;
  const read = (storage, name) => { try { return window[storage].getItem(name); } catch (_) { return null; } };
  const write = (storage, name, value) => { try { window[storage].setItem(name, value); } catch (_) {} };
  const main = document.querySelector('main');
  if (!main) return;
  const visible = el => el && el.getClientRects().length > 0 && !el.disabled;
  const exact = label => [...document.querySelectorAll('a, button')].find(el =>
    visible(el) && el.textContent.trim().replace(/\s+/g, ' ') === label);
  const steps = [];
  const add = (el, title, text) => { if (visible(el)) steps.push({el, title, text}); };
  const button = (label, text) => add(exact(label), label, text);
  const field = (selector, title, text) => add(main.querySelector(selector), title, text);
  field('[role="search"]', 'Encontre uma excursão', 'Informe destino, período ou tipo de pacote e clique em Pesquisar. Você pode combinar os filtros ou limpar a busca.');
  button('Ver detalhes', 'Abra a viagem que deseja conhecer. Na próxima página você verá datas, valor, vagas e pontos de embarque.');
  if (main.querySelector('dl')) field('dl', 'Confira a viagem', 'Leia destino, datas, valor e vagas antes de reservar. Confira também os pontos de embarque abaixo.');
  if (role === 'visitante') {
    button('Entre para reservar', 'Entre com sua conta de passageiro para escolher o embarque e reservar. Se ainda não tem conta, use Criar conta.');
    button('Criar conta', 'O cadastro público cria uma conta de passageiro. Agentes usam uma conta previamente vinculada à agência.');
    button('Entrar', 'Use seu usuário e senha. O sistema identifica seu perfil; não é preciso escolher Passageiro ou Agente.');
    field('#id_username', 'Seu usuário', 'Informe seu nome de usuário. No cadastro, escolha um identificador; no acesso, use o que já cadastrou.');
    field('#id_password, #id_password1', 'Sua senha', 'Digite a senha neste campo. O tutorial não lê nem armazena seus dados.');
  }
  if (role === 'passageiro') {
    button('Selecionar embarque e reservar', 'Abra a seleção do embarque. Esta ação ainda não confirma a reserva.');
    field('#id_ponto_embarque', 'Escolha o embarque', 'Selecione o local e horário em que você vai embarcar nesta excursão.');
    button('Confirmar reserva de uma vaga', 'Confira o embarque antes de clicar. Este botão registra uma vaga; não realiza pagamento. O tutorial nunca confirma por você.');
    button('Minhas reservas', 'Consulte aqui as reservas da sua conta e confira a excursão e o embarque escolhidos.');
  }
  if (role === 'agente') {
    button('Excursões da agência', 'Esta área reúne somente as excursões da agência vinculada à sua conta.');
    button('Nova excursão', 'Cadastre os dados da viagem. Ao salvar, a excursão começa como rascunho.');
    field('#id_titulo', 'Dados da excursão', 'Preencha título, destino, datas, valor e capacidade. Revise os campos antes de salvar.');
    button('Salvar excursão', 'Salve os dados preenchidos. Para uma viagem nova, o próximo passo é adicionar ao menos um embarque.');
    button('Adicionar embarque', 'Cadastre local e horário. A excursão precisa de pelo menos um embarque antes da publicação.');
    field('#id_local', 'Local de embarque', 'Informe um local claro para o passageiro encontrar.');
    field('#id_horario', 'Horário de embarque', 'Informe o horário correspondente a este local.');
    button('Salvar embarque', 'Salve e volte à lista de excursões para revisar a publicação.');
    button('Editar', 'Altere os dados da excursão. Os dados de reservas existentes devem ser preservados.');
    button('Publicar', 'Depois de conferir dados e embarques, clique para disponibilizar a excursão no catálogo. O guia não publica automaticamente.');
    button('Reservas', 'Veja as reservas desta excursão e o ponto de embarque escolhido.');
    button('Passageiros', 'Consulte os passageiros da excursão. Dados pessoais ficam restritos a usuários autorizados.');
  }
  if (!steps.length) add(main.querySelector('h1') || main, 'Nesta página', 'Confira as informações disponíveis. Use o menu para continuar e Como usar para rever a orientação.');
  const status = [...main.querySelectorAll('[role="status"]')].find(el => visible(el) && /nenhuma|não há|nenhum/i.test(el.textContent));
  if (status) add(status, 'Disponibilidade', 'A página informa o que está disponível agora. Se não houver vagas ou excursões, não é possível concluir uma nova reserva.');

  const style = document.createElement('style');
  style.textContent = `
    .sire-ajuda{cursor:pointer}.sire-guia{position:fixed;z-index:9999;bottom:1rem;right:1rem;width:min(24rem,calc(100vw - 2rem));box-sizing:border-box;max-height:70vh;overflow:auto;padding:1rem;background:#fff;color:#30212a;border:2px solid #97254e;border-radius:1rem;box-shadow:0 8px 28px #0003}
    .sire-guia[hidden]{display:none}.sire-guia h2{font-size:1.2rem;margin:.5rem 0}.sire-guia p{margin:.5rem 0}.sire-guia-acoes{display:flex;flex-wrap:wrap;gap:.5rem}.sire-guia button{min-height:44px}.sire-guia button:focus-visible,.sire-ajuda:focus-visible{outline:3px solid #8b4513;outline-offset:3px}.sire-guia-alvo{outline:4px solid #c36900!important;outline-offset:4px;scroll-margin:1rem}
    body.sire-guia-aberto{padding-bottom:var(--sire-guia-espaco,24rem)}
    @media(max-width:500px){.sire-guia{bottom:.5rem;right:.5rem;width:calc(100vw - 1rem);max-height:min(45vh,22rem);max-height:min(45dvh,22rem)}body.sire-guia-aberto{scroll-padding-bottom:50vh}}
  `;
  document.head.append(style);
  const help = document.createElement('button');
  help.type = 'button'; help.className = 'sire-ajuda secundario'; help.textContent = 'Como usar';
  help.setAttribute('aria-haspopup', 'dialog');
  (document.querySelector('header nav') || main).append(help);
  const panel = document.createElement('section');
  panel.className = 'sire-guia'; panel.hidden = true;
  panel.setAttribute('role', 'dialog'); panel.setAttribute('aria-modal', 'false');
  panel.setAttribute('aria-labelledby', 'sire-guia-titulo');
  panel.innerHTML = '<p class="sire-guia-contador" aria-live="polite"></p><h2 id="sire-guia-titulo" tabindex="-1"></h2><p class="sire-guia-texto"></p><div class="sire-guia-acoes"><button type="button" data-action="anterior">Voltar</button><button type="button" data-action="proximo">Próximo</button><button type="button" class="secundario" data-action="pular">Pular</button><button type="button" class="secundario" data-action="fechar" aria-label="Fechar tutorial">Fechar</button></div>';
  document.body.append(panel);
  const heading = panel.querySelector('h2');
  const previous = panel.querySelector('[data-action="anterior"]');
  const next = panel.querySelector('[data-action="proximo"]');
  let index = 0, target = null, offer = null;
  function clear() { target?.classList.remove('sire-guia-alvo'); target = null; }
  function position() {
    if (panel.hidden || !target) return;
    panel.style.top = ''; panel.style.bottom = '1rem';
    document.body.style.setProperty('--sire-guia-espaco', (panel.offsetHeight + 32) + 'px');
    target.scrollIntoView({block: 'center', behavior: 'instant'});
    const rect = target.getBoundingClientRect(), box = panel.getBoundingClientRect();
    if (rect.bottom > box.top && rect.top < box.bottom && rect.right > box.left && rect.left < box.right) {
      window.scrollBy({top: rect.top - 20, behavior: 'instant'});
      const after = target.getBoundingClientRect();
      if (after.bottom > panel.getBoundingClientRect().top && after.top > panel.offsetHeight + 24) {
        panel.style.bottom = 'auto'; panel.style.top = '1rem';
      }
    }
  }
  function render() {
    clear();
    const step = steps[index]; target = step.el; target.classList.add('sire-guia-alvo');
    panel.querySelector('.sire-guia-contador').textContent = `Etapa ${index + 1} de ${steps.length} nesta página`;
    heading.textContent = step.title;
    panel.querySelector('.sire-guia-texto').textContent = step.text;
    previous.disabled = index === 0; next.textContent = index === steps.length - 1 ? 'Concluir' : 'Próximo';
    heading.focus({preventScroll: true}); position();
  }
  function open() {
    offer?.remove(); offer = null; index = 0; panel.hidden = false;
    document.body.classList.add('sire-guia-aberto');
    write('localStorage', key, 'seen'); write('sessionStorage', key + '-active', 'yes'); render();
  }
  function close() {
    clear(); panel.hidden = true; document.body.classList.remove('sire-guia-aberto');
    write('localStorage', key, 'seen'); write('sessionStorage', key + '-active', 'no'); help.focus();
  }
  help.addEventListener('click', open);
  panel.addEventListener('click', event => {
    const action = event.target.closest('button')?.dataset.action;
    if (action === 'pular' || action === 'fechar') close();
    else if (action === 'anterior' && index > 0) { index--; render(); }
    else if (action === 'proximo') { if (index === steps.length - 1) close(); else { index++; render(); } }
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    if (!panel.hidden) { event.preventDefault(); close(); }
    else if (offer) { offer.remove(); offer = null; write('localStorage', key, 'seen'); help.focus(); }
  });
  window.addEventListener('resize', position);
  if (read('sessionStorage', key + '-active') === 'yes') open();
  else if (read('localStorage', key) !== 'seen') {
    offer = document.createElement('section'); offer.className = 'sire-guia';
    offer.setAttribute('aria-label', 'Conheça o SIRE');
    offer.innerHTML = '<h2>Quer conhecer o SIRE?</h2><p>Veja onde clicar, no seu ritmo. Você pode pular e voltar em Como usar.</p><div class="sire-guia-acoes"><button type="button" data-offer="start">Começar</button><button type="button" class="secundario" data-offer="skip">Agora não</button></div>';
    document.body.append(offer);
    offer.addEventListener('click', event => {
      const action = event.target.closest('button')?.dataset.offer;
      if (action === 'start') open();
      else if (action === 'skip') { offer.remove(); offer = null; write('localStorage', key, 'seen'); help.focus(); }
    });
  }
})();

/* EVO-USO-01: guia contextual sem operações de escrita, sem dados pessoais. */
(() => {
  "use strict";
  const VERSION = "evo-uso-01-v1";
  const role = document.body.dataset.sireRole || "visitante";
  const steps = role === "agente" ? [
    ["Excursões da agência", "Consulte apenas excursões da sua agência."],
    ["Nova excursão", "Cadastre a excursão; revise os dados antes de salvar."],
    ["Adicionar embarque", "Defina o local e o horário antes de publicar."],
    ["Publicar", "Publicação é uma ação sua; este guia nunca publica."],
    ["Reservas", "Consulte reservas vinculadas à sua agência."],
    ["Passageiros", "Consulte os passageiros autorizados."]
  ] : role === "passageiro" ? [
    ["Catálogo", "Encontre excursões e abra os detalhes."],
    ["Detalhes da excursão", "Confira destino, datas, preço, vagas e embarques."],
    ["Selecionar embarque e reservar", "Escolha um ponto de embarque. Sem vagas, não é possível reservar."],
    ["Confirmar reserva de uma vaga", "Confirme apenas quando estiver pronto. Reserva não é pagamento."],
    ["Minhas reservas", "Acompanhe suas reservas após entrar."]
  ] : [
    ["Catálogo", "Encontre excursões e abra os detalhes. Se não houver opções, tente novamente depois."],
    ["Entrar", "Entre na conta; o cadastro público é para Passageiro."],
    ["Criar conta", "Cadastre-se como Passageiro para reservar."],
    ["Voltar ao catálogo", "Confira destino, datas, preço, vagas e embarques nos detalhes."],
    ["Selecionar embarque e reservar", "Escolha um ponto de embarque. Sem vagas, não é possível reservar."],
    ["Confirmar reserva de uma vaga", "Confirme apenas quando estiver pronto. Reserva não é pagamento."],
    ["Minhas reservas", "Acompanhe suas reservas após entrar."]
  ];
  const style = document.createElement("style");
  style.textContent = `
    .sire-ajuda { margin-inline:.5rem; cursor:pointer }
    .sire-guia { position:fixed; z-index:9999; bottom:1rem; right:1rem; width:min(23rem,calc(100vw - 2rem)); padding:1rem; background:#fff; color:#20202b; border:2px solid #5543a9; border-radius:.8rem; box-shadow:0 8px 28px #0004 }
    .sire-guia[hidden], .sire-guia-convite[hidden] {display:none}
    .sire-guia button { margin:.3rem; min-height:2.5rem }
    .sire-guia button:focus-visible,.sire-ajuda:focus-visible {outline:3px solid #e08a00;outline-offset:3px}
    .sire-guia-alvo { outline:4px solid #e08a00!important; outline-offset:4px; position:relative; z-index:2 }
    @media(max-width:500px){.sire-guia{bottom:0;right:0;width:100%;box-sizing:border-box;border-radius:.8rem .8rem 0 0}}
  `;
  document.head.append(style);
  const help = document.createElement("button");
  help.type = "button"; help.className = "sire-ajuda secundario"; help.textContent = "Como usar";
  help.setAttribute("aria-haspopup","dialog");
  (document.querySelector("header nav") || document.querySelector("header") || document.body).append(help);
  const dialog = document.createElement("section");
  dialog.className = "sire-guia"; dialog.hidden = true;
  dialog.setAttribute("role","dialog"); dialog.setAttribute("aria-modal","false");
  dialog.setAttribute("aria-label","Tutorial de uso do SIRE");
  dialog.innerHTML = '<p class="sire-guia-contador"></p><h2 class="sire-guia-titulo"></h2><p class="sire-guia-texto"></p><p class="sire-guia-situacao" role="status"></p><div><button type="button" data-action="anterior">Anterior</button><button type="button" data-action="proximo">Próximo</button><button type="button" data-action="pular">Pular / Fechar</button></div>';
  document.body.append(dialog);
  const title = dialog.querySelector(".sire-guia-titulo"), body = dialog.querySelector(".sire-guia-texto");
  const count = dialog.querySelector(".sire-guia-contador"), situation = dialog.querySelector(".sire-guia-situacao");
  let index=0, active=null, opener=help, invitation=false;
  const storageKey="sire-tutorial-"+VERSION+"-"+role;
  function remember(){try{localStorage.setItem(storageKey,"seen")}catch(_e){}}
  function findTarget(label) {
    return [...document.querySelectorAll('a,button,h1,h2,nav a')].find(el =>
      !dialog.contains(el) && !help.contains(el) && el.textContent.trim().toLocaleLowerCase("pt-BR").includes(label.toLocaleLowerCase("pt-BR")));
  }
  function clearTarget(){if(active){active.classList.remove("sire-guia-alvo");active=null}}
  function render(){
    clearTarget();
    const [label, description]=steps[index];
    count.textContent="Etapa "+(index+1)+" de "+steps.length;
    title.textContent=label; body.textContent=description;
    active=findTarget(label);
    if(active){active.classList.add("sire-guia-alvo");situation.textContent="Elemento destacado nesta página."; }
    else situation.textContent="Esta ação pode estar em outra página, depender do seu perfil ou não estar disponível agora. Continue pelo menu quando estiver disponível.";
    dialog.querySelector('[data-action="anterior"]').disabled=index===0;
    dialog.querySelector('[data-action="proximo"]').textContent=index===steps.length-1?"Concluir":"Próximo";
    dialog.querySelector('[data-action="proximo"]').focus();
  }
  function open(from,invite=false){opener=from||help;invitation=invite;index=0;dialog.hidden=false;render()}
  function close(){clearTarget();dialog.hidden=true;remember();opener?.focus()}
  help.addEventListener("click",()=>open(help));
  dialog.addEventListener("click",e=>{
    const action=e.target.closest("button")?.dataset.action;
    if(action==="pular")close();
    if(action==="anterior" && index>0){index--;render()}
    if(action==="proximo"){if(index===steps.length-1)close();else{index++;render()}}
  });
  document.addEventListener("keydown",e=>{if(e.key==="Escape"&&!dialog.hidden){e.preventDefault();close()}});
  let seen=false;try{seen=localStorage.getItem(storageKey)==="seen"}catch(_e){}
  if(!seen){
    const offer=document.createElement("div");
    offer.className="sire-guia";offer.setAttribute("role","region");offer.setAttribute("aria-label","Convite para conhecer o SIRE");
    offer.innerHTML='<p>Quer conhecer o SIRE?</p><button type="button" data-offer="start">Começar</button><button type="button" data-offer="skip">Agora não</button>';
    document.body.append(offer);
    offer.addEventListener("click",e=>{
      const action=e.target.closest("button")?.dataset.offer;
      if(!action)return;
      const source=help;offer.remove();
      if(action==="start")open(source,true);else remember();
    });
  }
})();
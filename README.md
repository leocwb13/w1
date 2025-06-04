# Diagnóstico Financeiro

Este repositório contém o código do site **consultoria.leonardograciano.com.br**, hospedado no GitHub Pages. Aqui você encontrará as páginas de diagnóstico financeiro, o blog e recursos estáticos utilizados pelo site.

## Geração automática dos posts do blog

Os artigos são escritos em Markdown dentro da pasta [`drafts/`](./drafts). Quando um arquivo `.md` é enviado para o repositório, a _workflow_ [`make-post.yml`](./.github/workflows/make-post.yml) é executada automaticamente. Esta ação converte o Markdown em HTML usando **pandoc**, gera o layout do post a partir do template [`partials/template-post.html`](./partials/template-post.html) e atualiza:

- a página de índice do blog (`blog/index.html`),
- o sitemap (`sitemap.xml`),
- o próprio arquivo Markdown, que é movido para `drafts/_done_...`.

Após a conversão, o bot faz o commit e envia as mudanças para o repositório. Portanto, basta adicionar um Markdown com título (linha iniciada com `#`) na pasta `drafts` e fazer _push_ para publicá‑lo.

## Deploy e visualização

A publicação acontece via GitHub Pages através da workflow [`deploy.yml`](./.github/workflows/deploy.yml). Sempre que houver commits na branch `main`, o site é implantado automaticamente em `consultoria.leonardograciano.com.br`.

Para pré‑visualizar localmente, clone o projeto e abra qualquer arquivo HTML do diretório em seu navegador. Não há passos de build manual, pois todo processamento é feito pelas ações do GitHub.

### Variáveis de ambiente

A action de deploy substitui tokens nos HTML usando dois segredos configurados no repositório:

- `WEBHOOK_URL` – URL para onde os formulários são enviados.
- `WHATSAPP` – número usado nos links do WhatsApp (apenas dígitos, exemplo `5541999999999`).

Se for fazer deploy manualmente ou pré‑visualizar o site com as URLs reais, defina essas variáveis e substitua os tokens `{{WEBHOOK_URL}}` e `{{WHATSAPP}}` antes de publicar.

## Testes

No momento não existem testes automatizados. Quando forem adicionados, configure o ambiente instalando as dependências indicadas (por exemplo, `npm install` ou `pip install -r requirements.txt`) e execute a ferramenta de testes definida pelo projeto. Atualize este README conforme necessário.

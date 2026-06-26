# Leitor de Contatos e Disparo Automático 🚀

Este projeto realiza a leitura de contatos armazenados no banco de dados Supabase e efetua o disparo automático de mensagens via WhatsApp utilizando a API da Z-API.

## 🛠️ Tecnologias Utilizadas

* **Python 3** — Linguagem base do script.
* **Supabase** — Banco de dados PostgreSQL como serviço.
* **Z-API** — API de integração e automação do WhatsApp.

## 🗄️ Configuração do Banco de Dados (Supabase)

Crie uma tabela chamada `contacts` no seu projeto do Supabase seguindo os passos abaixo:

1. Acesse o **Table Editor** no painel do Supabase.
2. Clique em **New Table** e defina o nome como `contacts`.
3. Adicione as seguintes colunas:
   * `name` (text) — Nome do contato.
   * `phone` (text) — Número de telefone. *Exemplo de formato: `5515981358461`*

## ⚙️ Configuração do Ambiente

Siga os comandos abaixo no seu terminal para clonar o repositório e configurar o ambiente virtual.

### 1. Clonar o repositório
```bash
git clone <LINK_DO_SEU_REPO>
cd <NOME_DA_PASTA>
```

### 2. Criar e ativar o ambiente virtual (Venv)
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/Mac
source venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente
Crie um arquivo chamado `.env` na raiz do seu projeto e adicione as suas credenciais:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_secret_key_do_supabase
ZAPI_INSTANCE_ID=seu_id_da_instancia
ZAPI_TOKEN=seu_token_da_instancia
```

## 🚀 Como Executar

Com o ambiente virtual ativo e o arquivo `.env` configurado, execute o script principal:

```bash
python main.py
```
## 🔒 Segurança
Este projeto utiliza um arquivo .gitignore para garantir que arquivos sensíveis, como o .env, não sejam versionados publicamente no GitHub.

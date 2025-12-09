**BMO - AI Terminal Companion**

**Projeto:** Assistente virtual via CLI (Interface de Linha de Comando) focado em respostas concisas e humanizadas. Status: Funcional / MVP

**Sobre o Projeto**

Desenvolvi um agente conversacional integrado ao terminal para fornecer assistencia rapida e organizada, eliminando a complexidade visual de interfaces graficas. A solucao utiliza Python e LangChain para orquestrar o fluxo de conversacao, atingindo uma experiencia de usuario focada e responsiva atraves da integracao com a API do Google Gemini.

O diferencial deste projeto e a implementacao de uma persona (BMO) instruida via System Prompt para manter interacoes concisas, objetivas e amigaveis, priorizando frases curtas para otimizar a leitura e a eficiencia da comunicação.

**Tecnologias e Decisoes Arquiteturais**

Por que Google Gemini?
A escolha do modelo Google Gemini (familia Flash) foi baseada em dois pilares estrategicos:

Acessibilidade e Custo-Eficiencia: A API do Gemini oferece um Free Tier robusto, permitindo o desenvolvimento de aplicacoes reais e testes de integracao sem barreiras financeiras iniciais, ideal para escalabilidade de projetos pessoais.

Equilibrio de Performance: O modelo Flash foi selecionado por sua arquitetura otimizada para tarefas de alta frequencia e baixa complexidade. Embora nenhuma requisicao via API seja instantanea, este modelo oferece uma baixa latencia competitiva, garantindo que a interacao no terminal seja agil o suficiente para manter a fluidez da conversa.

**Stack Tecnologica:**

1. Linguagem: Python 3.x

2. Orquestracao de IA: LangChain (Core & Google GenAI)

3. Gerenciamento de Ambiente: Python-dotenv

4. Interface: CLI (Standard Output)

**Funcionalidades**

Persistencia de Contexto: O bot gerencia o historico da sessao ativa (Memory), permitindo conversas coerentes.

Engenharia de Prompt (Persona BMO): System Prompt calibrado para emular uma personalidade atenciosa e organizada, com instrucoes explicitas para respostas curtas, evitando textos desnecessariamente longos.

Resiliencia: Implementacao de tratamento de erros (try/except) para capturar falhas na chamada da API ou interrupcoes do usuario, mantendo a aplicacao estavel.

**Como Executar**

Pre-requisitos:

1. Python instalado.

2. Uma API Key do Google AI Studio.

**Instalacao**

1. Clone o repositorio:

```
git clone https://github.com/seu-usuario/bmo-chatbot.git
cd bmo-chatbot
```
2. Instale as dependencias:

```
pip install langchain-google-genai langchain-core python-dotenv
```

3. Configure o ambiente: Crie um arquivo .env na raiz do projeto e adicione sua chave e o modelo desejado:

```
GOOGLE_API_KEY="sua-chave-aqui"
GEMINI_MODEL="gemini-1.5-flash"
```

4. Execute o chatbot:

```
python app.py
```

**Exemplo de Uso**

```
CHAT ATIVO --- DIGITE 'sair' PARA ENCERRAR

Você: Preciso arrumar meus arquivos.
BMO: Oh, isso parece importante. Vamos Organizar tudo, amigo.

Você: O que voce sugere?
BMO: Comece separando por categorias. Guardar com carinho e essencial!
```

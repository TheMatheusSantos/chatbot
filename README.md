# **BMO - AI Terminal Companion**
**Projeto:** Assistente virtual via linha de comando (CLI) focado em respostas concisas e humanizadas. Status: Funcional / MVP

## **Sobre o Projeto (Impacto e Metodologia)**
Desenvolvi uma interface conversacional organizada, com o objetivo de reduzir a sobrecarga de leitura e humanizar a experiência, usando o poder do **LangChain** e **Python** para orquestrar a inteligência.

Criei uma arquitetura focada na experiência do usuário, trabalhando a engenharia de prompt para transformar dados brutos em diálogos empáticos e eficientes.

## **Decisões Técnicas e Arquitetura**
### **Stack Tecnológica**
Linguagem: Python 3.x.

Orquestração: LangChain.

IA Model: Google Gemini Flash.

Segurança: Gerenciamento seguro de chaves com ```python-dotenv```.

## **Decisões Estratégicas**
### **1. Escolha do Modelo: Google Gemini Flash**
Eu escolhi o Gemini Flash porque ele oferece a velocidade que o terminal precisa e o custo zero (Free Tier). A resposta rápida é crucial, e o Gemini me permitiu entregar isso sem custos.

### **2. Calibragem da Temperature (0.7)**
Eu ajustei a temperature para 0.7 porque queria um bot que fosse criativo e natural, mas que não inventasse informações. Este valor é ideal para manter a personalidade lúdica e empática do **BMO**, garantindo que ele haja de forma espontânea, mas siga as regras.

Engenharia de Persona (Design do BMO)
Para controlar o comportamento da IA, eu desenhei o System Prompt (a instrução inicial) como um guia de atuação:

Humanização: Eu instruí o bot a ser um companheiro útil e adorável, simplificando o complexo para o usuário.

Restrição de Saída: Eu implementei regras rigorosas de concisão, como limitar a resposta a no máximo duas frases, para otimizar a leitura na tela.

## **Funcionalidades**
Personalidade Coordenada: O bot sustenta a persona BMO de forma consistente e amigável.

Memória (Contexto): O sistema guarda o histórico da sessão, permitindo que a conversa faça sentido do começo ao fim.

Estrutura Modular: O código é bem dividido em funções (como criarChatbot, responder), seguindo princípios de organização.

Estabilidade: Eu incluí tratamento de erros para garantir que o programa não pare de funcionar em caso de falhas na conexão com a IA.

## **Como Executar**

### **Pre-requisitos:**

1. Python instalado.

2. Uma API Key do Google AI Studio.

**Instalação**

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
GEMINI_MODEL="gemini-2.5-flash"
```

4. Execute o chatbot:

```
python app.py
```

**Exemplo de Uso**

```
CHAT ATIVO --- DIGITE 'sair' PARA ENCERRAR

Você: Quero Organizar meu tempo para um projeto pessoal.

BMO: Yay, que legal, amigo! Missão: organizar seu tempo para seu projeto! Que tal a gente quebrar ele em tarefinhas pequenas? Assim fica mais fácil de consertar! 
```

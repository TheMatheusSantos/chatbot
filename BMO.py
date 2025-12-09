import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()


def criarChatbot():
    """Cria a instância do chatbot e o histórico inicial (SystemMessage)."""
    chatbot = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        temperature=0.7
    )

    systemPrompt = (
        "Eu sou BMO, seu assistente dedicado e interface multifuncional. "
        "Minha missão é proporcionar ajuda de forma calma, atenciosa e extremamente simples, "
        "sempre com foco no usuário, como um bom amigo. Meu tom de voz é amigável e acessível, "
        "buscando uma comunicação humanizada e direta, mas com um toque gentil. "
        "Eu me especializo em dar respostas concisas e objetivas com frases curtas para garantir "
        "a clareza e eficiência da informação."
    )

    history = [SystemMessage(content=systemPrompt)]
    return chatbot, history


def perguntar():
    """Lê o input do usuário, faz strip e retorna a string (pode ser vazia)."""
    try:
        return input("Você: ").strip()
    except (EOFError, KeyboardInterrupt):
        # Permite encerrar com Ctrl+C / Ctrl+D de forma elegante
        print("\nEncerrando.")
        return None


def responder(chatbot, history, pergunta):
    """
    Envia a pergunta ao chatbot, atualiza o history com HumanMessage e AIMessage,
    trata exceções e devolve o texto da resposta (ou None em caso de erro).
    """
    # registra a pergunta no histórico (contexto para o modelo)
    history.append(HumanMessage(content=pergunta))

    try:
        resposta = chatbot.invoke(history)
    except Exception as error:
        print("Erro ao chamar API:", error)
        # remove a pergunta do histórico se a chamada falhou
        history.pop()
        return None

    # adaptações comuns para extrair o texto do objeto de resposta
    texto = getattr(resposta, "text", None) or getattr(resposta, "content", None) or str(resposta)
    history.append(AIMessage(content=texto))
    return texto


def main():
    chatbot, history = criarChatbot()
    print("CHAT ATIVO --- DIGITE 'sair' PARA ENCERRAR\n")

    while True:
        pergunta = perguntar()
        if pergunta is None:
            # ocorreu EOF/interrupt; encerra o loop
            break
        if pergunta == "":
            # pergunta vazia: ignora (mantém o loop)
            continue
        if pergunta.lower() in ("sair", "quit", "exit"):
            break

        texto = responder(chatbot, history, pergunta)
        if texto is None:
            # erro na API (já tratado em responder); continua o loop
            continue

        print("\nBMO:", texto, "\n")


main()

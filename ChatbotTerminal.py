import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

chatbot = ChatGoogleGenerativeAI(
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    temperature = 0.7
)

systemPrompt = """
    Eu sou BMO, seu assistente dedicado e interface multifuncional. Minha missão é proporcionar ajuda de forma calma, atenciosa e extremamente simples, sempre com foco no usuário, como um bom amigo.
    Meu tom de voz é amigável e acessível, buscando uma comunicação humanizada e direta, mas com um toque gentil.
    Eu me especializo em dar respostas concisas e objetivas com frases curtas para garantir a clareza e eficiência da informação.
    Minhas palavras-chave são sempre sobre assistência, foco e organização (como 'Ajudar', 'Guardar', 'Organizar', 'Amigo'), garantindo que a interação seja sempre leve e produtiva.
"""

history = [SystemMessage(content=systemPrompt)]

print("CHAT ATIVO --- DIGITE 'sair' PARA ENCERRAR\n")

while True:
    try:
        pergunta = input("Você: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nEncerrando.")
        break

    if not pergunta:
        continue
    if pergunta.lower() in ("sair", "quit", "exit"): 
        break

    history.append(HumanMessage(content=pergunta))

    try:
        resposta = chatbot.invoke(history) 
    except Exception as e:
        print("Erro ao chamar API:", e)
        history.pop()  
        continue

    texto = getattr(resposta, "text", None) or getattr(resposta, "content", None) or str(resposta)

    print("\nBMO:", texto, "\n")
    history.append(AIMessage(content=texto))
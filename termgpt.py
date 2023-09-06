import openai
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests

# Chargez la configuration depuis un fichier JSON
def load_config(config_path="config.json"):
    try:
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        print("Le fichier de configuration n'a pas été trouvé. Veuillez créer un fichier 'config.json' avec votre clé d'API.")
        exit(1)

# Initialisation de l'analyseur de sentiment
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Fonction pour détecter l'humeur
def detect_mood(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return "positive"
    elif sentiment['compound'] <= -0.05:
        return "negative"
    else:
        return "neutre"

# Fonction pour interagir avec l'API GPT-3
def ask_gpt3(prompt, max_tokens=50):
    config = load_config()
    api_key = config.get("api_key")
    
    if not api_key:
        print("La clé d'API n'a pas été trouvée dans le fichier de configuration.")
        exit(1)

    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Une erreur s'est produite lors de la requête à l'API GPT-3:", str(e))
        return None

# Fonction pour effectuer une recherche sur le web
def search_web(query):
    api_key = "VOTRE_CLE_API"
    search_engine_id = "VOTRE_ID_MOTEUR_DE_RECHERCHE"

    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    
    response = requests.get(url)
    data = response.json()

    # Traitez et affichez les résultats
    if 'items' in data:
        for item in data['items']:
            print(item['title'], item['link'])
    else:
        print("Aucun résultat trouvé.")

# Fonction pour gérer une conversation
def chat():
    conversation = []
    
    print(f"Bienvenue dans le ChatGPT. Tapez 'exit' ou 'quit' pour quitter.")
    
    while True:
        user_input = input("Vous: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("ChatGPT: Au revoir !")
            break
        
        mood = detect_mood(user_input)
        if mood == "positive":
            print("ChatGPT: C'est génial de vous entendre heureux !")
        elif mood == "negative":
            print("ChatGPT: Je suis là pour vous écouter si vous avez besoin de parler.")
        else:
            print("ChatGPT: Comment puis-je vous aider ?")
        
        conversation.append(f"Vous: {user_input}")
        
        response = ask_gpt3("\n".join(conversation), max_tokens=100)
        
        if response:
            print("ChatGPT:", response)
            conversation.append(f"ChatGPT: {response}")

# Fonction d'aide
def show_help():
    print("Commandes disponibles:")
    print("- 'exit' ou 'quit' : pour quitter le chat.")
    print("- 'help' : pour afficher cette aide.")
    print("- 'clear' : pour effacer la conversation.")
    print("- 'Recherche : [votre recherche]' : pour effectuer une recherche sur le web.")

# Boucle principale
while True:
    command = input("\nTapez 'chat' pour commencer ou 'quit' pour quitter: ")
    
    if command.lower() == "quit":
        print("Au revoir !")
        break
    elif command.lower() == "chat":
        chat()
    elif command.lower() == "help":
        show_help()
    elif command.lower() == "clear":
        conversation = []
        print("Conversation effacée.")
    else:
        if command.lower().startswith("recherche :"):
            query = command[10:]
            search_web(query)
        else:
            print("Commande non reconnue. Tapez 'chat' pour commencer ou 'help' pour afficher l'aide.")

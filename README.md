## TermGPT

<div align="center">
 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="200" alt="python logo"  />
  <img width="72" />
</div>

TermGPT est un chatbot polyvalent alimenté par GPT-3 d'OpenAI et développé par Xeush0flex. Il peut vous aider dans diverses tâches, notamment répondre à des questions, fournir des informations, effectuer des recherches sur le web et même convertir des devises. Ce README fournit un aperçu de l'utilisation efficace de TermiFlex.

Pour commencer

1. Clonez ce dépôt sur votre machine locale.

2. Installez les packages python requis en exécutant la commande suivante :

 ```
   pip install openai json nltk.sentiment.vader requests
 ```

3. Configurez vos clés API :

   - API OpenAI : Remplacez `VOTRE_CLE_API_OPENAI` dans config.json par votre clé API OpenAI.
   - API Google Custom Search JSON : Remplacez `VOTRE_CLE_API` et `VOTRE_ID_MOTEUR_DE_RECHERCHE` dans le code par votre clé API Google et votre ID de moteur de recherche personnalisé.
   - API Open Exchange Rates : Remplacez `VOTRE_CLE_API_EXCHANGE_RATE` dans le code par votre clé API Open Exchange Rates.

4. Démarrez le chatbot en exécutant :

 ```
   python termgpt.py
 ```

Fonctionnalités

- TermGPT peut engager des conversations naturelles avec les utilisateurs.
- Il analyse l'humeur de l'utilisateur et répond en conséquence.
- Vous pouvez lui demander d'effectuer des recherches sur le web en tapant "Recherche : [votre requête]."
- La conversion de devises est possible avec des commandes telles que "convertir 10 USD en EUR."
- Vous pouvez enregistrer et charger des conversations précédentes pour référence.

Utilisation

- Tapez `chat` pour commencer une conversation avec TermiFlex.
- Tapez `exit` ou "quit" pour quitter la discussion.
- Tapez `help` pour afficher la liste des commandes disponibles.
- Tapez `clear` pour supprimer l'historique de la conversation.
- Tapez `save` pour enregistrer la conversation actuelle.
- Tapez `charger` pour charger une conversation précédemment enregistrée.

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des améliorations ou de nouvelles fonctionnalités à suggérer, veuillez créer une pull request.

<div align="center">
<a href="https://instagram.com/xeush0flex" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/instagram/default.svg" width="80" height="60" alt="instagram logo"  />
  </a>
  <a href="https://t.me/xeush0flex" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/telegram/default.svg" width="80" height="60" alt="telegram logo"  />
  </a>
</div>

Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

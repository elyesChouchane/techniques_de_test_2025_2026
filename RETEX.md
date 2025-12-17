# RETEX - Retour d'Expérience

## Ce qui a bien fonctionné
- **L'outillage :** L'utilisation combinée de `pytest` pour les tests et `ruff` pour le linting a permis de maintenir un code très propre dès le début. Le `Makefile` a grandement simplifié l'exécution des tâches répétitives.
- **L'architecture :** La séparation claire entre le code source (`src`) et les tests (`tests`) rend le projet lisible et professionnel.

## Difficultés rencontrées et Évolution
- **La confrontation Théorie vs Réalité :**
  Initialement, j'avais une vision très "mathématique" du projet (une simple fonction de calcul). J'ai réalisé en cours de route que pour respecter l'architecture demandée (Composant interfacé), je devais passer d'une simple fonction à une Classe `Triangulator` avec injection de dépendance (`PointSetManager`).

- **L'impact sur les tests :**
  Ce changement d'architecture a cassé mes premiers tests. J'ai appris que les tests ne sont pas figés : ils doivent évoluer en même temps que l'architecture. Je suis passé de tests "boîte noire" simples à des tests utilisant des **Mocks** pour isoler mon composant de la base de données.

## Ce que je ferais différemment
- Je commencerais plus tôt par définir les interfaces (les Classes vides) avant d'écrire l'algorithme mathématique, pour éviter d'avoir à refactorer le code et les tests à la fin.
- Je mettrais en place le `pytest.ini` dès le début pour éviter les problèmes d'import (`ModuleNotFoundError`) qui m'ont fait perdre du temps au démarrage.

## Conclusion
Ce projet m'a permis de comprendre qu'un bon test n'est pas seulement un test qui passe, mais un test qui isole correctement la responsabilité du composant (grâce au Mocking).
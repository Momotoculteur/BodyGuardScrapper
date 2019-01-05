# Infos
Code source du tutoriel de https://deeplylearning.fr/cours-pratiques-deep-learning/detecteur-de-harcelement/

Exemple d'utilisation d'un crawler. Je vous montre une simple utilisation de BeautifulSOup4 pour extraire des données en parcourant un site web BodyGuard pour permettre de constituer un début de dataset afin de créer un réseau de neurones qui va réaliser de la détection de harcelement.

## Composition du projet

| Attribut | Description                    |
| ------------- | ------------------------------ |
| `ScrapperV2.py`      | Permet de récuperer les données      |
| `data.txt`   | Données brutes extraite du site    |
| `cleanData.txt`   | Données néttoyés de doublons, phrases incomplétes, etc.    | 
| `toolbox.py`   | Permet de nettoyer les données de data.txt vers cleanData.txt en appliquand divers filtres    | 

# Documentation de G-OS Theme

Ce manuel accompagne le thème G-OS destiné à GNOME 51. Il explique son installation, son organisation, les règles de personnalisation et la validation du rendu. Il s'adresse aux personnes qui découvrent les thèmes GNOME comme aux contributeurs qui souhaitent modifier le thème proprement.

## Parcours conseillé

1. [Présentation et architecture](01-architecture.md)
2. [Installation, activation et retour arrière](02-installation.md)
3. [Comprendre et modifier les feuilles CSS](03-css-et-personnalisation.md)

## Périmètre

Le dépôt fournit des styles pour GNOME Shell, GTK 3 et GTK 4/Libadwaita. Ces environnements n'utilisent pas exactement les mêmes moteurs ni les mêmes sélecteurs. Une règle CSS valide dans GTK n'est pas nécessairement valide dans GNOME Shell.

Le manuel distingue donc explicitement les trois cibles. Il ne promet pas de personnaliser les éléments que GNOME ou Libadwaita ne rendent pas configurables par un thème.

## Principes

- Travailler dans une copie du dépôt et conserver des changements ciblés.
- Ne jamais modifier les fichiers système de GNOME pour installer le thème.
- Tester les variantes claire et sombre.
- Vérifier le rendu sur GNOME 51 réel : les détails internes du Shell peuvent changer.
- Préférer les règles simples, lisibles et faciles à retirer.
- Garder toutes les ressources du thème dans le dépôt ; aucune ressource distante n'est nécessaire à l'exécution.

## Contribuer à la documentation

Chaque chapitre doit expliquer le rôle du composant, indiquer le fichier source concerné, fournir un exemple minimal, détailler les effets attendus et proposer une méthode de vérification. Les captures doivent représenter le thème réellement exécuté, pas une maquette approximative.

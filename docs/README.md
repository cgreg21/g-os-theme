# Documentation G-OS Theme

Ce manuel accompagne G-OS, un thème communautaire destiné à GNOME 51. Il présente les composants, leur installation et les méthodes pour adapter le rendu sans modifier inutilement les fichiers sources.

## Parcours conseillé

1. [Architecture du thème](01-architecture.md) — comprendre ce qui relève de GNOME Shell, GTK 3, GTK 4 et Libadwaita.
2. [Installation et activation](02-installation.md) — installer, activer, vérifier et désinstaller le thème.
3. [CSS et personnalisation](03-css-et-personnalisation.md) — comprendre les règles, les couleurs, les états et les sélecteurs.

## Principe important

GNOME Shell, GTK 3 et GTK 4 n'utilisent pas exactement le même moteur CSS. Une règle valide dans un fichier GTK n'est pas nécessairement valide dans GNOME Shell. Libadwaita limite volontairement la prise en charge des thèmes GTK tiers : ses applications peuvent conserver leur apparence Adwaita même si les fichiers GTK 4 sont installés.

La réussite de la CI vérifie les fichiers et le script d'installation, pas le rendu graphique de chaque application.

# Documentation G-OS Theme

Ce manuel accompagne G-OS, un thème communautaire destiné à GNOME 51. Il présente les composants, leur installation et les méthodes pour adapter le rendu sans modifier inutilement les fichiers sources.

## Parcours conseillé

1. [Architecture du thème](01-architecture.md) — comprendre ce qui relève de GNOME Shell, GTK 3, GTK 4 et Libadwaita.
2. [Installation et activation](02-installation.md) — installer, activer, vérifier et désinstaller le thème.
3. [CSS et personnalisation](03-css-et-personnalisation.md) — comprendre les règles, les couleurs, les états et les sélecteurs.
4. [GNOME Shell : composants](04-gnome-shell-composants.md) — barre supérieure, menus, Quick Settings, calendrier, notifications, dash et dialogues.
5. [GTK 3 : widgets](05-gtk3-widgets.md) — boutons, champs, en-têtes, listes, sélections et contrôles.
6. [GTK 4 et Libadwaita](06-gtk4-libadwaita.md) — couleurs sémantiques, cartes, popovers et limites de personnalisation.
7. [Palette et mode sombre](07-palette-couleurs-mode-sombre.md) — rôles de couleur, cohérence et validation des deux variantes.
8. [Diagnostic et dépannage](08-diagnostic-depannage.md) — identifier le moteur, vérifier le chargement, lire les journaux et préparer un rapport de bug.

## Règles de lecture

Les exemples sont tirés des fichiers actuels du dépôt lorsqu'ils sont présentés comme des règles G-OS. Un exemple CSS générique est signalé comme tel. Les sélecteurs internes du Shell et les styles des applications doivent toujours être vérifiés dans la version ciblée.

## Limites de compatibilité

GNOME Shell, GTK 3 et GTK 4 n'utilisent pas exactement le même moteur CSS. Une règle valide dans un fichier GTK n'est pas nécessairement valide dans GNOME Shell. Libadwaita limite volontairement la prise en charge des thèmes GTK tiers : ses applications peuvent conserver leur apparence Adwaita même si les fichiers GTK 4 sont installés.

La CI valide les fichiers et le script d'installation ; elle ne remplace pas les essais graphiques sur une session GNOME 51.

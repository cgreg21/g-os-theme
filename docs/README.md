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
9. [Typographie et Fontconfig](09-typographie-fontconfig.md) — installer des polices, comprendre les familles de repli et régler la typographie.
10. [Icônes et icônes symboliques](10-icones-symboliques.md) — distinguer icônes d'applications, icônes symboliques et thème d'icônes.
11. [Curseurs et effets visuels](11-curseurs-ombres-transparence.md) — comprendre Xcursor, ombres, transparence, rayons et transitions.
12. [Contrôles avancés](12-controles-avances.md) — états, boutons, champs, listes, cases à cocher, curseurs et progressions.
13. [Échelle et accessibilité](13-echelle-responsive-accessibilite.md) — tailles de texte, mise à l'échelle, contraste, focus clavier et animations.
14. [Extensions GNOME Shell](14-extensions-gnome-shell.md) — identifier les classes d'extensions, personnaliser leurs composants et éviter les conflits.
15. [Inspection et débogage CSS](15-inspection-debogage-css.md) — inspecteur GTK, journaux Shell, cascade et diagnostic reproductible.
16. [Maintenance et publication](16-structure-maintenance-publication.md) — structure du dépôt, contrôles locaux, CI et publication fiable.

## Règles de lecture

Les exemples sont tirés des fichiers actuels du dépôt lorsqu'ils sont présentés comme des règles G-OS. Un exemple CSS générique est signalé comme tel. Les sélecteurs internes du Shell et les styles des applications doivent toujours être vérifiés dans la version ciblée.

## Limites de compatibilité

GNOME Shell, GTK 3 et GTK 4 n'utilisent pas exactement le même moteur CSS. Une règle valide dans un fichier GTK n'est pas nécessairement valide dans GNOME Shell. Libadwaita limite volontairement la prise en charge des thèmes GTK tiers : ses applications peuvent conserver leur apparence Adwaita même si les fichiers GTK 4 sont installés.

La CI valide les fichiers et le script d'installation ; elle ne remplace pas les essais graphiques sur une session GNOME 51.

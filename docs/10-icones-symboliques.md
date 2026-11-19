# Icônes, icônes symboliques et thèmes d'icônes

G-OS fournit deux thèmes Freedesktop : **G-OS** (clair) et **G-OS-dark** (sombre), inspirés du langage visuel macOS : silhouettes arrondies, dégradés subtils et couleurs distinctes.

## Organisation

Les ressources sont générées par `scripts/generate-icons.py` :

- `icons/G-OS/` : variante claire.
- `icons/G-OS-dark/` : variante sombre.
- `512x512/apps/` : logo GNOME en SVG 512 × 512.
- `scalable/apps/` : icônes d'applications SVG.
- `scalable/actions/` : commandes symboliques.
- `scalable/status/` : états symboliques.
- `scalable/places/` : dossiers et emplacements.
- `scalable/mimetypes/` : types de fichiers.

Chaque variante possède son `index.theme` et hérite d'Adwaita et hicolor pour les noms non couverts. Le logo GNOME est fourni seul, en monochrome noir sur fond clair et blanc sur fond sombre, sans l'intégrer dans une vignette. Le nom et le pied GNOME sont des marques de la GNOME Foundation ; vérifier ses règles et obtenir les autorisations nécessaires avant toute redistribution publique du logo.

## Couverture

Le générateur fournit 33 identifiants d'applications GNOME et Firefox, avec des icônes carrées 512 × 512 redimensionnables. Les pictogrammes symboliques couvrent navigation, édition, fichiers, recherche, préférences, fenêtres, zoom, médias, audio, réseau, batterie, Bluetooth, verrouillage, alertes et états usuels.

Les symboliques utilisent une grille 24 × 24 et un tracé homogène de 1,8 px. Le premier plan est sombre dans G-OS et clair dans G-OS-dark. Les noms utilisent le suffixe Freedesktop `-symbolic`.

## Installation

`install.sh` génère les ressources puis les installe dans `~/.local/share/icons`. Sélectionner une seule variante :

```sh
gsettings set org.gnome.desktop.interface icon-theme 'G-OS'
# variante sombre :
gsettings set org.gnome.desktop.interface icon-theme 'G-OS-dark'
```

## Vérification et extension

```sh
python3 scripts/generate-icons.py
python3 scripts/validate-icons.py
```

La CI valide les manifestes, les répertoires déclarés et le XML de chaque SVG. Pour ajouter une icône, utiliser le nom Freedesktop ou desktop-ID attendu et l'ajouter aux deux variantes.

## Limites

Le jeu couvre un ensemble étendu d'applications courantes, mais ne remplace pas chaque identifiant d'icône Linux. Les noms absents sont résolus par héritage Adwaita/hicolor. Les applications Libadwaita peuvent embarquer leurs propres icônes ou ignorer les thèmes GTK tiers.

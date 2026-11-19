# G-OS Theme

Thème GTK et GNOME Shell pour GNOME 51, avec une direction visuelle inspirée de macOS : surfaces claires, contrastes doux, accent bleu, coins arrondis et hiérarchie typographique nette.

## Documentation

Le manuel explique l'architecture du thème, son installation, son activation, son retour arrière et la personnalisation CSS des différents moteurs.

- [Sommaire de la documentation](docs/README.md)
- [Présentation et architecture](docs/01-architecture.md)
- [Installation, activation et retour arrière](docs/02-installation.md)
- [Comprendre et modifier les feuilles CSS](docs/03-css-et-personnalisation.md)

## Composants

- **GNOME Shell** : top bar, calendrier, quick settings, notifications, overview, dash, menus et dialogs.
- **GTK 3** : widgets classiques et applications GTK 3.
- **GTK 4 / Libadwaita** : styles compatibles avec les widgets GTK 4 et les applications Libadwaita, dans les limites de personnalisation exposées par ces bibliothèques.
- **Dark mode** : variantes claires et sombres.

## Installation

```sh
./install.sh
```

Le script installe le thème dans `~/.themes/G-OS`. Pour appliquer le thème Shell, l'extension **User Themes** doit être activée. Les thèmes GTK se sélectionnent avec GNOME Tweaks ou les paramètres de l'environnement.

Pour désinstaller :

```sh
./install.sh --uninstall
```

## Développement

Les sources sont organisées par moteur de rendu :

- `gnome-shell/` : feuille de style GNOME Shell.
- `gtk-3.0/` : styles GTK 3.
- `gtk-4.0/` : styles GTK 4 et Libadwaita.
- `assets/` : ressources locales du thème.

Aucune ressource distante n'est requise à l'exécution.

## Compatibilité

Cible initiale : GNOME Shell 51, GTK 3 et GTK 4. Les sélecteurs internes de GNOME Shell peuvent évoluer entre versions ; valider le rendu sur une session de test avant déploiement.

## Licence

GPL-3.0-or-later

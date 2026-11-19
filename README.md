# G-OS Theme

Thème GTK et GNOME Shell pour GNOME 51, avec une direction visuelle inspirée de macOS.

## Composants

- GNOME Shell, GTK 3 et GTK 4.
- Icônes SVG d'applications, dossiers et pictogrammes symboliques en variantes claires et sombres.

## Installation

```sh
./install.sh
```

Le script génère les ressources SVG et installe le thème dans `~/.themes/G-OS` ainsi que les icônes dans `~/.local/share/icons/G-OS` et `G-OS-dark`.

Sélectionner une variante :

```sh
gsettings set org.gnome.desktop.interface icon-theme 'G-OS'
# ou
gsettings set org.gnome.desktop.interface icon-theme 'G-OS-dark'
```

Désinstallation : `./install.sh --uninstall`.

## Documentation

- [Sommaire](docs/README.md)
- [Icônes et icônes symboliques](docs/10-icones-symboliques.md)

## Licence

GPL-3.0-or-later

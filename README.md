# G-OS Theme

Thème GTK et GNOME Shell pour GNOME 51, avec une direction visuelle inspirée de macOS : surfaces claires, contrastes doux, accent bleu, coins arrondis et hiérarchie typographique nette.

## Documentation

Le manuel technique couvre progressivement l'architecture, l'installation et la personnalisation détaillée des composants.

- [Sommaire complet](docs/README.md)
- [Architecture](docs/01-architecture.md)
- [Installation et activation](docs/02-installation.md)
- [CSS et personnalisation](docs/03-css-et-personnalisation.md)
- [Composants GNOME Shell](docs/04-gnome-shell-composants.md)
- [Widgets GTK 3](docs/05-gtk3-widgets.md)
- [GTK 4 et Libadwaita](docs/06-gtk4-libadwaita.md)
- [Palette et mode sombre](docs/07-palette-couleurs-mode-sombre.md)
- [Diagnostic et dépannage](docs/08-diagnostic-depannage.md)
- [Typographie et Fontconfig](docs/09-typographie-fontconfig.md)
- [Icônes et icônes symboliques](docs/10-icones-symboliques.md)
- [Curseurs et effets visuels](docs/11-curseurs-ombres-transparence.md)
- [Contrôles avancés](docs/12-controles-avances.md)
- [Échelle et accessibilité](docs/13-echelle-responsive-accessibilite.md)
- [Extensions GNOME Shell](docs/14-extensions-gnome-shell.md)
- [Inspection et débogage CSS](docs/15-inspection-debogage-css.md)
- [Maintenance et publication](docs/16-structure-maintenance-publication.md)

## Composants

- **GNOME Shell** : barre supérieure, calendrier, Quick Settings, notifications, vue d'ensemble, dash, menus et dialogues.
- **GTK 3** : widgets classiques et applications GTK 3.
- **GTK 4 / Libadwaita** : styles compatibles avec les widgets GTK 4 et les applications qui autorisent la personnalisation CSS.
- **Mode sombre** : variantes claires et sombres.

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
- `gtk-4.0/` : styles GTK 4.
- `index.theme` : métadonnées du métathème, dont les thèmes d'icônes et de curseurs déclarés.

Aucune ressource distante n'est requise à l'exécution.

## Compatibilité

Cible initiale : GNOME Shell 51, GTK 3 et GTK 4. Les sélecteurs internes de GNOME Shell peuvent évoluer entre versions ; valider le rendu sur une session de test avant déploiement. Les applications Libadwaita peuvent ignorer les thèmes GTK tiers par conception.

## Licence

GPL-3.0-or-later

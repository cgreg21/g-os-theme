# 1. Architecture du thème

## 1.1 Les couches

### GNOME Shell

Le fichier `gnome-shell/gnome-shell.css` définit l'apparence de l'interface du Shell : panneau supérieur, menus, calendrier, notifications, recherche et éléments de la vue d'ensemble.

GNOME Shell utilise St, une boîte à outils construite sur Clutter et inspirée de CSS. Ce n'est pas un navigateur web. Certaines propriétés CSS habituelles ne sont pas prises en charge et certains composants possèdent leurs propres classes.

### GTK 3

Le dossier `gtk-3.0/` contient les styles des applications GTK 3 : `gtk.css` pour la palette claire, `gtk-dark.css` pour la palette sombre et `settings.ini` pour le nom du thème à sélectionner.

### GTK 4

Le dossier `gtk-4.0/` contient les styles pour les applications GTK 4 qui acceptent la personnalisation par thème utilisateur. GTK 4 ne garantit pas que chaque application chargera un thème tiers.

### Libadwaita

Libadwaita fournit ses propres composants et conventions visuelles. Les applications Libadwaita ignorent généralement les thèmes GTK tiers. Le thème peut partager une palette et des choix esthétiques avec ces applications, mais il ne peut pas forcer uniformément leur apparence depuis un thème GTK.

## 1.2 Organisation

```text
.
├── gnome-shell/gnome-shell.css
├── gtk-3.0/
│   ├── gtk.css
│   ├── gtk-dark.css
│   └── settings.ini
├── gtk-4.0/
│   ├── gtk.css
│   └── gtk-dark.css
├── docs/
├── index.theme
└── install.sh
```

## 1.3 Pourquoi séparer les fichiers ?

Une couleur peut être identique dans toutes les couches, mais les sélecteurs et les propriétés ne le sont pas. Garder les fichiers séparés évite de copier des règles non compatibles et rend les erreurs plus faciles à isoler.

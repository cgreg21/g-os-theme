# Icônes, icônes symboliques et thèmes d'icônes

G-OS fournit deux thèmes Freedesktop : **G-OS** (clair) et **G-OS-dark** (sombre).

## Organisation

- `icons/G-OS/` : variante claire.
- `icons/G-OS-dark/` : variante sombre.
- `scalable/apps/` : icônes d'applications.
- `scalable/actions/` et `scalable/status/` : pictogrammes symboliques.
- `scalable/places/` : dossiers et emplacements.
- `scalable/mimetypes/` : icônes MIME statiques, versionnées individuellement dans Git.
- `assets/gnome-logo.svg` : ressource autonome du logo GNOME.

## Types MIME

Les icônes MIME sont de vrais fichiers SVG présents dans le dépôt. Elles ne sont pas fabriquées par `scripts/generate-icons.py`, ni par un autre générateur à l'installation.

La couverture inclut PDF, ODT, DOC, ODS, XLS, CSV, ODP, PPT, TXT, Markdown, RTF, PNG, JPEG, SVG, WebP, GIF, MP3, FLAC, WAV, MP4, MKV, WebM, ZIP, 7Z, TAR, GZIP, JSON, XML, Python, shell, C, JavaScript, HTML, CSS, exécutables, bibliothèques, polices, images ISO, paquets DEB/RPM, bases SQLite et fichiers binaires génériques.

Chaque icône utilise une feuille à coin plié, un signe central propre au format et un cartouche d'identification discret. Les familles ont des couleurs distinctes. Le rendu est flat, sans tuile carrée, sans reflet cyan et sans effets brillants. La variante sombre adapte le papier, les contours et le cartouche pour préserver le contraste.

Les SVG sont stockés directement dans `icons/G-OS/scalable/mimetypes/` et `icons/G-OS-dark/scalable/mimetypes/`. Ils sont copiés tels quels par `install.sh`. Le générateur existant reste réservé aux autres ressources qu'il gère déjà et ne crée, ne modifie ni ne remplace ces fichiers MIME.

## Installation

```sh
./install.sh
gsettings set org.gnome.desktop.interface icon-theme 'G-OS'
# ou
gsettings set org.gnome.desktop.interface icon-theme 'G-OS-dark'
```

## Vérification

```sh
python3 scripts/generate-icons.py
python3 scripts/validate-icons.py
```

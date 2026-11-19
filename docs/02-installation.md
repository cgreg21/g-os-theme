# 2. Installation, activation et retour arrière

## 2.1 Prérequis

- Une session GNOME 51 pour tester le style GNOME Shell.
- GTK 3 et/ou GTK 4 selon les applications à personnaliser.
- L'extension GNOME Shell **User Themes** pour charger un thème Shell depuis le répertoire utilisateur.
- GNOME Tweaks peut être utilisé pour sélectionner le thème GTK lorsque cette option est disponible.

## 2.2 Installer

Depuis la racine du dépôt :

```sh
chmod +x install.sh
./install.sh
```

Le script copie les dossiers de thème vers `~/.themes/G-OS`. Il ne modifie pas les fichiers système et n'installe aucune extension.

## 2.3 Activer le thème Shell

1. Installe et active l'extension User Themes.
2. Ouvre GNOME Tweaks.
3. Dans la section Apparence, sélectionne G-OS comme thème Shell.
4. Déconnecte-toi puis reconnecte-toi si le changement ne s'applique pas immédiatement.

## 2.4 Activer GTK 3

Dans GNOME Tweaks, sélectionne G-OS dans le choix du thème des applications. Le fichier `gtk-3.0/settings.ini` définit également le nom GTK attendu par les applications GTK 3 qui lisent ce réglage.

## 2.5 GTK 4 et Libadwaita

Les fichiers `gtk-4.0/` ne peuvent agir que sur les applications GTK 4 qui autorisent le chargement d'un CSS utilisateur ou d'un thème externe. Les applications Libadwaita ignorent généralement les thèmes GTK tiers. Ce comportement est une décision de conception de Libadwaita, pas une erreur d'installation.

## 2.6 Désinstaller

```sh
./install.sh --uninstall
```

Cette commande supprime uniquement `~/.themes/G-OS`. Elle ne désactive pas User Themes et ne modifie pas les autres thèmes installés.

## 2.7 Vérifier le résultat

- Vérifie que `~/.themes/G-OS/gnome-shell/gnome-shell.css` existe.
- Vérifie que les fichiers GTK 3 et GTK 4 ont été copiés.
- Vérifie séparément le thème Shell et le thème des applications.
- Si un élément reste inchangé, vérifie d'abord que l'application utilise bien le moteur ciblé.

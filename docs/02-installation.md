# Installation, activation et retour arrière

## 1. Préparer le système

G-OS Theme vise GNOME Shell 51, GTK 3 et GTK 4. Vérifiez votre session et votre version avant de commencer :

```bash
gnome-shell --version
```

Le résultat doit correspondre à la version ciblée par le dépôt. Une distribution peut appliquer des correctifs ou conserver des composants de versions différentes ; testez toujours sur la session réellement utilisée.

## 2. Récupérer le dépôt

```bash
git clone https://github.com/cgreg21/g-os-theme.git
cd g-os-theme
```

Pour mettre à jour une copie existante :

```bash
git pull --ff-only
```

L'option `--ff-only` évite de créer silencieusement un commit de fusion local. Si la commande refuse la mise à jour, examinez vos changements avant toute autre opération.

## 3. Installer pour le compte courant

Le dépôt fournit un script d'installation :

```bash
./install.sh
```

Le thème est installé dans `~/.themes/G-OS`. Cette installation utilisateur ne nécessite pas de remplacer les fichiers système de GNOME.

Avant l'exécution, vous pouvez lire le script :

```bash
less install.sh
```

Ne lancez pas un script d'installation avec des privilèges administrateur sans raison : l'installation utilisateur est le chemin prévu.

## 4. Activer le thème GNOME Shell

La feuille de style GNOME Shell est sélectionnée par l'extension User Themes. Vérifiez que cette extension est disponible et activée dans votre environnement GNOME.

Après activation, sélectionnez le thème Shell nommé G-OS dans l'outil de gestion des extensions ou dans l'outil de personnalisation utilisé par votre distribution.

Le thème GTK et le thème Shell sont deux réglages distincts. Activer l'un ne garantit pas l'activation de l'autre.

## 5. Activer les thèmes GTK

Les thèmes GTK 3 et GTK 4 sont installés dans le même dossier de thème. Sélectionnez G-OS avec GNOME Tweaks ou l'outil de personnalisation disponible sur votre distribution.

Les applications Libadwaita récentes peuvent limiter ou ignorer certaines personnalisations GTK traditionnelles. Ce comportement est une limite de la plateforme, pas nécessairement une erreur d'installation.

## 6. Vérifier l'installation

```bash
test -d "$HOME/.themes/G-OS" && echo "Thème installé"
find "$HOME/.themes/G-OS" -maxdepth 2 -type f -print
```

Vérifiez séparément le rendu du Shell, d'une application GTK 3 et d'une application GTK 4. Fermez puis relancez les applications après un changement de thème si leur apparence ne se met pas à jour immédiatement.

## 7. Désinstaller

Pour retirer la copie installée :

```bash
./install.sh --uninstall
```

Cette opération retire le thème G-OS installé par le script. Elle ne doit pas supprimer vos autres thèmes ni vos préférences personnelles.

Après désinstallation, sélectionnez un thème encore installé pour le Shell et les applications.

## 8. Retour arrière manuel

Si l'installation ou l'activation produit un affichage inutilisable, ouvrez les paramètres de personnalisation et sélectionnez un thème connu comme fonctionnel. Si l'interface Shell ne répond plus, utilisez une session de terminal accessible pour désactiver User Themes ou retirer le dossier G-OS de `~/.themes`.

Ne supprimez pas les thèmes fournis par la distribution. Le retour arrière doit porter uniquement sur les fichiers installés par G-OS.

## 9. Problèmes fréquents

**Le thème n'apparaît pas dans la liste.** Vérifiez le nom et l'emplacement du dossier, puis redémarrez l'outil de personnalisation.

**Le Shell reste inchangé.** Vérifiez que User Themes est activée et que G-OS est sélectionné pour GNOME Shell, pas uniquement pour GTK.

**Certaines applications ne changent pas.** Identifiez leur toolkit et leurs éventuelles règles de style internes. Les applications Libadwaita ne permettent pas toutes les personnalisations historiques.

**Le rendu est incohérent après une mise à jour GNOME.** Vérifiez la version de GNOME Shell, puis testez les sélecteurs de la feuille Shell. Ne supposez pas que les classes internes restent identiques entre versions.

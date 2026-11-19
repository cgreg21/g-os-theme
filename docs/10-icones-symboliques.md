# Icônes, icônes symboliques et thèmes d'icônes

Les icônes constituent une ressource graphique distincte des feuilles CSS. Ce chapitre explique les différents systèmes d'icônes utilisés sur un bureau GNOME et les limites de personnalisation du dépôt G-OS actuel.

## 1. Identifier le type d'icône

GNOME utilise plusieurs catégories :

- **Icônes d'applications** : identifient une application dans le dock, la vue d'ensemble et les lanceurs.
- **Icônes symboliques** : pictogrammes monochromes utilisés dans les barres d'outils, menus et contrôles.
- **Icônes de fichiers et dossiers** : représentent les types MIME, répertoires et volumes.
- **Icônes propres à GNOME Shell** : ressources employées par le Shell et ses composants.
- **Icônes fournies par une application ou une extension** : elles peuvent être embarquées ou installées séparément.

Ces ressources ne sont pas toutes contrôlées par le même mécanisme. Une règle CSS peut modifier certaines dimensions ou couleurs d'une icône déjà affichée, mais elle ne remplace pas automatiquement le fichier image utilisé.

## 2. Le thème d'icônes déclaré par G-OS

Le fichier racine `index.theme` déclare actuellement :

```ini
[X-GNOME-Metatheme]
GtkTheme=G-OS
MetacityTheme=Adwaita
IconTheme=Adwaita
CursorTheme=Adwaita
```

G-OS utilise donc le thème d'icônes Adwaita. Le dépôt ne contient pas actuellement de répertoire `icons/` ni de jeu d'icônes personnalisé. Il ne faut donc pas présenter G-OS comme fournissant ses propres icônes d'applications.

## 3. Comprendre la structure d'un thème d'icônes

Un thème d'icônes freedesktop comporte généralement un fichier `index.theme` et des répertoires organisés par tailles ou catégories. Les fichiers peuvent être des PNG, SVG ou autres formats pris en charge par l'environnement.

Un thème complet doit déclarer ses répertoires, ses tailles et ses éventuelles relations d'héritage. Il doit aussi couvrir un ensemble suffisamment large de noms d'icônes utilisés par les applications. Créer uniquement quelques images isolées ne constitue pas un thème cohérent.

Avant d'ajouter un jeu d'icônes à G-OS, étudiez la spécification du thème d'icônes freedesktop et vérifiez les noms effectivement demandés par les applications ciblées.

## 4. Icônes symboliques et couleur CSS

Les icônes symboliques sont généralement conçues pour recevoir une couleur depuis le contexte graphique. Selon le widget et le moteur, la couleur peut être héritée du texte ou appliquée par une propriété dédiée.

Exemple GTK générique :

```css
button image {
  color: #20242c;
}
```

Cet exemple ne garantit pas que toutes les images deviendront monochromes. Une image PNG multicolore ne se transforme pas en icône symbolique parce que sa propriété `color` change. Il faut que le composant et le format de l'icône prennent en charge cette coloration.

Dans GNOME Shell, vérifiez la classe réelle de l'icône avant d'écrire un sélecteur. Ne supposez pas qu'un sélecteur GTK s'applique à Shell.

## 5. Tailles et alignement

Les dimensions d'une icône dépendent du widget qui la contient, de la taille demandée par l'application et parfois du nom symbolique utilisé. Une surcharge CSS générique peut provoquer des décalages ou des icônes floues.

Exemple de règle de principe pour un widget GTK :

```css
button image {
  -gtk-icon-size: 16px;
}
```

Cette propriété est spécifique à GTK et ne doit pas être copiée dans une feuille GNOME Shell ou GTK 4 sans vérification. Elle ne s'applique pas nécessairement à toutes les images et toutes les versions.

Préférez laisser l'application demander la taille appropriée. Ne forcez une dimension que pour corriger un défaut observé et reproductible.

## 6. Inspecter les icônes disponibles

Quelques commandes utiles :

```bash
gsettings get org.gnome.desktop.interface icon-theme
find /usr/share/icons -maxdepth 2 -name index.theme -print
find ~/.local/share/icons -maxdepth 2 -name index.theme -print
```

Pour connaître les fichiers installés dans un thème précis :

```bash
find /usr/share/icons/Adwaita -type f | head -n 40
```

Les chemins exacts dépendent de la distribution. Certaines icônes peuvent également provenir de `/usr/local/share/icons` ou du dossier personnel.

## 7. Changer de thème d'icônes pour tester

Le réglage GNOME peut être consulté et modifié avec :

```bash
gsettings get org.gnome.desktop.interface icon-theme
gsettings set org.gnome.desktop.interface icon-theme 'Adwaita'
```

La commande d'écriture modifie le réglage de la session utilisateur. Notez la valeur précédente avant de faire un essai afin de pouvoir la restaurer. Le choix déclaré dans `index.theme` décrit le métathème ; il ne remplace pas nécessairement tous les réglages de la session.

## 8. Créer un jeu d'icônes cohérent

Pour concevoir un jeu personnalisé :

1. Définissez un langage visuel commun : épaisseur de trait, angles, perspective et niveau de détail.
2. Déterminez les catégories et tailles nécessaires.
3. Choisissez des noms de fichiers compatibles avec les noms d'icônes attendus.
4. Préparez les variantes symboliques et les icônes d'applications séparément.
5. Déclarez les répertoires et héritages dans `index.theme`.
6. Testez avec plusieurs applications et plusieurs tailles.
7. Vérifiez les licences des ressources utilisées.

Les icônes symboliques doivent rester lisibles à petite taille et avec un contraste suffisant. Les icônes d'applications peuvent être plus détaillées, mais doivent conserver une silhouette reconnaissable.

## 9. Limites du dépôt actuel

À ce stade, G-OS déclare Adwaita comme thème d'icônes et n'embarque pas de ressources d'icônes. La personnalisation des icônes n'est donc pas une fonction fournie par les fichiers actuels du dépôt. Une évolution future devra ajouter un véritable thème d'icônes structuré, plutôt que des images sans manifeste ni convention de nommage.

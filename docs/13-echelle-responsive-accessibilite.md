# Échelle d'interface, adaptation et accessibilité

Un thème doit rester utilisable avec différentes tailles d'écran, différents facteurs d'échelle, des textes longs et des besoins d'accessibilité variés. Le CSS du thème ne remplace pas les réglages d'affichage de GNOME.

## 1. Distinguer taille CSS et échelle de l'écran

Les dimensions déclarées dans une feuille CSS décrivent les dimensions des éléments dans le moteur concerné. Le facteur d'échelle de l'affichage est géré par GNOME, le serveur graphique et le matériel.

Ne tentez pas de simuler le réglage d'échelle de l'écran en agrandissant tous les éléments avec `transform: scale(...)`. Cette approche peut déplacer les zones de clic, provoquer des chevauchements et dégrader le rendu.

## 2. Consulter les réglages GNOME

Les paramètres d'affichage et d'accessibilité sont configurés par GNOME. Pour consulter les réglages d'interface courants :

```bash
gsettings get org.gnome.desktop.interface text-scaling-factor
gsettings get org.gnome.desktop.interface cursor-size
gsettings get org.gnome.desktop.interface enable-animations
```

Le facteur de taille du texte n'est pas le facteur d'échelle global de l'écran. Le réglage des animations est indépendant des règles CSS de couleurs et de dimensions.

Les options disponibles et leur comportement dépendent de la version de GNOME et de la distribution.

## 3. Dimensions robustes

Évitez de fixer des hauteurs qui supposent une seule police ou une seule langue. Préférez des espacements raisonnables et des dimensions minimales lorsque le moteur les prend en charge.

Exemple CSS générique :

```css
.exemple {
  min-height: 2.5em;
  padding: 0.45em 0.8em;
}
```

La classe `.exemple` est illustrative et n'existe pas dans les feuilles G-OS. Vérifiez la prise en charge des unités et propriétés dans le moteur ciblé.

## 4. Tester les tailles de texte

Augmentez le facteur de taille du texte dans les paramètres d'accessibilité ou avec l'outil de configuration adapté à votre environnement. Vérifiez ensuite :

- les menus GNOME Shell ;
- les Quick Settings ;
- les notifications ;
- les boutons et champs GTK ;
- les listes et barres latérales ;
- les titres de fenêtres ;
- les textes longs et traduits.

Un thème qui ne fonctionne qu'avec la taille de texte par défaut est fragile.

## 5. Contraste des couleurs

La couleur du texte doit rester suffisamment distincte de son arrière-plan. Vérifiez les contrastes pour les états normaux, survolés, sélectionnés et désactivés.

Les couleurs de G-OS sont déclarées dans ses feuilles : bleu d'accent, surfaces claires ou sombres, texte principal, texte secondaire et bordures. Lorsqu'une couleur de fond change, contrôlez toutes les couleurs de texte et d'icônes associées.

Ne transmettez pas une information uniquement par la couleur. Un état sélectionné doit également rester identifiable par sa forme, sa position ou un autre indicateur visuel lorsque cela est pertinent.

## 6. Focus clavier

Le focus doit être visible sans souris. G-OS définit des règles de focus pour les boutons GTK 3 et pour les boutons de la barre supérieure GNOME Shell.

Ne supprimez pas les contours de focus pour uniformiser les contrôles. Testez la navigation avec Tab, Maj+Tab, les flèches, Entrée et Espace selon le composant.

## 7. Mouvement et animations

Les transitions décoratives doivent rester courtes et ne pas gêner la compréhension. Le réglage GNOME `enable-animations` peut être consulté avec :

```bash
gsettings get org.gnome.desktop.interface enable-animations
```

Une règle CSS de thème ne garantit pas à elle seule le respect de toutes les préférences de réduction des animations. Évitez les animations indispensables à la compréhension et vérifiez le comportement dans la session réelle.

## 8. Curseur et interaction

La taille du pointeur peut être réglée dans GNOME indépendamment du thème CSS. Testez le thème avec plusieurs tailles de curseur, notamment sur les zones cliquables de petite dimension.

Assurez-vous que les états hover et focus ne sont pas les seuls moyens d'indiquer une action : les utilisateurs au clavier ne disposent pas du survol de souris.

## 9. Vérifier le mode sombre

Le mode sombre doit conserver :

- du texte lisible sur les surfaces ;
- une distinction claire entre surface principale et surface secondaire ;
- des bordures visibles sans être agressives ;
- un accent suffisamment contrasté ;
- des états focus et sélection identifiables.

Ne faites pas simplement une inversion mathématique des couleurs. Les couleurs de texte, les surfaces et les accents doivent être définis par rôle.

## 10. Procédure de validation

Avant de publier une évolution visuelle :

1. Testez en mode clair et sombre.
2. Augmentez la taille du texte.
3. Naviguez uniquement au clavier.
4. Vérifiez les états hover, focus, active et disabled.
5. Contrôlez les contrastes des textes et icônes.
6. Testez une fenêtre étroite et une fenêtre large.
7. Vérifiez les chaînes longues et les caractères accentués.
8. Confirmez que les contrôles restent cliquables et ne se chevauchent pas.

## 11. Limites du thème

G-OS peut améliorer les couleurs, les contours et les dimensions des widgets qui acceptent ses feuilles. Il ne peut pas corriger seul les défauts d'accessibilité d'une application, modifier la mise à l'échelle du compositeur ou garantir le comportement de toutes les extensions.

Les réglages GNOME, les applications et le thème doivent être testés ensemble.

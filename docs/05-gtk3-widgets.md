# GTK 3 : widgets, états et personnalisation

Ce chapitre suit les règles présentes dans `gtk-3.0/gtk.css` et `gtk-3.0/gtk-dark.css`. Il décrit les sélecteurs du thème G-OS et les principaux concepts nécessaires pour les modifier.

## 1. Fichiers et chargement

Le thème GTK 3 possède deux feuilles principales :

- `gtk-3.0/gtk.css` pour l'apparence claire ;
- `gtk-3.0/gtk-dark.css` pour l'apparence sombre.

Le fichier `settings.ini` accompagne cette configuration. Les applications GTK 3 peuvent cependant charger leurs propres feuilles de style et widgets spécifiques. Le résultat dépend donc aussi de l'application.

## 2. Couleurs nommées

GTK 3 permet de déclarer des couleurs avec `@define-color`, puis de les réutiliser avec la syntaxe `@nom`.

```css
@define-color theme_bg_color #f5f6f8;
@define-color theme_fg_color #20242c;
@define-color theme_base_color #ffffff;
@define-color theme_text_color #20242c;
@define-color theme_selected_bg_color #0878e8;
@define-color theme_selected_fg_color #ffffff;
```

Cette méthode évite de répéter une même valeur dans toutes les règles. Si la couleur de fond principale change, les règles qui utilisent `@theme_bg_color` suivent automatiquement cette modification.

Les noms historiques comme `theme_bg_color` et `theme_base_color` sont utilisés par de nombreux thèmes GTK 3. Ils ne remplacent pas les couleurs propres à chaque application.

## 3. Fond de fenêtre et surfaces de contenu

La feuille cible `window` et `.background` pour la surface générale. Les vues de contenu sont ciblées par `.view`, `textview`, `treeview` et `iconview`.

```css
window, .background {
  background-color: @theme_bg_color;
  color: @theme_fg_color;
}

.view, textview, treeview, iconview {
  background-color: @theme_base_color;
  color: @theme_text_color;
}
```

La fenêtre et la zone de contenu n'ont pas nécessairement la même couleur. Cette séparation donne une hiérarchie visuelle entre le cadre de l'application et sa surface de travail.

Vérifiez les vues contenant du texte, des listes, des fichiers et des icônes. Une règle générale peut toucher des éléments qui ne ressemblent pas à une simple zone blanche.

## 4. Boutons

Les sélecteurs `button` et `.button` définissent la surface, la bordure, le rayon et les espacements des boutons.

```css
button, .button {
  color: @theme_fg_color;
  background-image: none;
  background-color: #ffffff;
  border: 1px solid @borders;
  border-radius: 9px;
  box-shadow: none;
  padding: 6px 12px;
  text-shadow: none;
}
```

La suppression de `background-image` permet d'éviter qu'un dégradé ou une image de thème GTK ne concurrence la couleur de fond choisie.

Les états définis dans G-OS sont :

- `:hover` : pointeur au-dessus du bouton ;
- `:active` : bouton en cours d'activation ;
- `:checked` : bouton bascule sélectionné ;
- `:disabled` : contrôle désactivé ;
- `:focus` : contrôle qui reçoit le focus.

Ne confondez pas `:active` et `:checked`. Le premier décrit une interaction en cours ; le second décrit un état sélectionné persistant pour les contrôles qui le prennent en charge.

## 5. Champs de saisie

La feuille applique des règles communes à `entry`, `spinbutton` et `combobox`. Elle cible également les boutons d'un groupe lié avec `.linked > button`.

```css
entry, spinbutton, combobox {
  background-color: #ffffff;
  color: @theme_text_color;
  border: 1px solid @borders;
  border-radius: 8px;
  min-height: 28px;
  padding: 4px 8px;
  box-shadow: none;
}
```

Les champs doivent rester distincts des surfaces ordinaires. Vérifiez le texte saisi, le texte sélectionné, le curseur, le placeholder, le focus et l'état désactivé.

La hauteur minimale n'est pas une hauteur fixe. Le texte, la police et les marges internes peuvent augmenter la taille finale du widget.

## 6. Barre d'en-tête

Le sélecteur `headerbar` règle la barre d'en-tête des applications GTK 3 qui l'utilisent.

```css
headerbar {
  background-color: #f8f9fb;
  color: @theme_fg_color;
  border-bottom: 1px solid @borders;
  box-shadow: none;
  min-height: 42px;
}
```

Les boutons de la barre sont volontairement transparents dans G-OS afin de conserver une surface unifiée. Vérifiez les boutons de fenêtre, les menus et les contrôles ajoutés par les applications.

Toutes les applications GTK 3 n'utilisent pas une `headerbar`. Ne déduisez pas qu'une règle non visible est invalide avant d'avoir vérifié le type de fenêtre.

## 7. Barre latérale

La classe `.sidebar` définit le fond et la séparation de la barre latérale. Les lignes sont ciblées par `.sidebar row`, et la ligne sélectionnée par `.sidebar row:selected`.

```css
.sidebar row:selected {
  background-color: #dcecff;
  color: #075eb5;
}
```

Testez une liste vide, une longue liste, le défilement, le survol et la sélection. Une sélection doit rester visible lorsque la fenêtre perd le focus.

## 8. Sélection de texte

Le sélecteur `selection` définit les couleurs de sélection :

```css
selection {
  background-color: @theme_selected_bg_color;
  color: @theme_selected_fg_color;
}
```

Vérifiez la sélection dans un champ de saisie, un éditeur de texte et une vue de contenu. Les applications peuvent appliquer des styles spécifiques qui modifient le résultat.

## 9. Barres de progression et curseurs

La feuille cible les pistes avec `progressbar trough` et `scale trough`. La partie remplie utilise `progressbar progress` et `scale highlight`.

```css
progressbar trough, scale trough {
  background-color: #e4e8ee;
  border-radius: 99px;
}

progressbar progress, scale highlight {
  background-color: @accent_color;
  border-radius: 99px;
}
```

La piste et la valeur doivent être facilement distinguables. Testez les valeurs minimale, intermédiaire et maximale, ainsi que les contrôles désactivés.

## 10. Particularités du CSS GTK 3

GTK 3 prend en charge une syntaxe CSS propre à son moteur. Les couleurs nommées, les états des widgets et certains sélecteurs diffèrent des navigateurs web. Ne copiez pas aveuglément une règle CSS web.

Les propriétés GTK historiques préfixées par `-GtkWidget-` ne sont pas des propriétés CSS standard. Elles servent ici à définir les métriques du focus pour les widgets GTK 3. Vérifiez les avertissements émis par GTK lors du chargement de la feuille.

## 11. Tester les changements

Fermez et relancez l'application GTK 3 ciblée. Vérifiez au moins une application avec des boutons, champs de saisie, listes, barres latérales et contrôles de progression.

Pour repérer les règles existantes :

```bash
grep -nE 'button|entry|headerbar|sidebar|selection|progressbar|scale' gtk-3.0/gtk.css
```

Comparez la feuille claire et la feuille sombre. Une modification du fichier clair ne met pas automatiquement à jour la variante sombre.

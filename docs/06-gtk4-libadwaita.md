# GTK 4 et Libadwaita : palettes et limites

Ce chapitre décrit les feuilles `gtk-4.0/gtk.css` et `gtk-4.0/gtk-dark.css`. Il faut distinguer GTK 4, qui fournit le toolkit et son moteur CSS, de Libadwaita, qui fournit des composants et conventions visuelles pour les applications GNOME.

## 1. Comprendre la différence

GTK 4 possède son propre ensemble de widgets et son propre moteur de style. Une règle GTK 3 n'est pas automatiquement compatible avec GTK 4.

Libadwaita s'appuie sur GTK 4 et définit une identité visuelle cohérente pour les applications GNOME modernes. Ces applications peuvent volontairement limiter la personnalisation par les thèmes GTK globaux. Une feuille CSS présente dans le dossier `gtk-4.0` ne garantit donc pas qu'une application Libadwaita l'utilise.

Le but de G-OS est de fournir une palette cohérente aux applications qui autorisent ces personnalisations, sans prétendre contourner les choix de conception de Libadwaita.

## 2. Couleurs sémantiques

La feuille claire déclare notamment :

```css
@define-color window_bg_color #f5f6f8;
@define-color window_fg_color #20242c;
@define-color view_bg_color #ffffff;
@define-color view_fg_color #20242c;
@define-color headerbar_bg_color #f8f9fb;
@define-color headerbar_fg_color #20242c;
@define-color card_bg_color #ffffff;
@define-color card_fg_color #20242c;
@define-color popover_bg_color #ffffff;
@define-color popover_fg_color #20242c;
```

Ces noms expriment le rôle de la couleur plutôt que son apparence. `window_bg_color` correspond à la surface de fenêtre ; `view_bg_color` à la surface de contenu ; `card_bg_color` à une carte ; `popover_bg_color` à un panneau contextuel.

Cette sémantique facilite la cohérence : deux composants différents peuvent partager la même couleur parce qu'ils représentent le même type de surface.

## 3. Couleurs d'accent

Les couleurs d'accent déclarées par G-OS sont :

```css
@define-color accent_bg_color #0878e8;
@define-color accent_fg_color #ffffff;
@define-color accent_color #0878e8;
```

La couleur d'accent sert à distinguer les actions principales, les éléments sélectionnés et les contrôles actifs. Elle ne doit pas être utilisée pour tous les éléments décoratifs.

Lorsque vous modifiez l'accent, vérifiez le contraste entre le texte et le fond, les états survolés, les éléments désactivés et les contrôles sélectionnés.

## 4. Fenêtres et barres d'en-tête

Les sélecteurs `window` et `.background` définissent la surface générale. Le sélecteur `headerbar` règle la surface et la bordure de la barre d'en-tête.

```css
window, .background {
  background: @window_bg_color;
  color: @window_fg_color;
}

headerbar {
  background: @headerbar_bg_color;
  color: @headerbar_fg_color;
  box-shadow: none;
  border-bottom: 1px solid @borders;
}
```

Une application peut construire sa barre d'en-tête avec des widgets supplémentaires ou des styles propres. Inspectez son arbre de widgets avant d'ajouter une règle ciblée.

## 5. Boutons et champs

Le thème applique des rayons aux boutons et aux champs de saisie :

```css
button, .button {
  border-radius: 9px;
}

entry, textview, spinbutton {
  border-radius: 8px;
}
```

Ces règles sont volontairement simples. Les applications Libadwaita peuvent appliquer leurs propres classes et styles. Si un contrôle ne change pas, ne multipliez pas les sélecteurs au hasard : vérifiez d'abord si la personnalisation est permise.

## 6. Cartes et listes encadrées

G-OS cible `.card` et `.boxed-list` :

```css
.card, .boxed-list {
  background: @card_bg_color;
  color: @card_fg_color;
  border: 1px solid @borders;
  border-radius: 12px;
}
```

Une carte doit se distinguer du fond sans créer une bordure trop forte. Vérifiez les cartes imbriquées, les listes longues et les panneaux qui contiennent des contrôles interactifs.

## 7. Popovers

Les règles `popover > contents` et `popover contents` ciblent le contenu des popovers.

```css
popover > contents, popover contents {
  background: @popover_bg_color;
  color: @popover_fg_color;
  border: 1px solid @borders;
  border-radius: 12px;
}
```

La structure interne du widget peut évoluer. Une règle de sélecteur descendant trop large peut affecter des éléments inattendus. Préférez le sélecteur le plus précis qui fonctionne dans l'application cible.

## 8. Variante sombre

La feuille sombre redéfinit les mêmes rôles avec des surfaces foncées :

```css
@define-color window_bg_color #20242c;
@define-color window_fg_color #edf0f5;
@define-color view_bg_color #292e38;
@define-color view_fg_color #edf0f5;
@define-color accent_bg_color #2589ed;
@define-color accent_fg_color #ffffff;
@define-color accent_color #4da3ff;
```

Ne faites pas simplement une inversion mathématique des couleurs. Une palette sombre doit préserver la hiérarchie des surfaces, la lisibilité des textes secondaires et la distinction entre les états.

## 9. Vérifier la prise en charge

Pour vérifier le comportement :

1. Choisissez une application GTK 4 qui permet réellement le CSS utilisateur.
2. Appliquez le thème.
3. Vérifiez la fenêtre, la barre d'en-tête, les boutons, les champs et les cartes.
4. Répétez en mode sombre.
5. Comparez avec une application Libadwaita récente.
6. Notez explicitement les composants qui ignorent le thème.

Une application qui ignore le thème ne prouve pas que la feuille est mal écrite. Elle peut utiliser des styles internes ou respecter les restrictions de personnalisation de Libadwaita.

## 10. Ne pas détourner les mécanismes de style

Évitez de modifier les fichiers installés dans les répertoires système, de remplacer les ressources internes de Libadwaita ou d'injecter des styles non documentés pour forcer une apparence. Ces méthodes sont fragiles et peuvent casser lors d'une mise à jour.

La documentation de G-OS doit annoncer clairement les limites au lieu de promettre une compatibilité totale qui n'existe pas.

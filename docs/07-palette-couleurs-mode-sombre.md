# Palette, couleurs et mode sombre

Ce chapitre explique comment faire évoluer l'identité colorimétrique de G-OS sans perdre la cohérence entre GNOME Shell, GTK 3 et GTK 4.

## 1. Palette actuelle

La direction visuelle de G-OS repose sur quelques rôles récurrents :

- Fond général clair : gris très pâle.
- Surface principale : blanc.
- Surface secondaire : gris bleuté léger.
- Texte principal : gris presque noir.
- Texte secondaire : gris moyen.
- Accent : bleu.
- Bordures : bleu-gris très transparent.

Dans les feuilles GTK, ces rôles sont en partie déclarés avec `@define-color`. Dans GNOME Shell, des couleurs `g_os_*` sont déclarées au début du fichier, tandis que plusieurs règles utilisent encore des valeurs littérales. Cette différence doit être prise en compte lors d'une refonte de palette.

## 2. Couleurs nommées dans GTK

Une couleur nommée s'écrit avec `@define-color` :

```css
@define-color accent_color #0878e8;
```

Elle est ensuite référencée ainsi :

```css
button:focus {
  outline: 2px solid alpha(@accent_color, .45);
}
```

La fonction `alpha()` est une fonction de couleur GTK. Elle permet de réutiliser une couleur en lui donnant une transparence. Elle ne doit pas être supposée disponible dans toutes les syntaxes CSS.

Déclarez les rôles de couleur au même endroit, en tête de feuille. Évitez de définir plusieurs fois le même rôle avec des valeurs différentes dans des blocs éloignés.

## 3. Couleurs nommées dans GNOME Shell

La feuille Shell déclare des noms avec `@define-color` :

```css
@define-color g_os_bg #f5f6f8;
@define-color g_os_surface #ffffff;
@define-color g_os_surface_alt #eef1f5;
@define-color g_os_text #20242c;
@define-color g_os_muted #747d8b;
@define-color g_os_accent #0878e8;
@define-color g_os_border rgba(30, 42, 58, 0.12);
```

Dans l'état actuel du dépôt, certaines règles Shell utilisent néanmoins des couleurs écrites directement. Lors d'une évolution, remplacez progressivement les valeurs répétées par les noms de palette lorsque la syntaxe et le moteur le permettent. Cela rendra les futures variantes plus simples à maintenir.

Ne remplacez pas toutes les couleurs littérales sans vérifier les propriétés spécifiques à St, notamment les propriétés de flèche des menus.

## 4. Construire une palette claire cohérente

Une palette ne se limite pas à choisir une couleur de fond et une couleur de texte. Il faut définir des rôles :

- Fond de fenêtre.
- Surface de contenu.
- Surface élevée ou flottante.
- Bordure discrète.
- Texte principal.
- Texte secondaire.
- Texte désactivé.
- Accent et texte sur accent.
- États survolé, actif et sélectionné.
- Indicateur de focus.

Les rôles peuvent partager une valeur, mais ils doivent rester conceptuellement distincts. Cela évite de rendre tous les éléments identiques lorsqu'une seule couleur change.

## 5. Construire une palette sombre

Une palette sombre conserve les mêmes rôles avec des valeurs adaptées. Les surfaces ne doivent pas toutes être noires : plusieurs niveaux de gris bleuté permettent de distinguer la fenêtre, le contenu et les panneaux flottants.

Le texte principal doit être clair sans être nécessairement blanc pur. Les textes secondaires doivent rester lisibles. L'accent doit être suffisamment lumineux pour être identifiable, sans provoquer un contraste agressif sur tous les composants.

Testez les bordures : une bordure trop claire crée un quadrillage visuel, tandis qu'une bordure trop sombre peut rendre les panneaux difficiles à distinguer.

## 6. Ne pas confondre thème sombre et préférence système

La présence de `gtk-dark.css` ne signifie pas que toutes les applications basculent automatiquement vers ce fichier dans tous les contextes. Le choix dépend du toolkit, des paramètres du thème et des préférences de couleur de l'application.

GNOME Shell possède également son propre mécanisme de style. Il faut donc vérifier séparément le mode sombre du Shell, celui de GTK 3 et celui de GTK 4.

## 7. Contraste et lisibilité

Contrôlez au minimum :

- Texte principal sur fond principal.
- Texte secondaire sur surface secondaire.
- Texte blanc sur accent bleu.
- Texte sélectionné sur fond de sélection.
- Icônes sur les boutons actifs et inactifs.
- Focus clavier sur les différentes surfaces.

Ne vous fiez pas uniquement à une capture réduite. Vérifiez les composants à leur taille réelle et avec les polices réellement disponibles.

## 8. Modifier la palette sans incohérence

Pour changer l'accent G-OS :

1. Modifiez la couleur d'accent GTK 3 dans les deux variantes.
2. Modifiez les rôles d'accent GTK 4 dans les deux variantes.
3. Modifiez la couleur d'accent GNOME Shell.
4. Recherchez les anciennes valeurs littérales qui restent dans les règles.
5. Vérifiez les états actifs, sélectionnés et focus.
6. Testez les deux modes.

Recherche utile :

```bash
grep -RInE '#0878e8|#2589ed|#4da3ff|#075eb5' gnome-shell gtk-3.0 gtk-4.0
```

Cette recherche aide à repérer les valeurs répétées. Elle ne doit pas conduire à remplacer mécaniquement toutes les occurrences : certaines couleurs représentent des états différents.

## 9. Contrôle avant validation

Avant de considérer une palette terminée, examinez la barre supérieure, les menus, les Quick Settings, les notifications, les dialogues, les boutons, les champs, les listes, les cartes et les popovers.

Une palette est cohérente lorsque la hiérarchie reste compréhensible dans tous ces composants, pas seulement sur une fenêtre vide.

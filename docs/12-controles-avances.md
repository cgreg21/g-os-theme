# Contrôles avancés : boutons, champs, listes et indicateurs

Ce chapitre approfondit la personnalisation des contrôles GTK 3 et GTK 4. Les exemples sont explicitement distingués des sélecteurs réellement présents dans G-OS.

## 1. Les états d'un contrôle

Un widget peut changer d'apparence selon son état :

- normal : état au repos ;
- hover : pointeur au-dessus ;
- active : activation ou pression ;
- checked : option activée ;
- disabled : contrôle indisponible ;
- focus : contrôle ciblé au clavier ;
- selected : élément sélectionné dans une liste ou une vue.

Une règle correcte doit prendre en compte les états utiles. Un bouton désactivé ne doit pas ressembler à un bouton actif, et le focus clavier doit rester visible.

## 2. Boutons GTK 3 dans G-OS

Les feuilles `gtk-3.0/gtk.css` et `gtk-3.0/gtk-dark.css` définissent déjà les règles de base :

```css
button, .button {
  border-radius: 9px;
  padding: 6px 12px;
  box-shadow: none;
}
button:hover { /* état survolé */ }
button:active, button:checked { /* état activé */ }
button:disabled { /* état indisponible */ }
button:focus { /* focus clavier */ }
```

Le fichier clair et le fichier sombre possèdent des couleurs adaptées à leur palette. Conservez cette séparation lorsque vous modifiez les états.

## 3. Champs de saisie

G-OS cible les champs GTK 3 avec `entry`, `spinbutton` et `combobox`. Les règles actuelles contrôlent notamment le fond, le texte, la bordure, le rayon et la hauteur minimale.

Exemple générique pour un champ :

```css
entry {
  min-height: 28px;
  padding: 4px 8px;
  border-radius: 8px;
}
entry:focus {
  border-color: @accent_color;
}
```

N'appliquez pas une bordure de focus uniquement par changement de couleur si elle devient invisible sur certains fonds. Un contour ou un indicateur complémentaire peut être nécessaire.

## 4. Cases à cocher et boutons radio

GTK possède des widgets dédiés aux cases à cocher et boutons radio. Leur rendu peut utiliser des éléments internes, des icônes ou des nœuds spécifiques au moteur. Une règle générique `checkbutton` ne garantit pas le contrôle de tous les détails internes.

Commencez par inspecter le widget dans une application de test. Modifiez un seul aspect à la fois : taille, espacement, contour, indicateur activé ou état désactivé. Vérifiez que l'indicateur reste compréhensible sans couleur.

## 5. Barres de progression et curseurs

G-OS définit déjà dans GTK 3 :

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

La piste représente la zone totale ; la partie remplie représente la progression ou la valeur sélectionnée. Ne confondez pas le contrôle `scale` (curseur de valeur) avec le pointeur de souris (thème Xcursor).

Testez les curseurs horizontaux et verticaux, les valeurs minimales et maximales, ainsi que les états désactivés.

## 6. Listes et lignes sélectionnées

Les applications GTK utilisent différents conteneurs : listes, vues arborescentes, lignes de navigation et listes encadrées. La classe `.sidebar row` est utilisée par G-OS pour les lignes de barre latérale GTK 3.

Exemple réel :

```css
.sidebar row:selected {
  background-color: #dcecff;
  color: #075eb5;
}
```

Ne généralisez pas cette règle à toutes les lignes de toutes les applications. Une ligne sélectionnée dans une liste de fichiers peut nécessiter une autre couleur ou un indicateur distinct.

## 7. GTK 4 et contrôles Libadwaita

Les feuilles GTK 4 de G-OS définissent des couleurs sémantiques et quelques règles de surface. Elles ne redéfinissent pas chaque contrôle interne. Les applications Libadwaita peuvent ignorer les thèmes tiers et appliquer leurs propres styles.

Pour un contrôle GTK 4, commencez par identifier si son apparence vient du widget GTK, d'une classe CSS de l'application ou de Libadwaita. N'ajoutez pas des sélecteurs supposés fonctionner partout.

## 8. Méthode de création d'un nouveau style

1. Identifiez le moteur exact.
2. Repérez le widget et sa classe CSS réelle.
3. Relevez son apparence dans les états normal, focus, hover et disabled.
4. Ajoutez une règle minimale dans la feuille correspondante.
5. Reproduisez la même intention dans la variante sombre.
6. Testez avec le clavier et la souris.
7. Vérifiez les textes longs et les tailles d'affichage agrandies.

## 9. Erreurs fréquentes

- Modifier uniquement le style normal et oublier hover ou focus.
- Utiliser un sélecteur GTK dans GNOME Shell.
- Cibler une classe provenant d'une application particulière comme si elle était universelle.
- Masquer l'indicateur de focus pour obtenir une apparence plus épurée.
- Forcer une hauteur fixe qui coupe le texte traduit.
- Utiliser `!important` avant d'avoir compris la cascade.

## 10. Règle de maintenance

G-OS doit conserver des contrôles immédiatement reconnaissables. La cohérence visuelle ne doit jamais rendre ambiguë l'activation d'une case, la valeur d'un curseur ou l'indisponibilité d'un bouton.

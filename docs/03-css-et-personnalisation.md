# Comprendre et modifier les feuilles CSS

## 1. Commencer par identifier le moteur

Avant de modifier une règle, déterminez si le composant appartient à GNOME Shell, GTK 3 ou GTK 4/Libadwaita.

- Un menu système ou la barre supérieure relève généralement de GNOME Shell.
- Un widget d'une application GTK 3 relève de GTK 3.
- Un widget d'une application GTK 4 relève de GTK 4, éventuellement avec les conventions Libadwaita.

Une règle placée dans le mauvais dossier ne sera pas appliquée, même si sa syntaxe semble correcte.

## 2. Anatomie d'une règle CSS

Une règle associe un sélecteur à des déclarations :

```css
.example-widget {
  color: #20242b;
  background-color: #ffffff;
  border-radius: 10px;
  padding: 8px 12px;
}
```

Le sélecteur `.example-widget` cible les éléments qui portent cette classe. Les déclarations définissent des propriétés et leurs valeurs. Cet exemple illustre la syntaxe CSS générale ; il ne garantit pas que cette classe existe dans G-OS ou dans un composant GNOME.

Une règle n'a d'effet que si le moteur comprend la propriété et si le sélecteur correspond à un élément réellement présent.

## 3. Couleurs et contrastes

Les propriétés les plus courantes sont :

- `color` pour la couleur du texte ;
- `background-color` pour la surface ;
- `border-color` pour la bordure ;
- `outline-color` pour le contour lorsque le moteur le prend en charge.

Exemple :

```css
.example-widget {
  color: #20242b;
  background-color: #f5f7fa;
  border: 1px solid #dce2ea;
}
```

Vérifiez les états normal, survolé, actif, sélectionné et désactivé. Une couleur lisible dans l'état normal peut devenir illisible lorsqu'elle est utilisée avec une sélection ou une surface sombre.

## 4. Espacements et dimensions

Les propriétés de boîte courantes comprennent `margin`, `padding`, `min-width`, `min-height`, `max-width` et `max-height`, sous réserve de la prise en charge par le moteur concerné.

Exemple :

```css
.example-widget {
  min-height: 36px;
  padding: 6px 10px;
  margin: 4px;
}
```

Ne réduisez pas arbitrairement les zones interactives pour obtenir une capture plus compacte. Les contrôles doivent rester faciles à viser et les textes doivent pouvoir s'afficher sans être coupés.

## 5. Bordures, rayons et ombres

Les propriétés telles que `border`, `border-radius` et `box-shadow` sont courantes en CSS, mais leur disponibilité et leur rendu dépendent du moteur.

Exemple de surface :

```css
.example-surface {
  border: 1px solid rgba(30, 45, 65, 0.12);
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(20, 30, 45, 0.08);
}
```

Dans GNOME Shell, vérifiez le rendu réel : certaines propriétés CSS web ne sont pas prises en charge ou peuvent se comporter différemment.

## 6. États interactifs

Les pseudo-classes CSS usuelles comprennent `:hover`, `:active`, `:focus` et `:disabled`, mais les moteurs GNOME disposent aussi de conventions propres aux widgets et aux états.

Ne supposez pas qu'une pseudo-classe web fonctionne partout. Consultez la documentation du moteur et inspectez le composant avec les outils adaptés.

Exemple générique :

```css
.example-button:hover {
  background-color: #e8eef8;
}

.example-button:active {
  background-color: #d8e4f5;
}
```

Cet exemple est un point de départ pédagogique. Adaptez le sélecteur aux classes réellement exposées par le composant ciblé.

## 7. Méthode de modification sûre

1. Identifiez le composant et son moteur.
2. Recherchez sa classe dans les sources ou dans l'inspecteur approprié.
3. Repérez la règle existante la plus proche.
4. Modifiez cette règle au lieu d'ajouter plusieurs surcharges concurrentes.
5. Testez le composant dans son état normal et ses états interactifs.
6. Testez les variantes claire et sombre.
7. Vérifiez les autres composants qui partagent le même sélecteur.

Conservez les sélecteurs spécifiques. Une règle globale comme `* { ... }` peut modifier involontairement des icônes, des champs de saisie, des menus et des contrôles imbriqués.

## 8. Outils de diagnostic

Pour rechercher une classe ou une propriété dans le dépôt :

```bash
grep -RIn --include='*.css' 'nom-de-classe' gnome-shell gtk-3.0 gtk-4.0
```

Pour afficher les modifications locales :

```bash
git diff --check
git diff
```

`git diff --check` détecte notamment des erreurs d'espacement et des marqueurs de conflit ; il ne valide pas la syntaxe ni le rendu CSS.

## 9. Valider sans risquer sa session principale

Les changements de style GNOME Shell peuvent rendre l'interface difficile à utiliser si une règle provoque un problème. Travaillez par petites modifications et gardez un moyen de revenir au thème précédent.

Validez les trois cibles séparément. Une feuille GTK correcte ne prouve pas que la feuille Shell est correcte. Une capture d'écran doit être prise sur la version de GNOME réellement visée.

## 10. Règle de maintenance

Avant d'ajouter une propriété, vérifiez qu'elle est utile, comprise par le moteur et cohérente avec les autres composants. Préférez une règle courte et ciblée à une succession de correctifs contradictoires. Le thème doit rester facile à lire, à tester et à maintenir.

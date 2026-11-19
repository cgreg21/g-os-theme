# 3. Comprendre et modifier les feuilles CSS

## 3.1 Une règle CSS

Une règle CSS comporte un sélecteur et un bloc de déclarations.

```css
#panel {
  background-color: #f8f9fb;
  color: #252a33;
}
```

- `#panel` cible l'élément dont l'identifiant est panel.
- `background-color` définit la couleur de fond.
- `color` définit la couleur du texte et de certains contenus hérités.

Une déclaration se termine par un point-virgule. Les accolades délimitent le bloc.

## 3.2 Couleurs

Les couleurs sont écrites en hexadécimal ou avec une fonction telle que `rgba()`.

```css
background-color: #ffffff;
color: #0878e8;
border-color: rgba(30, 42, 58, 0.12);
```

Dans GTK, une couleur nommée peut être déclarée avec `@define-color`, puis réutilisée avec `@nom`.

```css
@define-color accent_color #0878e8;
button:focus {
  border-color: @accent_color;
}
```

Les variables `@define-color` sont propres au langage CSS de GTK et ne doivent pas être copiées telles quelles dans la feuille GNOME Shell.

## 3.3 Sélecteurs courants

- `button` cible les boutons.
- `entry` cible les champs de saisie GTK.
- `.sidebar` cible un élément portant la classe sidebar.
- `#panel` cible un élément portant l'identifiant panel.
- `:hover` décrit le survol du pointeur.
- `:focus` décrit l'état de focus clavier.
- `:disabled` décrit un contrôle désactivé.
- `:checked` décrit un contrôle activé lorsqu'il expose cet état.

Les classes disponibles dépendent du composant et de sa version. Pour GNOME Shell, inspecte les noms de classes du composant dans les sources de GNOME Shell 51.

## 3.4 États interactifs

Un bouton doit rester compréhensible dans tous ses états. Exemple GTK :

```css
button {
  background-color: #ffffff;
  color: #20242c;
  border: 1px solid rgba(30, 42, 58, 0.14);
  border-radius: 9px;
}
button:hover { background-color: #edf4fc; }
button:active { background-color: #e2efff; }
button:disabled { color: #a3aab5; }
```

Ne supprime pas l'indication de focus clavier : elle est essentielle à l'accessibilité.

## 3.5 Arrondis, espacements et bordures

- `border-radius` arrondit les angles lorsque le composant prend en charge cette propriété.
- `border` dessine une bordure.
- `padding` règle l'espace intérieur.
- `margin` règle l'espace extérieur.
- `box-shadow` ajoute une ombre lorsque le moteur l'implémente.

Toutes les propriétés ne sont pas disponibles dans toutes les couches. Teste une seule propriété sur un composant avant de généraliser.

## 3.6 Modifier la palette

Pour changer la couleur d'accent GTK 3 claire, modifie `@define-color accent_color` dans `gtk-3.0/gtk.css`. Pour le mode sombre, effectue le changement correspondant dans `gtk-3.0/gtk-dark.css`.

Pour le Shell, modifie les couleurs utilisées dans `gnome-shell/gnome-shell.css`. Les couleurs du Shell ne sont pas automatiquement liées aux variables GTK.

## 3.7 Méthode de travail

1. Crée une branche Git avant de modifier les sources.
2. Modifie un seul composant.
3. Recharge le thème ou relance la session de test.
4. Vérifie les états normal, survol, focus, actif et désactivé.
5. Vérifie le contraste du texte et des icônes.
6. Étends la modification aux autres composants seulement après validation.

## 3.8 Limites

Une feuille de style ne peut pas créer un composant qui n'existe pas, changer le comportement fonctionnel d'un widget ou garantir le style d'une application qui refuse les thèmes externes. Le CSS GNOME Shell est également lié aux classes internes de la version de GNOME installée.

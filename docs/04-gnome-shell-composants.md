# GNOME Shell : composants et personnalisation

Ce chapitre décrit les sélecteurs effectivement présents dans `gnome-shell/gnome-shell.css`. Il explique leur intention et la manière de les modifier. Les noms de classes de GNOME Shell sont des détails d'implémentation : leur présence dans la feuille du thème ne garantit pas qu'ils soient utilisés par toutes les constructions de GNOME Shell 51. Il faut vérifier le rendu dans la session cible.

## 1. Localiser la feuille Shell

Le fichier principal est :

```text
gnome-shell/gnome-shell.css
```

Les couleurs du thème sont déclarées au début avec `@define-color`. Les règles qui suivent ciblent les composants du bureau. Contrairement à une application GTK classique, GNOME Shell utilise St et son moteur CSS ; toutes les propriétés du CSS web ne sont pas disponibles.

## 2. La scène et la typographie

La règle `stage` définit la couleur de texte et la famille typographique par défaut de la scène Shell :

```css
stage {
  color: #20242c;
  font-family: "Inter", "Cantarell", sans-serif;
}
```

La liste de familles est ordonnée : le système utilise la première police disponible. Cantarell constitue ici une solution de repli adaptée à GNOME. Si Inter n'est pas installée, le thème doit rester lisible.

Pour changer la police, modifiez la liste sans imposer une police absente du système. Vérifiez les caractères accentués, les chiffres, les symboles et les tailles dans les menus et les notifications.

## 3. Barre supérieure

Le sélecteur `#panel` cible la barre supérieure. Le thème définit sa surface, sa couleur de texte, sa bordure inférieure et une ombre discrète.

```css
#panel {
  background-color: rgba(248, 249, 251, .94);
  color: #252a33;
  border-bottom: 1px solid rgba(25, 35, 50, .10);
  box-shadow: 0 1px 8px rgba(25, 35, 50, .06);
}
```

Les boutons de cette barre sont ciblés par `#panel .panel-button`. La feuille définit des styles distincts pour les états survolé, actif et sélectionné.

```css
#panel .panel-button:hover,
#panel .panel-button:active,
#panel .panel-button:checked {
  background-color: rgba(8, 120, 232, .11);
  color: #075eb5;
}
```

Le sélecteur `:focus` ajoute un contour visible. Ne le supprimez pas sans fournir un indicateur de focus alternatif : les utilisateurs qui naviguent au clavier doivent pouvoir identifier le contrôle actif.

Pour modifier la hauteur apparente, ne commencez pas par forcer une hauteur globale. Les dimensions de la barre dépendent aussi des métriques des widgets et de la configuration de la session. Ajustez les marges et espacements avec prudence puis vérifiez les indicateurs, l'horloge et les menus.

## 4. Menus contextuels et menus système

Les sélecteurs `.popup-menu-boxpointer` et `.candidate-popup-boxpointer` règlent la bulle qui porte le menu et sa flèche. Les propriétés préfixées par `-arrow-` sont spécifiques à St ; elles ne sont pas des propriétés CSS standard.

```css
.popup-menu-boxpointer,
.candidate-popup-boxpointer {
  -arrow-border-radius: 14px;
  -arrow-background-color: #ffffff;
  -arrow-border-color: rgba(30, 42, 58, .12);
  -arrow-border-width: 1px;
  -arrow-base: 24px;
  -arrow-rise: 12px;
}
```

Le contenu du menu est stylé par `.popup-menu-content`. Les lignes sont ciblées par `.popup-menu-item`, avec des variantes pour le survol, le focus et l'activation.

Lorsque vous changez le rayon du menu, vérifiez que la flèche et le panneau semblent former une seule surface. Un rayon trop grand ou une bordure trop contrastée peut créer une séparation visuelle artificielle.

## 5. Quick Settings

Le conteneur `.quick-settings` règle l'espacement général du panneau. Les boutons bascule sont ciblés par `.quick-toggle` et `.quick-menu-toggle`.

```css
.quick-toggle,
.quick-menu-toggle {
  border-radius: 12px;
  background-color: #eef1f5;
  color: #252a33;
}

.quick-toggle:checked {
  background-color: #0878e8;
  color: #ffffff;
}
```

L'état sélectionné doit rester compréhensible sans dépendre uniquement de la couleur. Vérifiez les icônes, les libellés et le contraste des contrôles actifs et inactifs. Testez les bascules Wi-Fi, Bluetooth, mode avion et les contrôles réellement disponibles sur la machine.

## 6. Calendrier et date

La classe `.calendar` définit la couleur de base. La règle `.calendar .calendar-day` cible les jours, puis les pseudo-classes `:selected` et `:hover` distinguent la sélection et le survol.

```css
.calendar .calendar-day:selected {
  background-color: #0878e8;
  color: #ffffff;
}
```

Vérifiez les jours du mois précédent et du mois suivant, la date du jour, la date sélectionnée et les jours survolés. Les noms de classes internes peuvent changer ; si aucune modification n'est visible, inspectez la hiérarchie réelle avant d'ajouter une nouvelle surcharge.

## 7. Notifications

Le thème cible `.message-list`, `.message` et `.notification-banner`. La carte de notification possède une surface, une bordure, un rayon et une ombre.

```css
.notification-banner {
  background-color: #ffffff;
  color: #20242c;
  border: 1px solid rgba(30, 42, 58, .12);
  border-radius: 14px;
  box-shadow: 0 8px 26px rgba(22, 32, 48, .14);
}
```

Ne réduisez pas les espacements au point de rendre les actions difficiles à atteindre. Vérifiez les notifications longues, les notifications contenant plusieurs actions et les notifications groupées.

## 8. Vue des activités et dash

Le fichier contient des règles pour `#dash`, `.dash-item-container .app-well-app` et `.overview-tile`. Elles définissent les surfaces et les rayons des éléments du lanceur et de la vue d'ensemble.

La règle `.search-entry` stylise le champ de recherche et son état de focus. Testez une recherche vide, une recherche avec résultats, une recherche sans résultat et la navigation au clavier.

Les dimensions et positions du dash sont gérées par GNOME Shell. Un thème doit éviter de les forcer lorsqu'une propriété visuelle suffit.

## 9. Dialogues

Le sélecteur `.modal-dialog` définit la surface du dialogue. Les boutons sont ciblés par `.modal-dialog-button`, et le bouton principal par `.modal-dialog-button.default`.

Conservez une distinction nette entre action principale et actions secondaires. Vérifiez les dialogues étroits, les textes longs et les boutons dont le libellé est traduit.

## 10. Vérifier une règle Shell

Procédez par modification isolée :

1. Notez le composant à modifier.
2. Recherchez son sélecteur dans le fichier.
3. Changez une seule propriété.
4. Enregistrez puis rechargez le thème par le mécanisme compatible avec votre session.
5. Observez le composant dans plusieurs états.
6. Revenez au fichier précédent si le Shell présente des artefacts.

Sous Wayland, le redémarrage du Shell n'est pas équivalent à celui des anciennes sessions X11. Préférez une session de test ou une déconnexion/reconnexion plutôt que de supposer qu'une commande de redémarrage fonctionne partout.

## 11. Limites

Une feuille CSS ne crée pas un composant absent et ne modifie pas sa logique. Les sélecteurs listés ici décrivent le thème du dépôt ; ils doivent être confrontés à la version précise de GNOME Shell. Ne présentez jamais un sélecteur comme universel sans l'avoir vérifié dans le code ou l'inspecteur de la version cible.

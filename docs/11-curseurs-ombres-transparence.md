# Curseurs, ombres, transparence et effets visuels

Ce chapitre sépare les effets que l'on peut régler en CSS des ressources et paramètres gérés par GNOME ou le système graphique.

## 1. Les curseurs ne sont pas des règles CSS

Le curseur de souris est fourni par un thème Xcursor. G-OS déclare actuellement Adwaita dans `index.theme` :

```ini
[X-GNOME-Metatheme]
CursorTheme=Adwaita
```

Le dépôt ne contient pas de répertoire `cursors/` : il ne fournit donc pas de curseur personnalisé.

Pour consulter le thème actif :

```bash
gsettings get org.gnome.desktop.interface cursor-theme
gsettings get org.gnome.desktop.interface cursor-size
```

Pour tester un autre thème installé :

```bash
gsettings set org.gnome.desktop.interface cursor-theme 'Adwaita'
```

Le changement de réglage agit sur la session utilisateur. Conservez la valeur précédente si vous souhaitez revenir en arrière.

## 2. Structure d'un thème Xcursor

Un thème de curseurs est généralement installé dans un répertoire nommé d'après le thème, avec un sous-répertoire `cursors/` contenant les ressources Xcursor. Un fichier `index.theme` peut déclarer l'héritage.

Les curseurs doivent fournir les formes et les tailles utiles : flèche normale, main, redimensionnement, attente, déplacement, sélection de texte et autres rôles. Le point chaud (hotspot) indique le pixel qui correspond à la position réelle du pointeur.

Un thème incomplet peut afficher des curseurs provenant du thème parent. Vérifiez la licence de chaque ressource avant redistribution.

## 3. Ce que CSS peut réellement modifier

CSS peut modifier l'apparence de surfaces dessinées par GNOME Shell ou GTK : couleur de fond, bordure, rayon, ombre et parfois opacité. Il ne peut pas remplacer le fichier du curseur système, son hotspot ou sa résolution.

Dans les feuilles G-OS, les ombres sont utilisées notamment sur le panneau, les menus, les notifications, le dash et les dialogues Shell. Exemple réel du thème :

```css
#panel {
  box-shadow: 0 1px 8px rgba(25,35,50,.06);
}
```

Les valeurs de flou et de décalage doivent rester modérées. Une ombre trop forte rend les surfaces visuellement lourdes et peut réduire la lisibilité des séparations.

## 4. Comprendre une ombre

La syntaxe courante est :

```css
.exemple {
  box-shadow: 0 8px 24px rgba(22,32,48,.16);
}
```

Les valeurs décrivent le décalage horizontal, le décalage vertical, le rayon de flou, éventuellement l'étalement, puis la couleur. Cet exemple est générique ; la classe `.exemple` n'est pas fournie par G-OS.

Le moteur CSS peut imposer des limites ou interpréter différemment certaines propriétés. Testez chaque effet sur le moteur concerné. Évitez les piles de plusieurs ombres si une seule suffit.

## 5. Transparence : alpha et arrière-plan

Une couleur avec canal alpha permet de rendre une surface partiellement transparente :

```css
.exemple {
  background-color: rgba(255, 255, 255, .88);
}
```

G-OS utilise déjà des couleurs alpha sur le panneau et le dash GNOME Shell. Une transparence CSS ne garantit toutefois pas un flou de l'arrière-plan. Le flou est un effet de composition distinct, dépendant du compositeur et du composant.

Une surface transparente peut laisser apparaître des contenus qui réduisent le contraste du texte. Testez-la sur des fonds clairs, sombres et chargés.

## 6. Flou d'arrière-plan et limites

La propriété CSS standard `backdrop-filter` n'est pas une solution portable pour les feuilles GNOME Shell et GTK. Ne l'ajoutez pas en supposant qu'elle produira un effet de verre dépoli.

Les effets de flou du bureau peuvent dépendre du compositeur, d'extensions spécifiques ou de mécanismes propres à une version de GNOME. Ils ne sont pas équivalents à une propriété de thème CSS générique.

Pour G-OS, privilégiez une surface semi-transparente avec bordure et contraste contrôlé plutôt qu'une dépendance à un effet de flou non garanti.

## 7. Rayon des angles et bordures

Le thème utilise des rayons arrondis sur les menus, les notifications, les boutons et les dialogues. Exemple réel :

```css
.popup-menu-content {
  border: 1px solid rgba(30,42,58,.12);
  border-radius: 14px;
}
```

Une cohérence visuelle vient de quelques rayons réutilisés, pas d'une valeur différente sur chaque élément. Gardez les rayons des petits contrôles plus faibles que ceux des grands panneaux.

## 8. Animations et transitions

Le thème Shell utilise une transition courte sur les boutons du panneau :

```css
#panel .panel-button {
  transition-duration: 120ms;
}
```

Les transitions CSS ne remplacent pas les animations fonctionnelles de GNOME. Évitez d'animer de nombreuses propriétés coûteuses ou d'introduire des mouvements qui ralentissent les interactions.

Respectez les préférences de réduction des animations lorsqu'un composant ou une application les expose. Une feuille de thème ne peut pas garantir à elle seule que toutes les animations du bureau seront supprimées.

## 9. Contrôler les effets

Pour chaque effet ajouté, vérifiez :

- la lisibilité du texte et des icônes ;
- le contraste de la bordure sur les deux modes ;
- le rendu avec plusieurs fenêtres derrière les surfaces transparentes ;
- la netteté des contours à différentes échelles ;
- les performances sur une machine moins puissante ;
- le comportement au clavier et au focus.

Ne combinez pas simultanément une nouvelle transparence, une ombre, un rayon et une animation. Introduisez les changements séparément afin d'identifier leur impact.

## 10. État actuel de G-OS

Le dépôt déclare le curseur Adwaita et ne contient pas de ressources Xcursor. Les effets visuels sont définis directement dans les feuilles CSS, principalement dans `gnome-shell/gnome-shell.css`. GTK 3 et GTK 4 possèdent leurs propres règles de surfaces et de bordures, mais ne partagent pas automatiquement les effets Shell.

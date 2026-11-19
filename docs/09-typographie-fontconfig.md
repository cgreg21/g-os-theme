# Typographie, polices et Fontconfig

Ce chapitre explique comment choisir les polices utilisées par G-OS, distinguer une police système d'une règle CSS et diagnostiquer un rendu typographique incorrect.

## 1. Les trois niveaux à ne pas confondre

La typographie d'un bureau GNOME dépend de plusieurs couches :

- **Installation des polices** : les fichiers de fontes sont installés dans les répertoires système ou dans le dossier personnel.
- **Fontconfig** : détecte les polices disponibles et résout les familles demandées vers une fonte installée.
- **CSS** : demande une famille, une taille, une graisse et d'autres propriétés aux moteurs GTK ou GNOME Shell.

Une feuille CSS ne contient pas une police. Elle ne fait que demander son utilisation. Si la famille demandée n'est pas disponible, le moteur choisit une police de remplacement.

## 2. Lire la règle typographique du thème Shell

Le fichier `gnome-shell/gnome-shell.css` contient actuellement :

```css
stage {
  color: #20242c;
  font-family: "Inter", "Cantarell", sans-serif;
}
```

Cette règle demande Inter en priorité, puis Cantarell, puis une famille générique sans empattement. La présence de plusieurs familles constitue une chaîne de repli : le système utilise la première famille qu'il peut résoudre.

Pour GTK 3 et GTK 4, le dépôt ne définit pas actuellement de famille globale dans ses feuilles. Les applications conservent donc leur choix typographique par défaut, sauf règles propres à leurs widgets ou préférences de l'application.

## 3. Installer une police pour l'utilisateur

Pour installer une police sans privilèges administrateur, créez le répertoire utilisateur :

```bash
mkdir -p ~/.local/share/fonts
```

Copiez-y les fichiers de police autorisés, par exemple les fichiers `.ttf` ou `.otf`, puis reconstruisez le cache :

```bash
fc-cache -f ~/.local/share/fonts
```

Pour une installation système, les polices peuvent être placées dans un répertoire prévu à cet effet sous `/usr/local/share/fonts`, avec les droits administrateur. Une installation utilisateur est préférable pour expérimenter et éviter de modifier le système.

N'intégrez pas une police dans le dépôt sans vérifier sa licence de redistribution. Le fait qu'une police soit téléchargeable gratuitement ne signifie pas nécessairement que ses fichiers peuvent être redistribués.

## 4. Vérifier la résolution d'une famille

Interrogez Fontconfig :

```bash
fc-match Inter
fc-match Cantarell
fc-list : family | sort -u
```

`fc-match` indique la police réellement choisie pour une demande donnée. Si `fc-match Inter` renvoie une autre famille, Inter n'est probablement pas installée ou n'est pas reconnue sous ce nom.

Pour inspecter les informations d'une police :

```bash
fc-query ~/.local/share/fonts/ma-police.ttf
```

Adaptez le chemin au fichier installé.

## 5. Modifier la famille utilisée par GNOME Shell

Pour tester une autre famille, modifiez la déclaration `stage` dans `gnome-shell/gnome-shell.css` :

```css
stage {
  color: #20242c;
  font-family: "Cantarell", sans-serif;
}
```

Ne changez que la propriété nécessaire. Conservez une famille générique en dernier recours. Après installation du thème ou modification de la feuille active, rechargez la session Shell selon votre environnement. Sous Wayland, une déconnexion puis reconnexion est la méthode la plus fiable.

## 6. Taille, graisse et hauteur de ligne

Les propriétés CSS courantes sont :

```css
.exemple {
  font-family: "Cantarell", sans-serif;
  font-size: 1rem;
  font-weight: 500;
  font-style: normal;
  line-height: 1.35;
  letter-spacing: 0;
}
```

Cet exemple est générique : `.exemple` n'est pas une classe déclarée par G-OS. Les moteurs CSS de GNOME Shell et GTK ont des compatibilités et des valeurs par défaut différentes. Vérifiez la propriété dans le moteur ciblé avant de généraliser une règle.

Évitez de fixer une taille absolue partout. Les tailles relatives facilitent l'adaptation, mais elles ne remplacent pas les réglages d'échelle de GNOME ni les tests avec des textes longs.

## 7. Graisses et familles variables

Une famille peut proposer plusieurs graisses. Si la fonte ne fournit pas la graisse demandée, le moteur peut sélectionner une variante proche ou synthétiser un style. Vérifiez les variantes disponibles avec :

```bash
fc-list | grep -i 'Inter'
```

Une fonte variable peut contenir plusieurs axes, mais le support de la syntaxe CSS avancée dépend du moteur et de sa version. Pour un thème destiné à plusieurs applications, privilégiez les valeurs usuelles comme 400, 500, 600 et 700.

## 8. Prévenir les défauts de mise en page

Une police différente modifie la largeur des caractères, la hauteur des lignes et parfois la taille minimale des widgets. Après chaque changement, vérifiez :

- les libellés longs dans les menus ;
- les boutons contenant plusieurs mots ;
- les notifications et leurs titres ;
- les champs de recherche ;
- les caractères accentués et les langues utilisant d'autres alphabets ;
- les tailles d'interface agrandies.

Ne corrigez pas un texte tronqué en réduisant globalement la taille de police. Cherchez d'abord le conteneur trop étroit ou la contrainte de largeur responsable.

## 9. Diagnostic

Si la police attendue n'apparaît pas :

1. Vérifiez l'orthographe du nom de famille.
2. Lancez `fc-match "Nom de la police"`.
3. Vérifiez le cache avec `fc-cache -f`.
4. Vérifiez que le bon fichier CSS est chargé.
5. Contrôlez si l'application impose sa propre police.
6. Redémarrez l'application ou la session concernée.

## 10. Règle de maintenance G-OS

Le thème demande actuellement Inter puis Cantarell dans GNOME Shell. Ne supposez pas que les deux familles sont installées sur chaque machine. Gardez une chaîne de repli et ne distribuez pas de fichiers de police sans licence vérifiée.

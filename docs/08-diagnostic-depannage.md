# Diagnostic et dépannage du thème

Ce chapitre donne une méthode reproductible pour comprendre pourquoi une règle ne produit pas le résultat attendu. Il s'adresse aux personnes qui découvrent GNOME comme à celles qui développent des thèmes.

## 1. Identifier le moteur responsable

Avant de modifier une feuille, identifiez le composant :

- Barre supérieure, calendrier, Quick Settings, notifications et vue d'ensemble : GNOME Shell.
- Fenêtre et widgets d'une application GTK 3 : GTK 3.
- Widgets d'une application GTK 4 : GTK 4.
- Composants d'une application Libadwaita : styles Libadwaita, avec des possibilités limitées de surcharge.

Une application peut mélanger plusieurs composants. Par exemple, sa fenêtre peut être dessinée par GTK alors que son contenu utilise des widgets Libadwaita.

## 2. Vérifier que le thème est installé

Le script installe les fichiers dans `~/.themes/G-OS`. Vérifiez le contenu :

```bash
test -f "$HOME/.themes/G-OS/gnome-shell/gnome-shell.css"
test -f "$HOME/.themes/G-OS/gtk-3.0/gtk.css"
test -f "$HOME/.themes/G-OS/gtk-4.0/gtk.css"
```

Si une commande échoue, relancez l'installation depuis la racine du dépôt :

```bash
./install.sh
```

Le script copie les fichiers ; il ne sélectionne pas automatiquement le thème dans les paramètres GNOME.

## 3. Vérifier le thème GTK 3 actif

La variable d'environnement `GTK_THEME` peut servir à tester temporairement un thème pour une application GTK 3 :

```bash
GTK_THEME=G-OS application
```

Remplacez `application` par le nom de l'exécutable concerné. Cette méthode est un test ponctuel, pas un réglage global recommandé. Certaines applications peuvent ignorer ou remplacer une partie du style.

Pour voir les variables GTK de votre session :

```bash
env | grep -E '^(GTK|GDK)_'
```

## 4. Vérifier la feuille GNOME Shell

Le thème Shell est chargé séparément des thèmes GTK. L'extension User Themes doit être activée et le thème sélectionné dans l'outil de configuration utilisé.

Vérifiez que le fichier existe dans le répertoire installé et que le nom du thème correspond au dossier sélectionné. Si une règle ne change rien, contrôlez d'abord que le sélecteur existe dans la version exacte de GNOME Shell utilisée.

Ne lancez pas de redémarrage forcé du Shell sur une session Wayland en supposant que le raccourci historique X11 est disponible. Une déconnexion/reconnexion ou une session de test est plus fiable.

## 5. Comprendre une règle qui ne s'applique pas

Suivez cet ordre :

1. Vérifiez le chemin du fichier chargé.
2. Vérifiez le moteur : Shell, GTK 3 ou GTK 4.
3. Vérifiez que le widget possède réellement la classe ciblée.
4. Vérifiez que le sélecteur est valide pour ce moteur.
5. Vérifiez qu'une règle plus spécifique ne prend pas le dessus.
6. Vérifiez l'état du widget : normal, hover, active, checked, selected, disabled ou focus.
7. Redémarrez l'application ou rechargez la session selon le moteur.

Ne corrigez pas un problème de sélecteur en ajoutant immédiatement `!important`. Cela masque souvent la cause et rend les évolutions ultérieures plus difficiles.

## 6. Examiner les avertissements GTK

Lancez une application depuis un terminal pour voir les avertissements éventuels :

```bash
G_MESSAGES_DEBUG=all application
```

Cette commande peut produire beaucoup de messages. Concentrez-vous sur les avertissements CSS et les erreurs qui apparaissent au chargement de la feuille. Tous les messages GTK ne signalent pas un défaut du thème.

Pour GNOME Shell, consultez le journal de la session :

```bash
journalctl --user -b | grep -iE 'gnome-shell|stylesheet|css'
```

Les journaux peuvent contenir des informations sans rapport avec le thème ; comparez les messages avant et après une modification.

## 7. Tester une modification sans perdre l'état fonctionnel

Avant de modifier un fichier :

```bash
cp gtk-3.0/gtk.css /tmp/g-os-gtk.css.backup
```

Effectuez une seule modification, testez-la, puis comparez le résultat. Pour restaurer cette copie :

```bash
cp /tmp/g-os-gtk.css.backup gtk-3.0/gtk.css
```

Pour une modification de palette, mettez à jour les variantes claire et sombre et vérifiez qu'elles conservent les mêmes rôles sémantiques.

## 8. Distinguer défaut du thème et limite de l'application

Si une application Libadwaita ne change pas d'apparence alors que GTK 3 ou une application GTK 4 classique change, ce comportement peut être normal. Libadwaita contrôle volontairement une partie importante de son apparence.

Ne contournez pas cette limite en modifiant les ressources système. Documentez le comportement observé et concentrez le thème sur les composants qui acceptent officiellement la personnalisation.

## 9. Préparer un rapport de bug utile

Un rapport reproductible doit contenir :

- Version exacte de GNOME Shell.
- Version GTK concernée.
- Nom de l'application et, si possible, sa version.
- Mode clair ou sombre.
- Chemin du fichier modifié.
- Sélecteur et propriété concernés.
- Capture d'écran avant/après.
- Messages d'erreur pertinents du terminal ou du journal.

Décrivez le résultat attendu et le résultat réellement observé. Évitez les captures recadrées qui ne montrent pas quel composant est concerné.

## 10. Contrôle avant de publier

Depuis la racine du dépôt :

```bash
bash -n install.sh
test -s gnome-shell/gnome-shell.css
test -s gtk-3.0/gtk.css
test -s gtk-3.0/gtk-dark.css
test -s gtk-4.0/gtk.css
test -s gtk-4.0/gtk-dark.css
```

Ces commandes vérifient la syntaxe Bash et la présence des feuilles. Elles ne valident pas le rendu CSS. Une validation visuelle sur GNOME 51 reste indispensable.

## 11. Principe général

Modifiez une chose à la fois, identifiez toujours le moteur concerné et vérifiez le résultat dans l'application réelle. Un thème est fiable lorsqu'il reste compréhensible, réversible et testable, pas lorsqu'il accumule des surcharges.

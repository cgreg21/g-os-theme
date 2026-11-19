# Inspection et débogage CSS

Un thème doit être diagnostiqué à partir du composant réellement affiché et du moteur qui le dessine. Modifier des règles au hasard rend le dépannage lent et fragile.

## 1. Identifier le moteur CSS

Avant toute modification, déterminez si l'élément appartient à :
- GNOME Shell (St et Clutter) ;
- GTK 3 ;
- GTK 4 ;
- une application Libadwaita ;
- une extension Shell avec sa propre feuille ;
- une application qui dessine elle-même son interface.

Les moteurs partagent une syntaxe CSS proche, mais pas une compatibilité totale. Les propriétés spécifiques à GTK ou Shell ne sont pas universelles.

## 2. Ouvrir l'inspecteur GTK

GTK fournit un inspecteur graphique pour examiner les widgets, leur hiérarchie et leurs propriétés CSS. Selon la version de GTK et la manière dont l'application est lancée, l'inspecteur peut être activé par une variable d'environnement :

```bash
GTK_DEBUG=interactive nom-de-l-application
```

Cette commande lance l'application avec le débogage interactif activé si la version de GTK utilisée le prend en charge.

Pour une application déjà ouverte, le raccourci et la disponibilité de l'inspecteur dépendent de sa configuration et de sa version. L'inspecteur GTK 3 et celui de GTK 4 ne présentent pas exactement les mêmes informations.

N'utilisez pas cette méthode pour inspecter GNOME Shell : le Shell n'est pas une application GTK.

## 3. Inspecter GNOME Shell

GNOME Shell utilise St et son propre environnement de développement. L'inspection de la hiérarchie Shell nécessite les outils de débogage compatibles avec la version de Shell, ou une extension de développement dédiée.

Les journaux de la session sont consultables avec :

```bash
journalctl -b /usr/bin/gnome-shell
```

Selon la distribution, le filtre peut ne rien retourner. Une recherche plus large peut être utile :

```bash
journalctl -b | grep -i 'gnome-shell'
```

Les messages CSS et JavaScript peuvent aider à repérer un sélecteur invalide, une ressource absente ou une erreur d'extension.

## 4. Rechercher une classe dans le thème

Pour localiser les règles qui ciblent un composant :

```bash
grep -R -n 'popup-menu-content' gnome-shell gtk-3.0 gtk-4.0
grep -R -n 'headerbar' gtk-3.0 gtk-4.0
```

Cette recherche permet de repérer les règles du dépôt. Elle ne prouve pas que le widget affiché utilise cette classe : l'inspecteur ou le code source du composant reste nécessaire.

## 5. Vérifier quel thème est actif

Pour GTK, consultez les paramètres de thème :

```bash
gsettings get org.gnome.desktop.interface gtk-theme
gsettings get org.gnome.desktop.interface color-scheme
```

La disponibilité du réglage `color-scheme` dépend de la version de GNOME. Le thème GTK sélectionné et la préférence clair/sombre sont deux informations différentes.

Pour GNOME Shell, vérifiez que l'extension User Themes est installée et activée si vous utilisez un thème Shell installé dans le dossier utilisateur :

```bash
gnome-extensions list --enabled
```

## 6. Procéder par modifications minimales

Quand un composant ne prend pas l'apparence attendue :

1. Confirmez le moteur de rendu.
2. Confirmez que le bon thème est chargé.
3. Repérez la classe réelle du widget.
4. Recherchez les règles concurrentes.
5. Ajoutez une seule propriété de test.
6. Rechargez le composant ou l'application.
7. Consultez les journaux.
8. Conservez uniquement la correction validée.

Cette méthode permet de distinguer une erreur de syntaxe, un mauvais sélecteur, un thème non chargé et une limite du moteur.

## 7. Valider les feuilles CSS

Les moteurs GTK proposent des diagnostics au chargement, mais il n'existe pas un validateur CSS unique qui garantit la compatibilité simultanée avec GTK 3, GTK 4 et GNOME Shell.

Le contrôle textuel peut détecter des erreurs simples, mais ne prouve pas qu'une propriété est reconnue. La validation finale doit être faite dans le moteur cible.

Une vérification basique des fichiers :

```bash
test -s gnome-shell/gnome-shell.css
test -s gtk-3.0/gtk.css
test -s gtk-3.0/gtk-dark.css
test -s gtk-4.0/gtk.css
test -s gtk-4.0/gtk-dark.css
```

## 8. Comprendre la cascade

Lorsque plusieurs règles ciblent le même widget, le résultat dépend de leur origine, de leur spécificité, de leur ordre et parfois des styles appliqués directement au widget.

Une règle plus spécifique peut l'emporter sur une règle générale. Ajouter une déclaration identique à la fin du fichier n'est pas toujours suffisant.

Évitez de corriger un problème en ajoutant une série de sélecteurs de plus en plus complexes. Supprimez ou simplifiez les règles redondantes lorsque leur origine est identifiée.

## 9. Constituer un rapport de bug utile

Un rapport reproductible doit inclure :
- version de GNOME Shell ;
- version GTK concernée ;
- nom de l'application ou de l'extension ;
- mode clair ou sombre ;
- étapes exactes de reproduction ;
- résultat attendu et résultat observé ;
- extrait CSS minimal ;
- messages de journal pertinents ;
- capture d'écran si elle aide à comprendre le défaut.

Ne joignez pas de données personnelles ou de journaux complets contenant des informations privées.

## 10. Limites

L'inspecteur GTK ne permet pas d'inspecter l'arbre St de GNOME Shell. Les outils de débogage Shell ne remplacent pas l'inspecteur GTK. Un thème peut aussi être correctement chargé alors qu'une application Libadwaita ignore volontairement les styles tiers.

Le diagnostic commence toujours par l'identification du composant et de son moteur.

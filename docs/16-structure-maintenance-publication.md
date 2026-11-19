# Structure, maintenance et publication du thème

Ce chapitre décrit comment faire évoluer G-OS sans rendre son installation fragile. Il s'appuie sur la structure réelle du dépôt et sur la CI existante.

## 1. Structure actuelle

Le dépôt contient actuellement :

- `gnome-shell/gnome-shell.css` : feuille GNOME Shell ;
- `gtk-3.0/gtk.css` : variante claire GTK 3 ;
- `gtk-3.0/gtk-dark.css` : variante sombre GTK 3 ;
- `gtk-3.0/settings.ini` : réglages GTK 3 du thème ;
- `gtk-4.0/gtk.css` : variante claire GTK 4 ;
- `gtk-4.0/gtk-dark.css` : variante sombre GTK 4 ;
- `index.theme` : métadonnées du métathème ;
- `install.sh` : installation et désinstallation ;
- `.github/workflows/ci.yml` : validation automatisée ;
- `docs/` : manuel technique.

Ne créez pas un répertoire de ressources ou un sous-thème sans définir clairement son rôle, sa convention de nommage et son installation.

## 2. Responsabilité de chaque fichier

Une modification doit être placée dans le fichier qui correspond au moteur ciblé. Une règle Shell ne doit pas être copiée mécaniquement dans GTK. Les variantes GTK claire et sombre doivent rester cohérentes.

Les couleurs partagées peuvent être exprimées avec les mécanismes propres à chaque moteur. Les variables `@define-color` de GTK ne sont pas des variables CSS standard et ne sont pas interchangeables avec les déclarations GNOME Shell.

## 3. Principe KISS

Pour maintenir le thème :

- préférez une règle simple à plusieurs surcharges ;
- évitez les dépendances à des extensions non nécessaires ;
- ne dupliquez pas une déclaration si une règle existante peut être corrigée ;
- n'ajoutez pas de ressources externes chargées à l'exécution ;
- conservez les variantes claires et sombres lisibles ;
- documentez les sélecteurs internes fragiles ;
- retirez les règles devenues inutiles.

Une feuille CSS plus longue n'est pas automatiquement plus complète. Chaque règle doit corriger un besoin identifié.

## 4. Procédure avant modification

Avant de changer un fichier :

```bash
git status --short
git pull --ff-only
```

Lisez le bloc concerné et recherchez les règles existantes :

```bash
grep -n 'nom-du-selecteur' gnome-shell/gnome-shell.css
grep -R -n 'nom-du-selecteur' gtk-3.0 gtk-4.0
```

Travaillez sur une branche dédiée si le changement est conséquent. Gardez un diff limité et compréhensible.

## 5. Vérifications locales

Avant de publier :

```bash
bash -n install.sh
test -s gnome-shell/gnome-shell.css
test -s gtk-3.0/gtk.css
test -s gtk-3.0/gtk-dark.css
test -s gtk-4.0/gtk.css
test -s gtk-4.0/gtk-dark.css
```

Vérifiez aussi qu'aucune feuille ne charge de ressource distante :

```bash
if grep -R -nE 'https?://' gnome-shell gtk-3.0 gtk-4.0; then
  echo "Une ressource distante a été trouvée."
  exit 1
fi
```

Ces commandes correspondent aux vérifications présentes dans la CI actuelle. Elles ne remplacent pas un essai graphique.

## 6. Tester l'installation

Le script du dépôt installe le thème dans le dossier utilisateur. Avant d'utiliser une modification sur la session principale :

1. sauvegardez les fichiers de thème actuellement installés ;
2. lancez le script d'installation ;
3. vérifiez que tous les répertoires attendus sont copiés ;
4. activez le thème GTK ;
5. activez User Themes si le thème Shell doit être utilisé ;
6. testez une session GNOME ;
7. vérifiez le retour au thème précédent.

La désinstallation doit être testée séparément. Vérifiez qu'elle ne supprime pas un dossier qui n'appartient pas à G-OS.

## 7. CI actuelle

Le workflow `.github/workflows/ci.yml` s'exécute sur les push vers `main`, les pull requests et les déclenchements manuels. Il contrôle :

- la présence des cinq feuilles CSS attendues ;
- la syntaxe shell de `install.sh` ;
- la présence de la mention GNOME Shell 51 dans le README ;
- l'absence d'URL HTTP(S) dans les répertoires de feuilles de style.

La CI ne lance pas de session GNOME graphique et ne vérifie pas visuellement les composants. Un workflow vert signifie que ces contrôles automatisés ont réussi, pas que chaque widget a été testé.

## 8. Publier une évolution

Une publication propre suit cet ordre :

1. mettre à jour les feuilles ;
2. mettre à jour les variantes claires et sombres ;
3. actualiser les chapitres concernés ;
4. vérifier les commandes de validation ;
5. créer un commit explicite ;
6. pousser la branche ;
7. attendre la fin de la CI du commit exact ;
8. corriger et relancer en cas d'échec ;
9. ne créer un tag qu'après validation.

Le statut d'une ancienne exécution ne prouve pas que le dernier commit est validé. Il faut vérifier le SHA exact.

## 9. Numérotation et notes de version

Les versions doivent décrire les changements visibles et les changements de compatibilité. Une mise à jour CSS pure peut être mineure ; une modification de structure ou d'installation peut nécessiter une note plus importante.

Documentez :
- les composants modifiés ;
- les éventuelles incompatibilités ;
- les extensions ou versions testées ;
- les corrections du mode sombre ;
- les changements du script d'installation.

## 10. Critères de qualité

Une version G-OS est prête à être distribuée lorsque :
- les fichiers requis sont présents ;
- le script d'installation et de désinstallation est contrôlé ;
- les feuilles claire et sombre sont cohérentes ;
- les styles ne chargent aucune ressource distante ;
- les principaux composants ont été testés dans GNOME 51 ;
- les limites connues sont documentées ;
- la CI du commit publié est terminée et réussie.

Ne présentez jamais une validation automatisée comme un test graphique complet.

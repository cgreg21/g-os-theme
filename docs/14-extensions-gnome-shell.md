# Personnaliser les extensions GNOME Shell

Les extensions GNOME Shell ajoutent des composants à l'interface : indicateurs, menus, docks, panneaux, lanceurs et outils système. Elles s'exécutent dans le processus GNOME Shell et peuvent introduire leurs propres classes CSS.

Ce chapitre explique comment adapter leur apparence sans confondre le thème Shell avec le code d'une extension.

## 1. Thème Shell et extension : deux responsabilités

Le thème GNOME Shell fournit une feuille de style générale chargée par le Shell. Une extension fournit son propre code JavaScript, ses widgets et parfois ses propres règles CSS.

Une extension peut :
- réutiliser les classes natives du Shell ;
- ajouter ses propres classes ;
- charger une feuille CSS privée ;
- créer des widgets St ;
- utiliser des composants GTK dans une fenêtre externe.

Une règle de G-OS ne peut agir que sur les éléments qui existent dans l'arbre de widgets et qui sont exposés au moteur CSS. Elle ne peut pas styliser une fenêtre indépendante comme si elle était un composant Shell.

## 2. Identifier une extension installée

Les extensions utilisateur sont généralement stockées dans :

```bash
~/.local/share/gnome-shell/extensions/
```

Les extensions fournies par la distribution peuvent être installées dans un répertoire système, par exemple sous `/usr/share/gnome-shell/extensions/`.

Lister les extensions :

```bash
gnome-extensions list
gnome-extensions list --enabled
```

Afficher les informations d'une extension :

```bash
gnome-extensions info UUID
```

Remplacez `UUID` par l'identifiant retourné par la commande de liste.

## 3. Trouver les styles propres à une extension

Dans le répertoire de l'extension, recherchez les feuilles CSS et les classes utilisées dans le code :

```bash
find ~/.local/share/gnome-shell/extensions -type f \( -name '*.css' -o -name '*.js' \)
grep -R -nE 'add_style_class_name|add_style_class|add_class_name|className' ~/.local/share/gnome-shell/extensions
```

Les API disponibles varient avec la version de GNOME et le langage utilisé. L'objectif de cette recherche est d'identifier les classes effectivement ajoutées par l'extension, pas de supposer leur nom.

Consultez aussi le fichier `metadata.json` pour connaître l'identifiant et les versions de Shell déclarées compatibles.

## 4. Écrire une règle ciblée

Si l'extension ajoute une classe CSS documentée ou repérée dans son code, une règle peut être ajoutée dans la feuille Shell de G-OS.

Exemple fictif :

```css
.mon-extension-menu {
  background-color: #ffffff;
  color: #20242c;
  border-radius: 12px;
}
```

La classe `.mon-extension-menu` est un exemple et n'est pas fournie par G-OS. Remplacez-la par le nom réellement utilisé par l'extension.

Évitez les sélecteurs trop généraux comme `.popup-menu-content` si le but est de modifier une seule extension : un sélecteur général peut changer tous les menus du bureau.

## 5. Gérer les conflits de styles

Un style peut être surchargé par :
- une règle plus spécifique ;
- une règle chargée plus tard ;
- une feuille CSS privée de l'extension ;
- un style inline ou une classe d'état ajoutée dynamiquement ;
- un changement interne de l'extension après une mise à jour.

Ne multipliez pas les sélecteurs et les déclarations `!important` pour masquer le problème. Identifiez d'abord la règle gagnante et son origine.

## 6. Compatibilité entre versions

Une extension peut être compatible avec GNOME 51 tout en changeant sa structure interne au fil des versions. Une classe CSS privée n'est pas nécessairement une API stable.

Après une mise à jour :
1. Vérifiez la version de l'extension.
2. Vérifiez ses versions de Shell déclarées compatibles.
3. Comparez les noms de classes et les feuilles CSS.
4. Testez le menu ouvert, fermé, sélectionné et désactivé.
5. Vérifiez que les autres composants du bureau n'ont pas changé.

## 7. Activer et désactiver pour isoler un problème

```bash
gnome-extensions disable UUID
gnome-extensions enable UUID
```

Utilisez l'identifiant exact. Désactiver une extension permet de vérifier si elle est responsable d'un défaut graphique. Ne désactivez pas au hasard les extensions nécessaires au fonctionnement de la session.

## 8. Limites et bonnes pratiques pour G-OS

G-OS ne doit pas embarquer des correctifs CSS spécifiques à une extension sans raison claire. Une règle dédiée doit être documentée, testée sur la version ciblée et isolée dans un bloc identifiable.

Si une extension change souvent ses classes internes, privilégiez une configuration propre à l'extension ou signalez la limite plutôt que de rendre le thème dépendant d'une structure privée instable.

## 9. Checklist

- [ ] UUID et version de l'extension identifiés.
- [ ] Classe CSS vérifiée dans le code ou l'inspecteur.
- [ ] Règle limitée au composant voulu.
- [ ] Aucun effet de bord sur les menus natifs.
- [ ] Fonctionnement vérifié après redémarrage de session.
- [ ] Compatibilité GNOME 51 confirmée.

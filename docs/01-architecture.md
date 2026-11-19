# Présentation et architecture de G-OS Theme

## 1. Objectif visuel

G-OS Theme propose une identité cohérente inspirée des interfaces de bureau modernes : surfaces claires, contrastes doux, accent bleu, arrondis maîtrisés et hiérarchie typographique lisible. L'objectif n'est pas de transformer GNOME en un autre système, mais d'habiller les composants exposés par GNOME tout en conservant leurs comportements natifs.

Le thème comporte des variantes claires et sombres. Une apparence réussie doit rester lisible dans les deux modes, y compris pour les menus, les états désactivés, les sélections et les notifications.

## 2. Trois environnements distincts

### GNOME Shell

GNOME Shell dessine l'interface du bureau : barre supérieure, menus système, calendrier, notifications, vue des activités, dash, fenêtres de dialogue et plusieurs éléments de navigation.

Sa feuille de style utilise le moteur CSS de GNOME Shell et des noms de classes propres à ses composants. Ce n'est pas une feuille GTK générique. Les sélecteurs doivent être vérifiés dans la version ciblée du Shell.

Les fichiers de cette partie se trouvent dans `gnome-shell/`.

### GTK 3

GTK 3 fournit le style des applications encore basées sur cette version du toolkit. Son CSS possède des sélecteurs, propriétés et états spécifiques à GTK 3.

Les fichiers correspondants se trouvent dans `gtk-3.0/`. Les applications peuvent également charger leurs propres feuilles CSS ou utiliser des composants personnalisés ; un thème global ne peut donc pas garantir un rendu identique dans toutes les applications.

### GTK 4 et Libadwaita

GTK 4 utilise un moteur et des widgets différents de GTK 3. Libadwaita ajoute des conventions visuelles et des composants adaptatifs pour les applications GNOME modernes.

Les fichiers du dépôt dans `gtk-4.0/` ciblent les possibilités de personnalisation réellement exposées. Libadwaita peut imposer ses propres choix de style : une feuille CSS de thème ne peut pas remplacer toutes ses décisions internes.

## 3. Pourquoi séparer les feuilles de style

Une propriété ou un sélecteur peut être accepté par un moteur et ignoré par un autre. Mélanger toutes les règles dans un seul fichier rend le diagnostic difficile et augmente le risque de régression.

La séparation par moteur permet de répondre à trois questions :

1. Quel composant est stylé ?
2. Quel moteur interprète la règle ?
3. Dans quel fichier la correction doit-elle être effectuée ?

Avant d'ajouter une règle, identifiez le moteur du composant concerné. Ne copiez pas directement une règle trouvée dans un thème GTK vers GNOME Shell.

## 4. Ressources locales

Les images, textures et autres ressources du thème sont conservées dans `assets/`. Le thème ne doit pas dépendre d'une URL distante pour fonctionner.

Lorsqu'une ressource est ajoutée, vérifiez son format, sa licence, sa résolution et son contraste sur les deux variantes. Évitez d'ajouter une image si un style natif simple produit le même résultat.

## 5. Limites à connaître

Un thème agit sur l'apparence, pas sur le comportement fonctionnel des composants. Il ne remplace pas une extension GNOME et ne doit pas modifier les paramètres personnels de l'utilisateur sans son accord.

Certains éléments sont contrôlés par l'application, le toolkit, le compositeur ou le système. Si un composant ne réagit pas au thème, vérifiez d'abord s'il expose réellement un point de personnalisation.

## 6. Repérer les sources

Depuis la racine du dépôt :

```bash
find gnome-shell gtk-3.0 gtk-4.0 assets -maxdepth 3 -type f -print
```

Pour localiser les règles qui ciblent un composant :

```bash
grep -RInE 'selector|background|color|border' gnome-shell gtk-3.0 gtk-4.0
```

Remplacez les termes de recherche par le nom de classe ou la propriété que vous souhaitez comprendre. Une recherche textuelle indique où une règle est écrite ; elle ne prouve pas que le moteur l'applique.

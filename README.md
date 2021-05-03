# Tournoi de résolution de sudoku 2021

L'association CodeAnon organise un tournoi de résolution automatique de Sudoku cette année ! L'objectif de ce tournoi est de proposer un (ou plusieurs) programme(s) de résolution de Sudoku.
Tout le monde, membre ou non de l'association, est invité à participer !

## Déroulement du tournoi

Le tournoi se déroulera du **1er Mai 2021** au **1er Juin 2021** inclus. Dés le **2 juin** toutes les soumissions seront collectées et les résultats seront communiqués le soir. Les soumissions seront évaluées selon plusieurs critères :

1. **Performance**: la vitesse de votre programme sera évaluée sur plusieurs grilles de sudoku de différentes difficultés
2. **Originalité**: l'originalité de votre méthode de résolution sera également jugée, n'hésitez pas à innover !
3. **Qualité du code**: bien sûr, la qualité et la fiabilité du code sera également évaluée.

Un gagnant sera annoncé pour **chaque catégorie**. Les 3 gagnants se verront attribuer un badge spéciale sur notre **[serveur discord](https://codeanon.org/discord/)**


## Consignes de soumission

Vous devez fournir une archive contenant au moins un programme exécutable en respectant les consignes suivantes :
+ Le programme sera écrit dans **le langage de votre choix**
+ Le programme doit pouvoir s'exécuter sur un système UNIX (Ubuntu par exemple)
+ Le programme exécutable sera nommé `solver`
+ Si le programme est écrit dans un langage compilé, l'archive doit absolument contenir un fichier `Makefile` de sorte qu'en tapant la commande `make solver`, l'executable `solver` soit compilé
+ Si le programme est écrit dans un langage interprété, assurez vous que le programme soit exécutable simplement en tapant la commande `./solver`
+ Votre programme ne prendra aucun paramètres et se contentera de lire une grille de sudoku sur l'entrée standard UNIX (*stdin*) et d'écrire la grille complétée sur la sortie standard UNIX (*stdout*).

## Format des grilles

+ Les grilles de sudoku seront données sous la forme de 9 lignes de 9 entiers séparés par des espaces.
+ Chaque ligne est terminée par le symbole `\n` (y compris la **dernière**)
+ Les cases blanches dans une grille seront représentées par l'entier `0`

Votre programme devra fournir une unique réponse **complète** et **valide** qui respecte ce format

Voici un exemple de grille :

```
0 6 0 0 5 0 0 0 0
0 0 0 0 0 0 8 4 0
0 5 3 0 0 0 0 0 0
1 0 0 9 0 0 0 0 6
0 0 6 3 0 8 0 0 7
8 0 0 6 0 0 0 0 4
0 7 1 0 0 0 0 0 0
0 0 0 0 0 0 3 9 0
0 8 0 0 4 0 0 0 0
```

## Inscription et soumission

Pour participer au tournoi, vous devez avoir un compte **[github](https://github.com)** afin de pouvoir soumettre votre programme. Nous utilisons [**github classroom**](https://classroom.github.com) pour évaluer les soumissions.

L'inscription se fait à cette [**adresse**](https://classroom.github.com/a/4BaLyANK) ! après avoir cliqué sur le lien, un dépôt git à votre nom sera automatiquement créé et configuré pour vous permettre d'y placer votre code. Si vous avez besoin d'aide pour effectuer votre inscription, n'hésitez pas à nous contacter via [**discord**](https://codeanon.org/discord) ;).

A chaque fois que vous mettez à jour votre soumission, un test de conformité est effectué afin de vous indiquer si votre programme respecte les consignes ou non.

## Langages disponibles et environnement

Les tests de conformité ainsi que l'évaluation des soumissions sont fait sous la dernière version d'`ubuntu` avec les paquets suivants installés :

+ `ocaml`, `opam`
+ `rustc`, `cargo`
+ `python3.9`
+ `clang`, `gcc`

Si vous utilisez des outils non listés ci-dessus, merci de rajouter les instructions nécessaires à leur installation dans votre `Makefile`.

## Evaluation des soumissions

+ Vos soumissions seront évaluées uniquement sur des grilles de sudoku **valides** (qui admettent une solution).
+ Vos soumissions seront testées sur plusieurs grilles de difficultés variables
+ Si votre programme donne une réponse invalide pour l'une des grilles de test, celle-ci ne sera pas prise en compte. En revanche, cela n'affectera pas votre score sur les autres grilles de tests.


Pour toute question, n'hésitez pas à contacter le bureau de l'association via le **[serveur discord](https://codeanon.org/discord)**

Bonne chance à tous !

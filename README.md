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
+ Les cases blanches dans une grille seront représenté par le symbole `?`
  
Votre programme devra fournir une unique réponse **complète** et **valide** qui respecte ce format

Voici un exemple de grille :

```
? 6 ? ? 5 ? ? ? ?
? ? ? ? ? ? 8 4 ?
? 5 3 ? ? ? ? ? ?
1 ? ? 9 ? ? ? ? 6
? ? 6 3 ? 8 ? ? 7
8 ? ? 6 ? ? ? ? 4
? 7 1 ? ? ? ? ? ?
? ? ? ? ? ? 3 9 ?
? 8 ? ? 4 ? ? ? ?
```

## Vérifiez que votre soumission est correcte

Afin de vérifiez que votre soumission respecte les règles, vous pouvez suivre la procédure suivante :

1. clonez ce dépôt git (`git clone https://codeanonorg/Sudoku-tournament-2021.git`)
2. placez vous dans le répertoire (`cd ./Sudoku-tournament-2021.git`)
3. copiez-y les fichiers de votre soumissions
4. exécutez la commande `./test`

## Evaluation des soumissions

+ Vos soumissions seront évaluées uniquement sur des grilles de sudoku **valides** (qui admettent une solution).
+ Vos soumissions seront testées sur plusieurs grilles de difficultés variables
+ Si votre programme donne une réponse invalide pour l'une des grilles de test, celle-ci ne sera pas prise en compte. En revanche, cela n'affectera pas votre score sur les autres grilles de tests.

## Inscription

Le formulaire d'inscription se trouve à [cette adresse](https://forms.gle/dazkNZcMjmM6g4Ag9).
Pour toute question, n'hésitez pas à contacter le bureau de l'association via le **[serveur discord](https://codeanon.org/discord)**

Bonne chance à tous !



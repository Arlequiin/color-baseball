# Chapitre 13 : Algo
## Baseball des couleurs

Algo 1 : Algorithme tournant
```python
'''
Tant que le plateau n'est pas trié :
-> On choisit la base adjacente dans le sens horaire
-> On choisit de déplacer le pion le plus éloigné de sa base
---> En cas d'égalité, on choisit au hasard
'''
#L'inconvénient de cet algo c'est qu'il ne donne pas toujours la solution auquel cas il boucle à l'infini
```

Algo 2 : Version en liste
```python
#On numérote les bases de 1 à n
'''
On choisit la base 1
Tant que le plateau n'est pas trié :
-> On ramène tous les pions à la base choisie sans passer par un pion entre la dernière et la première base
-> On choisit la base suivante
'''
```
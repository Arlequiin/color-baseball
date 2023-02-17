http://www-verimag.imag.fr/~wack/baseball/
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
# Notes
```python
import time
print(time.time()) #Compteur lancé le 1er Janvier 1970 à minuit en secondes
```
# Activité 1

-  Recherche séquentielle

$
\text{Recherche-seq(liste,élément):}\\
\to \text{Pour tous les éléments dans la liste:}\\
\to \to \text{Si élément est trouvé:}\\
\to \to \to \text{Renvoyer vrai}\\
\to \text{Renvoyer faux}\\
$
- Pour une suite de taille n:
- - Meilleur des cas : 1 comparaison
- - Pire des cas : n comparaisons

```python
def recherche_seq(L,e):
    for i in L:
        if i==e:
            return True
    return False
```

- Recherche séquentielle triée
$
Recherche-seq-triée(liste,élément):\\
\to \text{Si l'élément recherché est compris entre le premier et le dernier élément de la liste:}\\
\to \to \text{Pour tous les éléments de la liste:}\\
\to \to \to \text{Si l'élément est trouvé:}\\
\to \to \to \to \text{Renvoyer Vrai}\\
\to \to \to \text{Sinon si l'élément de la liste est supérieur à l'élément recherché}\\
\to \to \to \to  \text{Renvoyer Faux}\\
\to \text{Sinon}\\
\to \to \text{Renvoyer Faux}\\
$

```python
#Tel que L une liste triée
def recherche_seq_triee(L,e):
    if L[0]<=e<=L[-1]:
        for i in L:
            if i==e:
                return True
            elif e<i:
                return False
    else:
        return False
```

- Meilleure des cas : 1 comparaison
- Pire des cas " L'élément recherché est le dernier de la liste, $2 \cdot n$ comparaisons

```python
def dicho(L,e):
    while len(L)>1:
        if e==L[len(L)//2]:
            return True
        elif e>L[len(L)//2]:
            L=L[len(L)//2:]
        else:
            L=L[:len(L)//2]
    if L[0]==e:
        return True
    else:
        return False

```

Dans une recherche sequentielle doubler la taille de la liste revient à doubler le nombre de vérification. Inversement en doublant la taille d'une liste avec la dichotomie seule une comparaison additionnelle est effectuée.

__<underline>Recherche sequentielle</underline>__<br>
Dans le pire cas, pour une liste de taille $n$, il y a n comparaisons. On dit que la __complexité__ de cet algorithme est d'ordre $n$ et on le note $O(n)$

__<underline>Recherche par dichotomie</underline>__<br>
Soit $x$ le nombre de divisions pour 2 successives pour obtenir une liste de taille $1$.<br>
Pour une liste de taille $n$, on obtient :
$$\frac{n}{2^x}=1$$

## Fonction logarithme

$$a = b \Leftrightarrow ln(a) = ln(b)$$
$$ln(a^b)=b \cdot ln(a)$$
$$\Leftrightarrow ln(n)=x ln(2)$$
$$x = \frac{ln(n)}{ln(2)}$$
$$\Leftrightarrow x = log_2(n)$$
Si $log_{10}$, on écrit simplement $log$
$$log_{10}(x)=\frac{ln(x)}{ln(3)}$$
$$log_3(x)=\frac{ln(x)}{ln(3)}$$
# Complexité



# Introduzione

NumPy è una libreria Python che permette di lavorare in modo efficiente con array multidimensionali e operazioni matematiche ad alte prestazioni. Per questo task è richiesto di implementare alcune funzioni utilizzando la libreria NumPy.

# Istruzioni

- Esegui il fork di questo progetto e assicurati che il tuo repository sia pubblico. Quindi, importa il progetto nel tuo IDE (es. PyCharm).
- Non puoi cambiare la firma delle funzioni fornite (nel file `task.py`) né rinominarle.
- Non puoi interagire con i tuoi colleghi: lavora individualmente e fai del tuo meglio.
- Le funzionalità da implementare sono descritte tramite un insieme di sub-task.
- Implementa le funzioni una alla volta, seguendo rigorosamente l’ordine fornito dai sub-task. Non leggere in anticipo le sub-task successive.
- Un sub-task può considerarsi completato quando sei sicuro che la funzionalità richiesta sia stata implementata correttamente.
- Ogni volta che completi un sub-task, esegui il commit e il push del codice.
- Al termine del compito, assicurati di aver eseguito il push di tutto il progetto sul repository.

# Sub-task

Ricordati di leggere e implementare i sub-task uno alla volta, seguendo l’ordine fornito. Non passare al sub-task successivo finché quello corrente non è stato completato. Implementa le funzionalità richieste lavorando nel file `task.py`.

---

## Sub-task 1 – Prodotto Scalare

Il prodotto scalare è un’operazione tra due vettori che restituisce un numero reale ottenuto sommando i prodotti delle componenti corrispondenti dei vettori.

### Requisito

Implementa la funzione:

```python
prodotto_scalare(v1: list, v2: list) -> float
````

Questa funzione riceve due liste di numeri e restituisce il prodotto scalare come float.

### Esempi

```python id="ps1"
Input: v1 = [1, 2, 3], v2 = [4, 5, 6]
Output: 32.0
```

```python id="ps2"
Input: v1 = [1, 0], v2 = [0, 1]
Output: 0.0
```

```python id="ps3"
Input: v1 = [-1, -2], v2 = [2, 3]
Output: -8.0
```

---

## Sub-task 2 – Rango di una matrice

Il rango di una matrice è un numero intero che rappresenta il massimo numero di righe (o colonne) linearmente indipendenti. In altre parole, indica la “dimensione informativa” della matrice, cioè quante righe contengono informazione non ridondante rispetto alle altre.

Il rango è una proprietà fondamentale dell’algebra lineare e viene utilizzato per determinare:

* la invertibilità di una matrice quadrata;
* la compatibilità di sistemi lineari;
* la presenza di dipendenze lineari tra righe o colonne.

---

### Requisito

Implementa la funzione:

```python id="rq1"
rango_matrice(m: list) -> int
```

La funzione riceve in input una matrice rappresentata come lista di liste e restituisce un intero.

Il risultato deve corrispondere al numero massimo di righe linearmente indipendenti presenti nella matrice.

---

### Esempi

```python id="rq2"
Input: m = [[1, 2],
            [3, 4]]

Output: 2
```

```python id="rq3"
Input: m = [[1, 2],
            [2, 4]]

Output: 1
```

```python id="rq4"
Input: m = [[2, 4, 1],
            [0, 0, 0],
            [1, 2, 0]]

Output: 2
```

---

## Sub-task 3 – Risolvere un Sistema Lineare

Un sistema di equazioni lineari del tipo `Ax = b` consiste in una matrice dei coefficienti `A`, un vettore dei termini noti `b` e un vettore incognito `x` di cui vogliamo calcolare i valori.

### Requisito

Implementa la funzione:

```python
risolvi_sistema_lineare(A: list, b: list) -> np.ndarray
```

Questa funzione riceve la matrice quadrata dei coefficienti `A` (come lista di liste) e il vettore dei termini noti `b` (come lista), e restituisce il vettore soluzione `x` come array NumPy.

### Esempi

```python id="rsl1"
Input: A = [[2, 1], [1, 3]], b = [5, 7]
Output: array([1.6, 1.8])
```

```python id="rsl2"
Input: A = [[1, 0], [0, 1]], b = [3, 4]
Output: array([3., 4.])
```

```python id="rsl3"
Input: A = [[3, 1], [1, 2]], b = [9, 8]
Output: array([2., 3.])
```

---

## Sub-task 4 – Correlazione tra Matrici 2x2

La correlazione statistica (nello specifico, il coefficiente di Pearson) misura il grado di dipendenza lineare tra due insiemi di dati.

Quando abbiamo due matrici di dimensione identica (come due matrici 2x2), possiamo valutarne la correlazione appiattendo i loro valori (flattening) e trattandoli come due array lineari.

### Requisito

Implementa la funzione:

```python
correlazione_matrici(m1: list, m2: list) -> np.ndarray
```

Questa funzione riceve due matrici 2x2 (sotto forma di liste di liste) e restituisce la matrice di correlazione calcolata tra i valori “appiattiti” (sequenziali) delle due matrici.

### Esempi

```python id="cm1"
Input: m1 = [[1, 2], [3, 4]], m2 = [[2, 4], [6, 8]]
Output: [[1. 1.]
 [1. 1.]]
```

```python id="cm2"
Input: m1 = [[1, 2], [3, 4]], m2 = [[4, 3], [2, 1]]
Output: [[ 1. -1.]
 [-1.  1.]]
```
---

## Sub-task 5 – Operazioni Elemento per Elemento

Le operazioni elemento per elemento (element-wise) sono operazioni in cui una funzione viene applicata separatamente a ciascun elemento di una struttura dati (come un array o una matrice), producendo un risultato della stessa forma.
Le operazioni elemento per elemento si basano quindi sulle funzioni vettoriali di NumPy, che applicano automaticamente le operazioni in modalità element-wise su tutti gli elementi degli array.

### Requisito

Implementa la funzione:

```python
operazioni_elemento_per_elemento(v1: list) -> tuple
```

La funzione riceve in input una lista di numeri e, utilizzando le specifiche funzioni vettoriali di NumPy, deve calcolare:

* seno elemento per elemento;
* coseno elemento per elemento;
* arcoseno elemento per elemento;
* arcocoseno elemento per elemento;

e restituire una tupla contenente i quattro array risultanti.

Ogni operazione deve essere svolta usando le funzioni vettoriali di NumPy che operano in modalità element-wise, in modo da ottenere risultati della stessa forma degli input.

### Esempi

```python id="oe5_1"
Input: v1 = [0, 0.5, 1, -0.5]
Output: (
    array([0.        , 0.47942554, 0.84147098, -0.47942554]),
    array([1.        , 0.87758256, 0.54030231, 0.87758256]),
    array([0.        , 0.52359878, 1.57079633, -0.52359878]),
    array([1.57079633, 1.04719755, 0.        , 2.0943951 ])
)
```

```python id="oe5_2"
Input: v1 = [0.2, -0.8, 1.0]
Output: (
    array([ 0.19866933, -0.71735609, 0.84147098]),
    array([ 0.98006658, 0.69670671, 0.54030231]),
    array([0.20135792, -0.92729522, 1.57079633]),
    array([1.36943841, 2.49809154, 0.        ])
)
```


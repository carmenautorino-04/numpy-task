import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    """Sub-task 1: Prodotto Scalare."""
    pass
from typing import List


def prodotto_scalare(v1: List[float], v2: List[float]) -> float:
    """
    Calcola il prodotto scalare tra due vettori numerici.

    :param v1: prima lista di numeri
    :param v2: seconda lista di numeri
    :return: prodotto scalare (float)

    :raises TypeError: se gli input non sono liste o contengono elementi non numerici
    :raises ValueError: se le liste hanno lunghezze diverse o sono vuote
    """

    # Controllo tipo liste
    if not isinstance(v1, list) or not isinstance(v2, list):
        raise TypeError("Entrambi gli input devono essere liste.")

    # Controllo liste vuote
    if len(v1) == 0 or len(v2) == 0:
        raise ValueError("Le liste non possono essere vuote.")

    # Controllo lunghezza
    if len(v1) != len(v2):
        raise ValueError("Le liste devono avere la stessa lunghezza.")

    # Controllo elementi numerici
    for i, (a, b) in enumerate(zip(v1, v2)):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Gli elementi in posizione {i} non sono numerici.")

    # Calcolo prodotto scalare
    prodotto = sum(a * b for a, b in zip(v1, v2))

    return float(prodotto)




def rango_matrice(m: list) -> int:
    """Sub-task 2: Calcola il rango di una matrice."""
    pass
def rango_matrice(m: list) -> int:
    """
    Calcola il rango di una matrice (numero massimo di righe linearmente indipendenti).

    :param m: matrice rappresentata come lista di liste
    :return: rango (int)

    :raises TypeError: se la struttura o gli elementi non sono validi
    :raises ValueError: se la matrice è vuota o irregolare
    """

    # --- Controlli di validità ---
    if not isinstance(m, list) or not m:
        raise ValueError("La matrice deve essere una lista non vuota di liste.")

    if not all(isinstance(riga, list) for riga in m):
        raise TypeError("La matrice deve essere una lista di liste.")

    n_col = len(m[0])
    if n_col == 0:
        raise ValueError("Le righe non possono essere vuote.")

    if not all(len(riga) == n_col for riga in m):
        raise ValueError("Tutte le righe devono avere la stessa lunghezza.")

    for i, riga in enumerate(m):
        for j, val in enumerate(riga):
            if not isinstance(val, (int, float)):
                raise TypeError(f"Elemento non numerico in posizione ({i},{j})")

    # --- Copia della matrice in float ---
    A = [list(map(float, riga)) for riga in m]

    righe = len(A)
    colonne = n_col
    rango = 0
    EPS = 1e-10  # tolleranza per confronti con zero

    r = 0  # riga corrente

    for c in range(colonne):
        # Trova pivot
        pivot = None
        for i in range(r, righe):
            if abs(A[i][c]) > EPS:
                pivot = i
                break

        if pivot is None:
            continue

        # Scambia righe
        A[r], A[pivot] = A[pivot], A[r]

        # Normalizza la riga pivot (opzionale ma utile)
        pivot_val = A[r][c]
        A[r] = [x / pivot_val for x in A[r]]

        # Elimina sotto
        for i in range(r + 1, righe):
            fattore = A[i][c]
            A[i] = [A[i][j] - fattore * A[r][j] for j in range(colonne)]

        rango += 1
        r += 1

        if r == righe:
            break

    return rango
def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    """Sub-task 3: Risolvere un Sistema Lineare."""
    pass
def risolvi_sistema_lineare(A: list, b: list) -> list:
    """
    Risolve il sistema lineare Ax = b usando l'eliminazione di Gauss.

    :param A: matrice quadrata (lista di liste)
    :param b: vettore termini noti (lista)
    :return: soluzione x (lista di float)

    :raises TypeError: input non validi
    :raises ValueError: sistema non risolvibile o dati inconsistent
    """

    # --- Controlli ---
    if not isinstance(A, list) or not A:
        raise ValueError("A deve essere una lista di liste non vuota.")
    if not all(isinstance(r, list) for r in A):
        raise TypeError("A deve essere una lista di liste.")

    n = len(A)
    if not all(len(r) == n for r in A):
        raise ValueError("A deve essere quadrata.")

    if not isinstance(b, list) or len(b) != n:
        raise ValueError("b deve essere una lista lunga quanto A.")

    for i in range(n):
        for j in range(n):
            if not isinstance(A[i][j], (int, float)):
                raise TypeError(f"A[{i}][{j}] non numerico.")
        if not isinstance(b[i], (int, float)):
            raise TypeError(f"b[{i}] non numerico.")

    # --- Copia in float ---
    A = [[float(x) for x in r] for r in A]
    b = [float(x) for x in b]

    # --- Eliminazione di Gauss ---
    for i in range(n):
        # Pivot (gestione pivot nullo)
        if abs(A[i][i]) < 1e-12:
            for k in range(i + 1, n):
                if abs(A[k][i]) > 1e-12:
                    A[i], A[k] = A[k], A[i]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                raise ValueError("Sistema non ha soluzione unica (pivot nullo).")

        # Normalizzazione riga
        pivot = A[i][i]
        A[i] = [x / pivot for x in A[i]]
        b[i] /= pivot

        # Eliminazione sotto
        for k in range(i + 1, n):
            fattore = A[k][i]
            A[k] = [A[k][j] - fattore * A[i][j] for j in range(n)]
            b[k] -= fattore * b[i]

    # --- Sostituzione all'indietro ---
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))

    return x



def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""






def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """
    Calcola la matrice di correlazione tra due matrici 2x2,
    considerando i valori appiattiti come due variabili.

    :param m1: prima matrice 2x2 (lista di liste)
    :param m2: seconda matrice 2x2 (lista di liste)
    :return: matrice di correlazione 2x2 (np.ndarray)

    :raises TypeError, ValueError: in caso di input non validi
    """

    # --- Controlli ---
    def valida(m, nome):
        if not isinstance(m, list) or len(m) != 2:
            raise ValueError(f"{nome} deve essere una matrice 2x2.")
        for i, r in enumerate(m):
            if not isinstance(r, list) or len(r) != 2:
                raise ValueError(f"{nome} deve essere una matrice 2x2.")
            for j, val in enumerate(r):
                if not isinstance(val, (int, float)):
                    raise TypeError(f"{nome}[{i}][{j}] non è numerico.")

    valida(m1, "m1")
    valida(m2, "m2")

    # --- Appiattimento ---
    v1 = np.array([m1[0][0], m1[0][1], m1[1][0], m1[1][1]], dtype=float)
    v2 = np.array([m2[0][0], m2[0][1], m2[1][0], m2[1][1]], dtype=float)

    # --- Controllo varianza ---
    if np.allclose(np.var(v1), 0) or np.allclose(np.var(v2), 0):
        raise ValueError("Varianza nulla: correlazione non definita.")

    # --- Matrice dati (2 variabili, 4 osservazioni) ---
    data = np.vstack((v1, v2))

    # --- Matrice di correlazione ---
    corr_matrix = np.corrcoef(data)

    return corr_matrix

    pass
def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    pass

import numpy as np


def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """
    Calcola seno, coseno, arcoseno e arcocoseno elemento per elemento.

    :param v1: lista di numeri
    :return: tupla (sin, cos, arcsin, arccos) come np.ndarray

    :raises TypeError, ValueError: in caso di input non validi
    """

    # --- Controlli ---
    if not isinstance(v1, list) or not v1:
        raise ValueError("L'input deve essere una lista non vuota.")


def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()

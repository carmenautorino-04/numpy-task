#import numpy as np

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

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""
    pass

def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    pass


def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()

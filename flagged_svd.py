import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':
    # domain
    nnu = 1024
    nu = np.linspace(-np.pi, np.pi, nnu)
    nt = 128
    t = np.linspace(0, 25, nt)

    # low rank function (a single fringe)
    x = np.exp(1.0j*(nu[:, None] + t[None, :]))

    V, L, U = np.linalg.svd(x)

    # choose 10% random flags
    nflagged = int(0.1*nnu*nt)
    Inu = np.random.randint(0, nnu, nflagged)
    It = np.random.randint(0, nt, nflagged)
    xflagged1 = x.copy()
    xflagged1[Inu, It] = 0j
    V1, L1, U1 = np.linalg.svd(xflagged1)

    # flag entire time and freq slots
    xflagged2 = x.copy()
    xflagged2[:, 25] = 0j
    xflagged2[:, 45] = 0j
    xflagged2[512, :] = 0j
    V2, L2, U2 = np.linalg.svd(xflagged2)

    print('Rank of unflagged matrix = ', np.linalg.matrix_rank(x))
    print('Rank of randomly flagged matrix = ', np.linalg.matrix_rank(xflagged1))
    print('Rank of uniformly flagged matrix = ', np.linalg.matrix_rank(xflagged2))

    plt.figure()
    plt.plot(L, 'xr', label='orig')
    plt.plot(L1, '+k', label='random')
    plt.plot(L2, '*b', label='uniform')
    plt.legend()

    plt.show()


import matplotlib.pyplot as plt
import numpy as np


def render(otaular = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
           tuzdyq = [-1, -1],
           qazandar = [0, 0]):
    fig = plt.figure(figsize=(15, 4))

    points_bastaushy_x = np.array([i * 2 for i in range(10)])
    points_bastaushy_y = np.array([i % 5 for i in range(50)])

    x = np.arange(-3, 225, 1)
    y = -1

    text_kwargs = dict(ha='center', va='center', fontsize=12)

    for i in range(9):
        # qostaushy's part
        plt.scatter(np.repeat(points_bastaushy_x + 25 * i, 5)[:otaular[17 - i]],
                    points_bastaushy_y[:otaular[17 - i]], marker='o')
        # horizontal line
        plt.plot(x, np.repeat(y, len(x)))
        # vertical lines
        plt.plot(np.repeat(25 * i - 2, len(x)), np.arange(-7, 5, 12 / len(x)))
        # bastaushy's part
        plt.scatter(np.repeat(points_bastaushy_x + 25 * i, 5)[:otaular[i]],
                    points_bastaushy_y[:otaular[i]] - 6, marker='o')

    # last vertical line
    plt.plot(np.repeat(25 * 9 - 2, len(x)), np.arange(-7, 5, 12 / len(x)))

    for i in range(9):
        # bastaushy's qumalaqtar
        plt.text(25 * i + 10, -7, f'{i} ({otaular[i]})', **text_kwargs)
        # qostaushy's qumalaqtar
        plt.text(25 * i + 10, 5, f'{17 - i} ({otaular[17 - i]})', **text_kwargs)
    # bastaushy qazan's qumalaqtar
    plt.text(230, -4, f'qazan: {qazandar[0]}', **text_kwargs)
    # qostaushy qazan's qumalaqtar
    plt.text(230, 2, f'qazan: {qazandar[1]}', **text_kwargs);
    # bastaushy tuzdyq's qumalaqtar
    plt.text(230, -6, f'tuzdyq: {tuzdyq[0]}', **text_kwargs)
    # qostaushy tuzdyq's qumalaqtar
    plt.text(230, 0, f'tuzdyq: {tuzdyq[1]}', **text_kwargs);
    return fig
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')


def main() -> None:
    X = np.array([0.4154, 0.2474, 0.1474, 0.0878, 0.0523, 0.0311, 0.01826])

    width = 0.1

    fig, ax = plt.subplots(constrained_layout=True)
    x = np.arange(len(X))
    ax._res = ax.bar(x, height=X)
    for rect in ax._res:
        height = rect.get_height()
        ax.annotate(
            '{}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(rect.get_x() + rect.get_width() / 2, height + 0.005),
            ha='center',
            va='bottom',
        )

    ax.set(
        xticks=x,
        xticklabels=np.arange(7.5, 9.25, 0.25),
        yticks=np.arange(0, 0.5, 0.05),
        title='$P(M)$',
        xlabel='$M$ - Moment magnitude',
        ylabel='$P(M = m)$',
    )

    fig.savefig('plot_d.png')
    fig.savefig('plot_d.svg')


if __name__ == '__main__':
    main()

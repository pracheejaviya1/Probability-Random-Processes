#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf


def ievsig() -> None:
    df = pd.read_csv('plot_final.csv')
    df['Incident energy'] /= 10e6
    df['sigma'] *= 10e3
    fig, ax = plt.subplots()
    ax.plot(df['Incident energy'], df['sigma'])
    ax.grid(True)
    ax.set(xlabel='$\sigma$', ylabel='Incident energy')
    fig.savefig('ievsigma.png')


def bwd() -> None:
    df = pd.read_csv('plot_final.csv')
    df['Incident energy'] /= 10e6
    df['sigma'] *= 10e3
    k = 4.9765e-3
    gamma = 9.2475e5
    E_r = 6.4e5
    E = tf.constant(np.arange(2 * 10e6))
    sigma = (k * gamma**2) / ((E - E_r)**2 + (gamma / 2)**2)
    fig, ax = plt.subplots()
    ax.plot(E / 10e6, sigma * 10e3, label='BWD')
    ax.plot(df['Incident energy'], df['sigma'], label='1R')
    ax.grid(True)
    ax.legend(loc='upper right')
    ax.set(xlabel='E',
           ylabel='$\sigma$',
           title='Breit-Wigner Distribution',
           xlim=(-0.1, 1.1),
           xticks=np.arange(-0.1, 1.2, 0.1))
    fig.savefig('bwd.png')
    fig.savefig('bwd.svg')


if __name__ == '__main__':
    bwd()

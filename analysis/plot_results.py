"""
Generate figures for "Quantum Algorithms Do Not Need Classical Control."

Usage:
    pip install matplotlib numpy
    python plot_results.py
"""

import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_data():
    """Load and merge N=1..17 and N=18..23 datasets."""
    with open(DATA_DIR / "ibm_n1_to_n17.json") as f:
        d1 = json.load(f)
    with open(DATA_DIR / "ibm_n18_to_n23.json") as f:
        d2 = json.load(f)
    d1.update(d2)
    return d1

def plot_main_results(data):
    """Figure 2: Fidelity vs N for dynamic and pure unitary."""
    ns = sorted(data.keys(), key=int)
    N = [int(n) for n in ns]
    p_dyn = [data[n]["p_dynamic"] * 100 for n in ns]
    p_unit = [data[n]["p_groverize"] * 100 for n in ns]

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(N, p_dyn, "o-", color="#d62728", label="Dynamic (mid-circuit measurement)", linewidth=2, markersize=6)
    ax.plot(N, p_unit, "s-", color="#1f77b4", label="Pure unitary (CNOT)", linewidth=2, markersize=6)
    ax.axhline(y=100/2**1, color="gray", linestyle="--", alpha=0.4, label="Random guess (1/2)")
    ax.set_xlabel("N (conditional operations)", fontsize=13)
    ax.set_ylabel("P(ideal outcome) [%]", fontsize=13)
    ax.set_title("Pure Unitary vs Dynamic: IBM ibm_marrakesh", fontsize=14)
    ax.legend(fontsize=11)
    ax.set_ylim(-2, 102)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(DATA_DIR.parent / "figure2_main_results.png", dpi=300)
    print("Saved figure2_main_results.png")
    return fig

def plot_relative_advantage(data):
    """Supplementary: Relative advantage vs N."""
    ns = sorted(data.keys(), key=int)
    N = [int(n) for n in ns]
    rel = [data[n]["relative"] for n in ns]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(N, rel, color="#2ca02c", alpha=0.8)
    ax.set_xlabel("N (conditional operations)", fontsize=13)
    ax.set_ylabel("Relative advantage (unitary / dynamic)", fontsize=13)
    ax.set_title("Fidelity Advantage by N", fontsize=14)
    ax.axhline(y=1, color="red", linestyle="--", alpha=0.5, label="Break-even")
    ax.legend()
    ax.grid(True, alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(DATA_DIR.parent / "figure_relative_advantage.png", dpi=300)
    print("Saved figure_relative_advantage.png")
    return fig

def print_table(data):
    """Print LaTeX table for the paper."""
    ns = sorted(data.keys(), key=int)
    print("\n% LaTeX table")
    print("\\begin{tabular}{@{}rrrrr@{}}")
    print("\\toprule")
    print("$N$ & Dynamic & Pure Unitary & Advantage & Relative \\\\")
    print("\\midrule")
    for n in ns:
        d = data[n]
        print(f"{int(n):>2} & {d['p_dynamic']*100:.1f}\\% & {d['p_groverize']*100:.1f}\\% "
              f"& {d['abs_diff']*100:+.1f}\\% & {d['relative']:.2f}$\\times$ \\\\")
    print("\\bottomrule")
    print("\\end{tabular}")

if __name__ == "__main__":
    data = load_data()
    plot_main_results(data)
    plot_relative_advantage(data)
    print_table(data)
    plt.show()

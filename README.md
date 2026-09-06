# Static Unitary Compilation Outperforms Dynamic Feedback on NISQ Hardware

Experimental data, analysis scripts, and figures for the paper "Static Unitary Compilation Outperforms Dynamic Feedback on NISQ Hardware: A Physics-Based Roadmap."

## Contents

### Data
- `data/ibm_n1_to_n17.json` — Results for N=1 to N=17 conditional operations on IBM ibm_marrakesh (156-qubit Heron).
- `data/ibm_n18_to_n23.json` — Extended results for N=18 to N=23.
- `data/ibm_n25_to_n31.json` — Extended results for N=25 to N=31 (dynamic yields zero counts by N=25).

### Analysis
- `analysis/plot_results.py` — Reproduce main figures from paper data.
- `analysis/plot_fig1_compilation.py` — Figure 1: Compilation framework diagram.
- `analysis/plot_fig2_depth.py` — Figure 2: Executable depth projection.
- `analysis/plot_fig3_scaling.py` — Figure 3: Main scaling results (semi-log).
- `analysis/plot_fig4_noise.py` — Figure 4: Noise budget comparison.
- `analysis/plot_threshold.py` — Decision threshold scaling with gate fidelity.

### Figures
- `figures/` — Publication-quality figures (PDF and PNG).

### LaTeX Source
- `main.tex` — Full paper source.

## Data Format

Each JSON file is a dictionary keyed by N (number of conditional operations). Each entry contains:

| Field | Description |
|-------|-------------|
| `p_dynamic` | Probability of ideal outcome for dynamic circuit |
| `p_groverize` | Probability of ideal outcome for pure unitary circuit |
| `abs_diff` | Absolute fidelity difference |
| `relative` | Relative fidelity advantage (pure unitary / dynamic) |
| `dyn_depth` | Dynamic circuit depth |
| `grov_depth` | Pure unitary circuit depth |
| `phys_qubits` | Physical qubit indices used |
| `dyn_counts` | Raw measurement counts (dynamic) |
| `grov_counts` | Raw measurement counts (pure unitary) |

## Experimental Setup

- **Hardware**: IBM ibm_marrakesh, 156-qubit Heron processor
- **Qubit layout**: Fixed connected chain [0, 1, 2, ..., 15, 19, 35]
- **Dynamical decoupling**: OFF
- **Twirling (gates and measurement)**: OFF
- **Shots**: 4000 per circuit
- **Batch submission**: all N values in a single job to minimize calibration drift

## Reproducing Figures

```bash
pip install matplotlib numpy
python analysis/plot_results.py
```

## Citation

```bibtex
@article{lee2026unitary,
  title={Static Unitary Compilation Outperforms Dynamic Feedback on NISQ Hardware: A Physics-Based Roadmap},
  author={Lee, Lap-Yuen},
  journal={[Journal TBD]},
  year={2026}
}
```

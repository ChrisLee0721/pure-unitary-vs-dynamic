# Quantum Algorithms Do Not Need Classical Control

Experimental data and analysis for the paper "Quantum Algorithms Do Not Need Classical Control."

## Contents

- `data/ibm_n1_to_n17.json` — Results for N=1 to N=17 conditional operations on IBM ibm_marrakesh (156-qubit Heron).
- `data/ibm_n18_to_n23.json` — Extended results for N=18 to N=23.
- `analysis/plot_results.py` — Python script to reproduce all figures.

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
  title={Quantum Algorithms Do Not Need Classical Control},
  author={[Authors TBD]},
  journal={[Journal TBD]},
  year={2026}
}
```

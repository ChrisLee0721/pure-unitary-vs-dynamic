"""Generate Figure 1 (fig:scaling) for the paper: fidelity vs N."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Data from Table 2 (N=1-17) + Table 3 (N=18-31)
N_all = [1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 25, 27, 29, 31]
dynamic_all = [92.4, 80.3, 62.5, 49.3, 34.6, 18.0, 11.4, 6.8, 4.1, 2.5, 2.1, 1.3, 1.1, 0.6, 0.4, None, None, None, None]
unitary_all = [96.9, 93.5, 85.0, 79.4, 70.4, 62.6, 46.0, 42.1, 38.9, 33.2, 30.4, 29.0, 24.5, 18.1, 17.3, 4.9, 2.4, 0.88, 0.90]

# Theoretical curves
N_theory = np.linspace(0.5, 32, 200)
F_dyn_theory = 0.83 ** N_theory * 100
F_uni_theory = 0.995 ** N_theory * 100

# Split data for plotting (dynamic stops at N=23)
N_dyn = [n for n, d in zip(N_all, dynamic_all) if d is not None]
dyn_vals = [d for d in dynamic_all if d is not None]

fig, ax = plt.subplots(figsize=(7, 5))

# Theoretical curves (dashed, behind)
ax.plot(N_theory, F_dyn_theory, '--', color='#d62728', alpha=0.4, linewidth=1.5,
        label=r'${\rm Dynamic:}~0.83^N$')
ax.plot(N_theory, F_uni_theory, '--', color='#1f77b4', alpha=0.4, linewidth=1.5,
        label=r'${\rm Pure~unitary:}~0.995^N$')

# Data points with error bars (from Wilson score, approx ±2% for large N, smaller for small N)
# Using 95% CI approximation: ±1.96*sqrt(p(1-p)/n) with n=4000
def ci95(p_pct):
    p = p_pct / 100
    return 1.96 * np.sqrt(p * (1 - p) / 4000) * 100

dyn_err = [ci95(d) for d in dyn_vals]
uni_err = [ci95(u) for u in unitary_all]

ax.errorbar(N_dyn, dyn_vals, yerr=dyn_err, fmt='o-', color='#d62728', markersize=5,
            linewidth=1.8, capsize=3, label='Dynamic (experiment)')
ax.errorbar(N_all, unitary_all, yerr=uni_err, fmt='s-', color='#1f77b4', markersize=5,
            linewidth=1.8, capsize=3, label='Pure unitary (experiment)')

# Annotate key points
ax.annotate('9.49×', xy=(17, 38.9), xytext=(19, 55),
            arrowprops=dict(arrowstyle='->', color='black', lw=0.8),
            fontsize=9, ha='center')
ax.annotate('43×', xy=(23, 17.3), xytext=(25.5, 30),
            arrowprops=dict(arrowstyle='->', color='black', lw=0.8),
            fontsize=9, ha='center')

# 10% threshold line
ax.axhline(y=10, color='gray', linestyle=':', alpha=0.6, linewidth=1)
ax.text(0.5, 10.5, '10% threshold', fontsize=8, color='gray', va='bottom')

ax.set_xlabel(r'Number of conditional operations ($N$)', fontsize=12)
ax.set_ylabel('Probability of ideal outcome (%)', fontsize=12)
ax.set_yscale('log')
ax.set_ylim(0.2, 110)
ax.set_xlim(-0.5, 32.5)
ax.legend(fontsize=9, loc='upper right')
ax.grid(True, alpha=0.3, which='both')
ax.set_title('Figure 1: Scaling of fidelity with conditional operations', fontsize=11, pad=10)

plt.tight_layout()
plt.savefig(r'F:\PyQQQ\paper\fig_scaling.pdf', dpi=300, bbox_inches='tight')
plt.savefig(r'F:\PyQQQ\paper\fig_scaling.png', dpi=300, bbox_inches='tight')
print("Saved fig_scaling.pdf and fig_scaling.png")

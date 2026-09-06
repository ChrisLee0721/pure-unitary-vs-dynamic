"""Figure 3: Main experimental results — semi-log scaling curve.
Fidelity vs N for dynamic and pure unitary, with theoretical curves and annotations.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7, 5))

# === Data ===
# Table 2: N=1-17
N_main = [1, 3, 5, 7, 9, 11, 13, 15, 17]
dyn_main = [92.4, 80.3, 62.5, 49.3, 34.6, 18.0, 11.4, 6.8, 4.1]
uni_main = [96.9, 93.5, 85.0, 79.4, 70.4, 62.6, 46.0, 42.1, 38.9]

# Table 3: N=18-31
N_ext = [18, 19, 20, 21, 22, 23, 25, 27, 29, 31]
dyn_ext = [2.5, 2.1, 1.3, 1.1, 0.6, 0.4, None, None, None, None]
uni_ext = [33.2, 30.4, 29.0, 24.5, 18.1, 17.3, 4.9, 2.4, 0.88, 0.90]

# Combine
N_all = N_main + N_ext
dyn_all = dyn_main + dyn_ext
uni_all = uni_main + uni_ext

# Separate dynamic data (stops at N=23)
N_dyn = [n for n, d in zip(N_all, dyn_all) if d is not None]
dyn_vals = [d for d in dyn_all if d is not None]

# === Theoretical curves ===
N_theory = np.linspace(0.5, 32, 300)
F_dyn_th = 0.83 ** N_theory * 100
F_uni_th = 0.995 ** N_theory * 100

# === Plot ===
# Theoretical (dashed, behind)
ax.plot(N_theory, F_dyn_th, '--', color='#d62728', alpha=0.35, linewidth=1.8,
        label=r'$F^{\mathrm{dyn}} = 0.83^N$ (model)')
ax.plot(N_theory, F_uni_th, '--', color='#1f77b4', alpha=0.35, linewidth=1.8,
        label=r'$F^{\mathrm{uni}} = 0.995^N$ (model)')

# Error bars: Wilson score intervals are asymmetric, especially at low rates.
def ci95_wilson(p_pct, shots=4000, z=1.96):
        p = p_pct / 100
        denominator = 1 + z**2 / shots
        center = (p + z**2 / (2 * shots)) / denominator
        half_width = (z / denominator) * np.sqrt(
                p * (1 - p) / shots + z**2 / (4 * shots**2)
        )
        lower = np.maximum(0, center - half_width) * 100
        upper = np.minimum(1, center + half_width) * 100
        return lower, upper

dyn_intervals = [ci95_wilson(d) for d in dyn_vals]
uni_intervals = [ci95_wilson(u) for u in uni_all]
dyn_err = np.array([
        [value - interval[0] for value, interval in zip(dyn_vals, dyn_intervals)],
        [interval[1] - value for value, interval in zip(dyn_vals, dyn_intervals)],
])
uni_err = np.array([
        [value - interval[0] for value, interval in zip(uni_all, uni_intervals)],
        [interval[1] - value for value, interval in zip(uni_all, uni_intervals)],
])

# Data points
ax.errorbar(N_dyn, dyn_vals, yerr=dyn_err, fmt='o', color='#d62728', markersize=6,
            linewidth=0, capsize=3, capthick=1.2, elinewidth=1.2,
            markeredgecolor='white', markeredgewidth=0.8,
            label='Dynamic (IBM ibm_marrakesh)', zorder=5)
ax.errorbar(N_all, uni_all, yerr=uni_err, fmt='s', color='#1f77b4', markersize=5.5,
            linewidth=0, capsize=3, capthick=1.2, elinewidth=1.2,
            markeredgecolor='white', markeredgewidth=0.8,
            label='Pure unitary (IBM ibm_marrakesh)', zorder=5)

# Connecting lines for data points (thin)
ax.plot(N_dyn, dyn_vals, '-', color='#d62728', linewidth=1, alpha=0.5, zorder=4)
ax.plot(N_all, uni_all, '-', color='#1f77b4', linewidth=1, alpha=0.5, zorder=4)

# === Key annotations ===
# 9.49x at N=17
ax.annotate('', xy=(17, 6.0), xytext=(17, 28.0),
            arrowprops=dict(arrowstyle='<->', color='#333', lw=1.5))
ax.text(17.8, 14, '9.5x', fontsize=10, ha='left', va='center', fontweight='bold', color='#333')

# 43x at N=23
ax.annotate('', xy=(23, 0.7), xytext=(23, 12.0),
            arrowprops=dict(arrowstyle='<->', color='#333', lw=1.5))
ax.text(23.8, 3.2, '43x', fontsize=10, ha='left', va='center', fontweight='bold', color='#333')

# 10% threshold
ax.axhline(y=10, color='gray', linestyle=':', alpha=0.5, linewidth=1)
ax.text(0.7, 10.8, '10% executable depth threshold', fontsize=8, color='gray', va='bottom')

# Dynamic dead zone
ax.axhspan(0, 1, alpha=0.06, color='red')
ax.text(5.5, 0.42, 'Dead zone (<1%)', fontsize=8, ha='center',
        va='bottom', color='#d62728', alpha=0.75)

# === Formatting ===
ax.set_xlabel(r'Number of conditional operations ($N$)', fontsize=12)
ax.set_ylabel('Probability of ideal outcome (%)', fontsize=12)
ax.set_yscale('log')
ax.set_ylim(0.15, 120)
ax.set_xlim(-0.5, 33)
ax.legend(fontsize=7.8, loc='upper right', framealpha=0.9, ncol=1)
ax.grid(True, alpha=0.25, which='major')
ax.grid(True, alpha=0.1, which='minor')
ax.set_title('Experimental comparison: dynamic vs pure unitary circuits', fontsize=11, pad=10)

plt.tight_layout()
plt.savefig(r'F:\PyQQQ\paper\fig3_scaling.pdf', dpi=300, bbox_inches='tight')
plt.savefig(r'F:\PyQQQ\paper\fig3_scaling.png', dpi=300, bbox_inches='tight')
print("Saved fig3_scaling")

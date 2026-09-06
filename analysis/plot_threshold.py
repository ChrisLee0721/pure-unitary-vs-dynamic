"""Generate threshold scaling figure: decision boundary vs gate fidelity."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Fixed measurement parameters (IBM Heron)
F_meas = 0.99
Tfb_over_T2 = 34 / 200  # T_fb / T_2

# Measurement tax
T = F_meas * np.exp(-Tfb_over_T2)
ln_T = np.log(T)  # negative

# Gate fidelity range
F_gate = np.logspace(np.log10(0.99), np.log10(1 - 1e-7), 500)
F_gate = F_gate[F_gate < 1]  # exclude exactly 1
ln_Fg = np.log(F_gate)  # all negative

# Threshold = |ln T| / |ln F_gate|
threshold = np.abs(ln_T) / np.abs(ln_Fg)

fig, ax = plt.subplots(figsize=(6, 4))

# Shade unitary-favored region
ax.fill_between(F_gate, 0, threshold, alpha=0.15, color='#2ca02c', label='Unitary favored')
ax.plot(F_gate, threshold, color='#2ca02c', linewidth=2)

# Reference lines
ax.axvline(0.995, color='#d62728', linestyle='--', linewidth=1, alpha=0.7, label='Current Heron (99.5%)')
ax.axvline(0.9999, color='#1f77b4', linestyle='--', linewidth=1, alpha=0.7, label='Near-term target (99.99%)')

# Annotate threshold values at reference points
ax.annotate('36', xy=(0.995, 36), fontsize=10, color='#d62728',
            ha='left', va='bottom', fontweight='bold',
            xytext=(0.9955, 60), arrowprops=dict(arrowstyle='->', color='#d62728', lw=1))

threshold_9999 = np.abs(ln_T) / np.abs(np.log(0.9999))
ax.annotate(f'{threshold_9999:.0f}', xy=(0.9999, threshold_9999), fontsize=10, color='#1f77b4',
            ha='left', va='bottom', fontweight='bold',
            xytext=(0.99992, threshold_9999 * 1.8), arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1))

ax.set_xlabel(r'Gate fidelity $F_{\mathrm{gate}}$', fontsize=12)
ax.set_ylabel(r'Decision threshold $(c-1)\,d$', fontsize=12)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(0.99, 1 - 1e-7)
ax.set_ylim(1, 1e6)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.3, which='both')
ax.set_title('Unitary-vs-dynamic decision boundary scaling', fontsize=12)

plt.tight_layout()
plt.savefig('threshold_scaling.pdf', dpi=300, bbox_inches='tight')
plt.savefig('threshold_scaling.png', dpi=300, bbox_inches='tight')
print('Saved threshold_scaling.pdf and threshold_scaling.png')

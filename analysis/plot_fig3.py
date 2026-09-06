"""Generate Figure 3: Noise budget breakdown."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(7, 4))

# --- Left: Per-step fidelity breakdown ---
ax = axes[0]
categories = ['Gate\n' + r'($F_\mathrm{gate}$)', 
              'Measurement\n' + r'($F_\mathrm{meas}$)', 
              'Decoherence\n' + r'($e^{-T_\mathrm{fb}/T_2}$)']
dynamic_vals = [0.995, 0.99, 0.84]
unitary_vals = [0.995, 1.0, 1.0]  # no measurement, no decoherence

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, dynamic_vals, width, label='Dynamic', 
               color='#d62728', alpha=0.8, edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, unitary_vals, width, label='Pure unitary', 
               color='#1f77b4', alpha=0.8, edgecolor='black', linewidth=0.5)

# Value labels on bars
for bar, val in zip(bars1, dynamic_vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005, 
            f'{val:.3f}', ha='center', va='bottom', fontsize=8, color='#d62728')
for bar, val in zip(bars2, unitary_vals):
    label = '1.0' if val == 1.0 else f'{val:.3f}'
    label_text = 'N/A' if val == 1.0 else label
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005, 
            label_text, ha='center', va='bottom', fontsize=8, color='#1f77b4')

ax.set_ylabel('Per-step fidelity factor', fontsize=10)
ax.set_ylim(0.75, 1.05)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=8)
ax.legend(fontsize=8, loc='lower left')
ax.set_title('(a) Per-step noise budget', fontsize=10, fontweight='bold', loc='left')
ax.grid(axis='y', alpha=0.3)
ax.axhline(y=1.0, color='gray', linestyle=':', alpha=0.4)

# Add product annotations
ax.annotate(r'$F_\mathrm{step}^\mathrm{dyn} \approx 0.83$', 
            xy=(1.5, 0.85), fontsize=9, ha='center', color='#d62728',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffcccc', alpha=0.5))
ax.annotate(r'$F_\mathrm{step}^\mathrm{uni} \approx 0.995$', 
            xy=(1.5, 0.97), fontsize=9, ha='center', color='#1f77b4',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#cce5ff', alpha=0.5))

# --- Right: Cumulative fidelity vs N ---
ax = axes[1]
N = np.arange(1, 32)
F_dyn = 0.83 ** N * 100
F_uni = 0.995 ** N * 100

ax.semilogy(N, F_dyn, '-', color='#d62728', linewidth=2, label=r'Dynamic: $0.83^N$')
ax.semilogy(N, F_uni, '-', color='#1f77b4', linewidth=2, label=r'Pure unitary: $0.995^N$')

# Fill the gap
ax.fill_between(N, F_dyn, F_uni, alpha=0.15, color='green', where=F_uni > F_dyn)

# Mark key points
ax.axhline(y=50, color='gray', linestyle=':', alpha=0.5)
ax.text(1, 52, '50% threshold', fontsize=7, color='gray')

# Annotations for 50% crossover
N50_dyn = np.log(0.5) / np.log(0.83)
N50_uni = np.log(0.5) / np.log(0.995)
ax.annotate(f'N={N50_dyn:.0f}', xy=(N50_dyn, 50), xytext=(N50_dyn + 3, 65),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=0.8),
            fontsize=8, color='#d62728')
ax.annotate(f'N={N50_uni:.0f}', xy=(N50_uni, 50), xytext=(N50_uni - 5, 30),
            arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=0.8),
            fontsize=8, color='#1f77b4')

ax.set_xlabel(r'Number of conditional operations ($N$)', fontsize=10)
ax.set_ylabel('Cumulative fidelity (%)', fontsize=10)
ax.set_xlim(0, 32)
ax.set_ylim(0.1, 120)
ax.legend(fontsize=8, loc='upper right')
ax.set_title('(b) Cumulative fidelity decay', fontsize=10, fontweight='bold', loc='left')
ax.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig(r'F:\PyQQQ\paper\fig3_noise_budget.pdf', dpi=300, bbox_inches='tight')
plt.savefig(r'F:\PyQQQ\paper\fig3_noise_budget.png', dpi=300, bbox_inches='tight')
print("Saved fig3_noise_budget")

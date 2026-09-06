"""Figure 4: Cumulative fidelity decay with per-step noise annotations."""
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

RED = '#d62728'
BLUE = '#1f77b4'
GRAY = '#666666'

fig, ax = plt.subplots(figsize=(7.0, 4.25))

N = np.arange(1, 32)
dynamic = 0.83 ** N * 100
unitary = 0.995 ** N * 100

ax.semilogy(N, dynamic, color=RED, linewidth=2.4,
            label=r'Dynamic: $F_{\rm step}=0.83$')
ax.semilogy(N, unitary, color=BLUE, linewidth=2.4,
            label=r'Pure unitary: $F_{\rm step}=0.995$')
ax.fill_between(N, dynamic, unitary, color='#7fbf7b', alpha=0.10)

N50_dynamic = np.log(0.5) / np.log(0.83)
N50_unitary = np.log(0.5) / np.log(0.995)
ax.axhline(50, color=GRAY, linestyle=':', linewidth=0.9, alpha=0.65)
ax.plot(N50_dynamic, 50, 'v', color=RED, markersize=7, zorder=4)
ax.text(N50_dynamic + 0.7, 56, f'50% at N={N50_dynamic:.0f}',
        fontsize=8, color=RED, va='bottom')
ax.text(31.5, 56, f'Pure unitary: N={N50_unitary:.0f} (off-scale)',
        fontsize=8, color=BLUE, ha='right', va='bottom')

ax.text(1.0, 25, r'Dynamic: $0.995 \times 0.99 \times 0.84 \approx 0.83$',
        fontsize=8, color=RED, va='center')
ax.text(1.0, 15, r'Pure unitary: $0.995$ per step',
        fontsize=8, color=BLUE, va='center')

ax.set_xlabel(r'Conditional operations ($N$)', fontsize=10)
ax.set_ylabel('Cumulative fidelity (%)', fontsize=10)
ax.set_xlim(0, 32)
ax.set_ylim(0.15, 130)
ax.set_title('Cumulative effect of per-step noise', fontsize=11, pad=8)
ax.legend(fontsize=8.5, loc='lower center', bbox_to_anchor=(0.5, 0.02),
          ncol=2, framealpha=0.92)
ax.grid(True, alpha=0.22, which='both')

output_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(output_dir, 'fig4_noise_budget.pdf'), dpi=300,
            bbox_inches='tight')
fig.savefig(os.path.join(output_dir, 'fig4_noise_budget.png'), dpi=300,
            bbox_inches='tight')
print('Saved fig4_noise_budget')

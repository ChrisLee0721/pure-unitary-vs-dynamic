"""Figure 2: Executable-depth projection across hardware generations."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.2, 4.1))

years = [2026, 2029, 2036]
dynamic_depth = [13, 87, 767]
unitary_depth = [459, 2302, 23023]
advantage = [35, 26, 30]

# Main lines with markers. Only the 2026 point is current; later points are estimates.
ax.plot(years, dynamic_depth, 'o-', color='#d62728', linewidth=2.2, markersize=8,
        markeredgecolor='white', markeredgewidth=1.5, label='Dynamic', zorder=5)
ax.plot(years, unitary_depth, 's-', color='#1f77b4', linewidth=2.2, markersize=8,
        markeredgecolor='white', markeredgewidth=1.5, label='Pure unitary', zorder=5)

# The area between the curves is not a measured quantity, so avoid implying it is.
ax.axvline(2026, color='#888888', linewidth=1.0, linestyle=':', zorder=1)
ax.text(2034.6, 42000, 'model projection', fontsize=8, color='#666666',
    ha='right', va='top', style='italic')

# Annotate advantage multipliers
for y, d, u, a in zip(years, dynamic_depth, unitary_depth, advantage):
    mid_y = np.sqrt(d * u)  # geometric mean for label position
    ax.text(y + 0.28, mid_y, f'{a}x', fontsize=9, fontweight='bold', color='#2ca02c',
            ha='left', va='center',
            bbox=dict(boxstyle='round,pad=0.16', facecolor='#e8f5e9', edgecolor='#2ca02c', alpha=0.85))

# Annotate actual values
dynamic_label_scale = {2026: 0.72, 2029: 0.52, 2036: 0.55}
for y, d in zip(years, dynamic_depth):
    ax.text(y - 0.22, d * dynamic_label_scale[y], f'{d:,}',
            fontsize=8, ha='right', va='center', color='#d62728')
for y, u in zip(years, unitary_depth):
    ax.text(y - 0.22, u * 1.35, f'{u:,}', fontsize=8, ha='right', va='center', color='#1f77b4')

# Formatting
ax.set_yscale('log')
ax.set_xlabel('Hardware generation', fontsize=10)
ax.set_ylabel('Executable depth (steps to 10% fidelity)', fontsize=10)
ax.set_xlim(2025, 2037.5)
ax.set_ylim(5, 50000)
ax.set_xticks(years)
ax.set_xticklabels(['2026\n(Current)', '2029\n(Estimate)', '2036\n(Estimate)'], fontsize=9)
ax.legend(fontsize=9, loc='upper left', framealpha=0.95)
ax.grid(True, alpha=0.22, which='major')
ax.set_title('Executable depth projection', fontsize=11, pad=8)

plt.tight_layout()
plt.savefig(r'F:\PyQQQ\paper\fig2_depth_projection.pdf', dpi=300, bbox_inches='tight')
plt.savefig(r'F:\PyQQQ\paper\fig2_depth_projection.png', dpi=300, bbox_inches='tight')
print("Saved fig2_depth_projection")

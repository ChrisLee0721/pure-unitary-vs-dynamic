"""Generate Figure 1: Circuit comparison (dynamic vs pure unitary)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, axes = plt.subplots(2, 1, figsize=(7, 4.5))

# --- Top: Dynamic circuit ---
ax = axes[0]
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

ax.text(-0.3, 1.5, r'$q_0$', fontsize=11, ha='right', va='center', fontweight='bold')
ax.text(-0.3, 0.5, r'$q_i$', fontsize=11, ha='right', va='center', fontweight='bold')

# Qubit lines
ax.plot([0, 10], [1.5, 1.5], 'k-', linewidth=1)
ax.plot([0, 10], [0.5, 0.5], 'k-', linewidth=1)

# Repeat for N times (show 3 iterations)
for i in range(3):
    x_base = 1.0 + i * 3.0
    # Measure box
    rect = FancyBboxPatch((x_base, 1.1), 0.8, 0.8, boxstyle="round,pad=0.05",
                           facecolor='#ffcccc', edgecolor='#d62728', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x_base + 0.4, 1.5, 'M', fontsize=9, ha='center', va='center', fontweight='bold', color='#d62728')
    
    # Classical wire (double line)
    ax.plot([x_base + 0.8, x_base + 1.3], [1.5, 1.5], '-', color='#d62728', linewidth=2)
    ax.plot([x_base + 0.8, x_base + 1.3], [1.45, 1.45], '-', color='#d62728', linewidth=2)
    
    # Classical "if" diamond
    ax.plot(x_base + 1.5, 1.5, 'D', markersize=8, color='#d62728', markeredgecolor='#d62728')
    
    # Conditional X gate
    rect2 = FancyBboxPatch((x_base + 1.8, 0.1), 0.6, 0.8, boxstyle="round,pad=0.05",
                            facecolor='#cce5ff', edgecolor='#1f77b4', linewidth=1.5)
    ax.add_patch(rect2)
    ax.text(x_base + 2.1, 0.5, r'$X$', fontsize=10, ha='center', va='center', color='#1f77b4')
    
    # Vertical dashed line (condition)
    ax.plot([x_base + 2.1, x_base + 2.1], [1.1, 0.9], '--', color='#d62728', linewidth=1)

# Dots for repetition
ax.text(9.5, 1.5, r'$\cdots$', fontsize=14, ha='center', va='center')
ax.text(9.5, 0.5, r'$\cdots$', fontsize=14, ha='center', va='center')

# Arrow for measurement feedback
ax.annotate('', xy=(x_base + 1.3, 1.0), xytext=(x_base + 0.8, 1.0),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.2))
ax.text(x_base + 1.05, 0.85, r'$T_\mathrm{fb}$', fontsize=7, ha='center', va='center', color='#d62728')

ax.set_title('(a) Dynamic circuit: measure $\\to$ decode $\\to$ conditionally apply', 
             fontsize=9, loc='left', pad=5, fontweight='bold')

# --- Bottom: Pure unitary circuit ---
ax = axes[1]
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

ax.text(-0.3, 1.5, r'$q_0$', fontsize=11, ha='right', va='center', fontweight='bold')
ax.text(-0.3, 0.5, r'$q_i$', fontsize=11, ha='right', va='center', fontweight='bold')

# Qubit lines
ax.plot([0, 10], [1.5, 1.5], 'k-', linewidth=1)
ax.plot([0, 10], [0.5, 0.5], 'k-', linewidth=1)

# CNOT gates (N times, show 4)
for i in range(4):
    x_base = 1.0 + i * 2.2
    # Control dot
    ax.plot(x_base + 0.3, 1.5, 'o', markersize=7, color='#1f77b4', markeredgecolor='#1f77b4')
    # Target circle with plus
    circle = plt.Circle((x_base + 0.3, 0.5), 0.25, fill=False, edgecolor='#1f77b4', linewidth=1.5)
    ax.add_patch(circle)
    ax.plot([x_base + 0.05, x_base + 0.55], [0.5, 0.5], '-', color='#1f77b4', linewidth=1.5)
    ax.plot([x_base + 0.3, x_base + 0.3], [0.25, 0.75], '-', color='#1f77b4', linewidth=1.5)
    # Vertical line connecting control and target
    ax.plot([x_base + 0.3, x_base + 0.3], [1.5, 0.75], '-', color='#1f77b4', linewidth=1.5)

# Dots for repetition
ax.text(9.8, 1.5, r'$\cdots$', fontsize=14, ha='center', va='center')
ax.text(9.8, 0.5, r'$\cdots$', fontsize=14, ha='center', va='center')

# Final measure
rect3 = FancyBboxPatch((10.0, 1.1), 0.5, 0.8, boxstyle="round,pad=0.05",
                        facecolor='#ffcccc', edgecolor='#d62728', linewidth=1.5)
ax.add_patch(rect3)
ax.text(10.25, 1.5, 'M', fontsize=9, ha='center', va='center', fontweight='bold', color='#d62728')

ax.set_title('(b) Pure unitary circuit: CNOT$\\otimes N$, measure once at the end', 
             fontsize=9, loc='left', pad=5, fontweight='bold')

plt.tight_layout()
plt.savefig(r'F:\PyQQQ\paper\fig1_circuit_comparison.pdf', dpi=300, bbox_inches='tight')
plt.savefig(r'F:\PyQQQ\paper\fig1_circuit_comparison.png', dpi=300, bbox_inches='tight')
print("Saved fig1_circuit_comparison")

"""Figure 1: Compact compilation map for the paper.

Each row maps one classical control structure to its pure-unitary form.
"""
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon

RED = '#c0392b'
RED_FILL = '#fff0f0'
BLUE = '#1a6fb5'
BLUE_FILL = '#f0f6ff'
GOLD = '#d4880f'
GOLD_FILL = '#fff8e0'
GRAY = '#555555'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'mathtext.fontset': 'dejavusans',
    'axes.unicode_minus': False,
})

fig, ax = plt.subplots(figsize=(9.5, 5.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')


def rounded_box(x, y, width, height, face, edge, linewidth=1.4, linestyle='-'):
    patch = FancyBboxPatch(
        (x, y), width, height,
        boxstyle='round,pad=0.035,rounding_size=0.08',
        facecolor=face, edgecolor=edge, linewidth=linewidth,
        linestyle=linestyle,
    )
    ax.add_patch(patch)
    patch.set_zorder(3)
    return patch


def label_box(x, y, width, height, text, face, edge, fontsize=10):
    patch = rounded_box(x, y, width, height, face, edge)
    patch.set_zorder(4)
    ax.text(x + width / 2, y + height / 2, text,
            ha='center', va='center', fontsize=fontsize,
            fontweight='bold', color=edge, zorder=5)


def wire(x0, x1, y, color='black', linewidth=1.0):
    ax.plot([x0, x1], [y, y], color=color, linewidth=linewidth, solid_capstyle='round')


def measurement(x, y):
    rounded_box(x - 0.18, y - 0.18, 0.36, 0.36, '#ffe0e0', RED, 1.2)
    ax.text(x, y, 'M', ha='center', va='center', fontsize=8,
            fontweight='bold', color=RED)


def decision(x, y):
    points = [(x, y + 0.2), (x + 0.2, y), (x, y - 0.2), (x - 0.2, y)]
    ax.add_patch(Polygon(points, closed=True, facecolor='#ffe0e0',
                 edgecolor=RED, linewidth=1.2, zorder=4))
    ax.text(x, y, '?', ha='center', va='center', fontsize=7,
            fontweight='bold', color=RED, zorder=5)


def cnot(x, y_control, y_target):
    ax.plot(x, y_control, 'o', color=BLUE, markersize=7, zorder=4)
    ax.plot([x, x], [y_control, y_target], color=BLUE, linewidth=1.2, zorder=3)
    circle = Circle((x, y_target), 0.15, fill=False, edgecolor=BLUE, linewidth=1.4)
    ax.add_patch(circle)
    ax.plot([x - 0.1, x + 0.1], [y_target, y_target], color=BLUE, linewidth=1.2)
    ax.plot([x, x], [y_target - 0.1, y_target + 0.1], color=BLUE, linewidth=1.2)


def draw_dynamic_conditional(y):
    wire(0.55, 4.05, y + 0.16)
    wire(0.55, 4.05, y - 0.16)
    ax.text(0.42, y + 0.16, r'$q_c$', ha='right', va='center', fontsize=8)
    ax.text(0.42, y - 0.16, r'$q_t$', ha='right', va='center', fontsize=8)
    measurement(1.05, y + 0.16)
    ax.plot([1.24, 1.65], [y + 0.16, y + 0.16], color=RED, linewidth=1.4)
    ax.plot([1.24, 1.65], [y + 0.11, y + 0.11], color=RED, linewidth=1.4)
    decision(1.85, y + 0.16)
    ax.plot([2.05, 2.05], [y + 0.04, y - 0.08], '--', color=RED, linewidth=0.9)
    label_box(1.85, y - 0.32, 0.4, 0.25, r'$U$', '#ffe0e0', RED, 8)
    ax.text(2.55, y + 0.32, 'measure -> decode -> branch',
            ha='center', va='center', fontsize=6, color=RED, style='italic')


def draw_controlled_unitary(y):
    wire(6.0, 9.45, y + 0.16)
    wire(6.0, 9.45, y - 0.16)
    ax.text(5.86, y + 0.16, r'$q_c$', ha='right', va='center', fontsize=8)
    ax.text(5.86, y - 0.16, r'$q_t$', ha='right', va='center', fontsize=8)
    cnot(7.7, y + 0.16, y - 0.16)
    ax.text(7.7, y - 0.47, r'$CU$', ha='center', va='center', fontsize=7, color=BLUE)
    ax.text(8.75, y - 0.28, 'retain $q_c$; no MCM',
            ha='center', va='center', fontsize=5.5, color=BLUE, style='italic')


def draw_for_unitary(y):
    wire(6.0, 9.45, y)
    ax.text(5.86, y, r'$q$', ha='right', va='center', fontsize=8)
    for x, text in zip([6.45, 7.1, 7.75, 8.4], [r'$U_1$', r'$U_2$', r'$U_3$', r'$\cdots$']):
        if text == r'$\cdots$':
            ax.text(x, y, text, ha='center', va='center', fontsize=11, color=BLUE)
        else:
            label_box(x - 0.22, y - 0.16, 0.44, 0.32, text, BLUE_FILL, BLUE, 8)
    label_box(8.85, y - 0.16, 0.48, 0.32, r'$U_N$', BLUE_FILL, BLUE, 8)
    ax.text(7.7, y - 0.45, 'fixed coherent sequence',
            ha='center', va='center', fontsize=6, color=BLUE, style='italic')


def draw_switch_unitary(y):
    wire(6.0, 9.45, y + 0.16)
    wire(6.0, 9.45, y - 0.16)
    ax.text(5.86, y + 0.16, r'$q_c$', ha='right', va='center', fontsize=8)
    ax.text(5.86, y - 0.16, r'$q_t$', ha='right', va='center', fontsize=8)
    cnot(7.7, y + 0.16, y - 0.16)
    ax.text(8.45, y - 0.38, r'$M = \sum_j |j\rangle\langle j| \otimes U_j$',
            ha='center', va='center', fontsize=6, color=BLUE)


def draw_while_unitary(y):
    wire(6.0, 9.45, y + 0.16)
    wire(6.0, 9.45, y - 0.16)
    ax.text(5.86, y + 0.16, r'$q_0$', ha='right', va='center', fontsize=8)
    ax.text(5.86, y - 0.16, r'$q_t$', ha='right', va='center', fontsize=8)
    ax.plot(7.7, y + 0.16, 'o', color=GOLD, markersize=7, zorder=4)
    ax.plot([7.7, 7.7], [y + 0.16, y - 0.16], color=GOLD, linewidth=1.2)
    label_box(7.47, y - 0.32, 0.46, 0.32, r'$RY(\theta)$', GOLD_FILL, GOLD, 7)
    ax.text(8.25, y + 0.38, r'$\theta = 2\arcsin\sqrt{1-(1/2)^N}$',
            ha='center', va='center', fontsize=7, color=GOLD)


# Header
label_box(0.35, 5.25, 3.35, 0.48, 'Classical control flow', RED_FILL, RED, 10)
label_box(6.3, 5.25, 3.35, 0.48, 'Pure unitary compilation', BLUE_FILL, BLUE, 10)
ax.annotate('', xy=(5.85, 5.49), xytext=(4.15, 5.49),
            arrowprops=dict(arrowstyle='->', linewidth=1.8, color=GRAY))
ax.text(5.0, 5.7, 'defer M + compile', ha='center', va='center', fontsize=6.5,
        fontweight='bold', color=GRAY)

# Row labels and content
rows = [(4.45, 'if', 'controlled-U'), (3.3, 'switch', 'multiplexer'),
        (2.15, 'for', 'unroll'), (1.0, 'while', 'amplitude amplification')]
for y, left, right in rows:
    edge = GOLD if left == 'while' else RED
    fill = GOLD_FILL if left == 'while' else RED_FILL
    rounded_box(0.35, y - 0.36, 1.05, 0.72, fill, edge, 1.3)
    ax.text(0.875, y, left, ha='center', va='center', fontsize=10,
            fontweight='bold', color=edge)
    ax.annotate('', xy=(5.65, y), xytext=(1.65, y),
                arrowprops=dict(arrowstyle='->', linewidth=1.2, color=GRAY))
    label_x = 4.25
    label_size = 5.8 if left == 'while' else 6.5
    ax.text(label_x, y + 0.18, right, ha='center', va='center', fontsize=label_size,
            fontweight='bold', color=BLUE if left != 'while' else GOLD)

# Left-side compact control-flow cues
for y in [4.45, 3.3, 1.0]:
    wire(1.72, 3.85, y, RED, 1.0)
measurement(2.15, 4.45)
decision(2.65, 4.45)
ax.text(1.97, 4.83, 'measure -> branch', ha='left', va='center', fontsize=6, color=RED)
measurement(2.15, 3.3)
decision(2.65, 3.3)
ax.text(1.97, 3.68, 'case c', ha='left', va='center', fontsize=6, color=RED)
label_box(1.97, 1.99, 0.45, 0.32, r'$U_i$', RED_FILL, RED, 8)
ax.text(1.97, 2.53, 'repeat N times', ha='left', va='center', fontsize=6, color=RED)
measurement(2.15, 1.0)
decision(2.65, 1.0)
ax.text(1.97, 1.38, 'repeat until success', ha='left', va='center', fontsize=6, color=RED)

# Right-side unitary realizations
draw_controlled_unitary(4.45)
draw_switch_unitary(3.3)
draw_for_unitary(2.15)
draw_while_unitary(1.0)

output_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(output_dir, 'fig1_compilation.pdf'), dpi=300,
            bbox_inches='tight')
fig.savefig(os.path.join(output_dir, 'fig1_compilation.png'), dpi=300,
            bbox_inches='tight')
print('Saved fig1_compilation')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfs = [pd.read_csv(f) for f in snakemake.input]
df = pd.concat(dfs, ignore_index=True)


k_order = [f"k={k}" for k in snakemake.config["k_values"]]
n_val = snakemake.config["n"]

plt.figure(figsize=(12, 6))
sns.set_style("ticks")
sns.boxplot(
    x='k', y='Mean', data=df, 
    order=k_order, 
    color='white', 
    linewidth=1.5,
    fliersize=5,
    flierprops={'marker': 'o', 'markerfacecolor': '#4C4C4C', 'markeredgecolor': 'none'}
)

plt.title(f'Testing Draws for {n_val}', fontsize=14, pad=15)
plt.ylabel('Mean', fontsize=12)
plt.xlabel('') 
plt.axhline(y=(n_val + 1) / 2, color='gray', linestyle='--', alpha=0.5) 

plt.tight_layout()
plt.savefig(snakemake.output[0], dpi=300)
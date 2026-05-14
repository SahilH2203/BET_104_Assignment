import pandas as pd
import numpy as np

k = int(snakemake.wildcards.k)
n = int(snakemake.config["n"])
repeats = int(snakemake.config["repeats"])

means = []
for _ in range(repeats):
    draws = np.random.randint(1, n + 1, size=k)
    means.append(np.mean(draws))

df = pd.DataFrame({'k': [f"k={k}"] * repeats, 'Mean': means})
df.to_csv(snakemake.output[0], index=False)

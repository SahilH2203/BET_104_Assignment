import pandas as pd
import numpy as np

# Snakemake automatically injects the `snakemake` object into this script
k = int(snakemake.wildcards.k)
n = int(snakemake.config["n"])
repeats = int(snakemake.config["repeats"])

means = []
for _ in range(repeats):
    # Draw k times from the range 1 to n (inclusive)
    draws = np.random.randint(1, n + 1, size=k)
    means.append(np.mean(draws))

# Save to the output file defined in the Snakefile
df = pd.DataFrame({'k': [f"k={k}"] * repeats, 'Mean': means})
df.to_csv(snakemake.output[0], index=False)
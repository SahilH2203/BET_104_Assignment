# Law of Large Numbers (LLN) Demonstration Pipeline

## Overview
This repository contains an automated workflow built with Snakemake to demonstrate the **Law of Large Numbers**. 

The code simulates drawing random samples of size `k` from a uniform range of numbers (from 1 to `n`). The Law of Large Numbers states that as the sample size (`k`) grows, the mean of the sample will converge closer to the true average of the entire population. The pipeline automatically runs these simulations, calculates the means across multiple repeats, and generates a boxplot visualizing this convergence.

Below is the generated plot for a population range of `n=2000`, testing draws up to `k=5000`:

<img width="3600" height="1800" alt="plot" src="https://github.com/user-attachments/assets/5c268cd0-03f9-4934-b389-cd3e93ce31a2" />


---

## File Structure

The repository is organized as follows to separate configuration, logic, and output:

```text
.
├── config.yaml             # Main configuration file containing n, repeats, and k values
├── Snakefile               # The Snakemake rules defining the workflow
├── plot.png                # The final generated boxplot
├── scripts/                # Python scripts that perform the logic
│   ├── generate_data.py    # Simulates random draws and saves means to CSV
│   └── plot_data.py        # Reads all CSVs and plots the final visualization
└── data/                   # Directory where generated CSVs are stored (created at runtime)
└── README.md
```

## How to Run This Repository

### 1. Prerequisites

To run this pipeline, you need Python installed on your system along with a few standard data science libraries and Snakemake.

Install all dependencies using:

```bash
pip install snakemake pandas numpy matplotlib seaborn
```

---

### 2. Setup

Clone this repository to your local machine and navigate into the project folder:

```bash
git clone https://github.com/SahilH2203/lln-assignment.git
cd lln-assignment
```

---

### 3. Running the Pipeline

To execute the workflow and generate the plot, run the following command from the root directory of the project:

```bash
snakemake -c1
```

> **Note:** `-c1` instructs Snakemake to use 1 CPU core.  
> You can increase this number (for example, `-c4`) to process data generations in parallel.

---

### 4. How to Change Parameters (k and n)

One of the main benefits of this pipeline is that you do not need to edit any Python code to test different scenarios.

To change the population size (`n`) or test different sample sizes (`k`):

1. Open the `config.yaml` file in any text editor.
2. Change the value of `n` to your desired range.
3. Add, remove, or modify the numbers in the `k_values` list.
4. Save the file.
5. Run the pipeline again using:

```bash
snakemake -c1
```

The pipeline will automatically detect the changes, generate the required data, and overwrite `plot.png` with the updated graph.

---

## Example `config.yaml`

```yaml
n: 2000
repeats: 10
k_values: [5, 10, 25, 50, 100, 200, 1000, 2000, 5000]
```

# Snakefile
configfile: "config.yaml"


rule all:
    input:
        "plot.png"

# Rule 1
rule generate_data:
    output:
        "data/k_{k}.csv"
    params:
        n = config["n"],
        repeats = config["repeats"]
    script:
        "scripts/generate_data.py"

# Rule 2
rule plot_data:
    input:
        expand("data/k_{k}.csv", k=config["k_values"])
    output:
        "plot.png"
    script:
        "scripts/plot_data.py"

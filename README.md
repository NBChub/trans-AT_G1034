# transAT_G1000
Analysis of TransAT PKS in the G1000 dataset

## Prerequisites
1. Setup BGCFlow following the [quickstart guide](https://github.com/NBChub/bgcflow?tab=readme-ov-file#quick-start)
2. This analysis utilizes this particular BGCFlow version: https://github.com/NBChub/bgcflow/tree/dev-0.8.1-2
```bash
BGCFLOW_DIR="bgcflow" # change according to your local path of BGCFlow
BGCFLOW_VERSION="dev-0.8.1-2"
(cd $BGCFLOW_DIR && git checkout $BGCFLOW_VERSION)
```

## Usage
1. Clone this repository to your local machine
```bash
git clone git@github.com:NBChub/transAT_G1034.git
cd transAT_G1034
```
2. Create symlinks to existing BGCFlow in your local machine
```bash
BGCFLOW_DIR="../bgcflow" # change according to your local path of BGCFlow
ln -s $BGCFLOW_DIR/.snakemake/ .snakemake
ln -s $BGCFLOW_DIR/resources/ resources
ln -s $BGCFLOW_DIR/workflow/ workflow
```
3. Make sure the input folder are structured correctly. Follow the structure defined in the `samples.csv`.
4. Run the BGC subworkflow:
```bash
conda activate bgcflow
bgcflow run --workflow BGC -c 16 -n # this is a dry-run
```
5. Remove the -n (dry-run) flag to execute the workflows

## Polishing the clinker figures
Due to current issue of clinker: https://github.com/gamcil/clinker/issues/106, the resulting svg from clinker might not be correctly annotated.
We provide a script to correct the svg generated using the session json. See [`notebooks/clinker_svg_correction.py`](`notebooks/clinker_svg_correction.py`) for more details how to use it.

# transAT_G1000
Analysis of TransAT PKS in the G1000 dataset

## Usage
1. This analysis utilizes this particular BGCFlow version: https://github.com/NBChub/bgcflow/commit/7a82ad8ee80deb996940f2c447ac9d2a4bee258a
2. Make sure the input folder are structured correctly. Follow the structure defined in the `samples.csv`.
3. Run this with BGCFlow subworkflow:
```bash
bgcflow run --workflow BGC -c 16 
```
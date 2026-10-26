# PfMYST × dihydroartemisinin single-cell project

This forkable Terputer project contains an [executed Jupyter notebook](notebooks/terputer-pfmyst-dha-single-cell.ipynb), a [streaming count-matrix analysis](research/transcriptomics/gse246115/analysis.py), a [sample manifest](research/transcriptomics/gse246115/sample_manifest.tsv), and a [claim-linked evidence brief](research/pfmyst-dha-single-cell/generated/white-paper.md). The [claim ledger](research/pfmyst-dha-single-cell/generated/claim-ledger.tsv) and execution and generation receipts record the exact analyzed files.

## Source and scope

[GEO GSE246115](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115) contains a PfMYST conditional knockdown line exposed to glucosamine and dihydroartemisinin (DHA), an artemisinin-derived sesquiterpene drug. The [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12394585/) reports additional functional and multi-omics findings. This project analyzes the deposited `MYST` single-cell count matrix only.

The source matrix has 5,720 gene rows and 78,262 cell columns in ten GEO sample groups. Each group is one GSM/library. Four treatment contrasts compare DHA with time-matched controls at 6 and 9 hours, separately without and with glucosamine. The analysis sums raw counts per GSM, converts to pseudobulk CPM, and compares descriptive gene-effect ranks. It does **not** treat cells as independent biological replicates, compute differential-expression p-values, or establish a causal PfMYST interaction.

The matrix is downloaded on demand from GEO and checked against SHA-256 `80c558a843104e98dd57753a1b9753bfde551616224d0433ef71b2e614a8f6bf`. It is excluded from Git. The processed summary tables under `research/transcriptomics/gse246115/results/` are committed.

## Reproduce

```sh
python -m pip install -r requirements.txt
python notebook-runner.py notebooks/terputer-pfmyst-dha-single-cell.ipynb . 180 '["research/transcriptomics/gse246115/results/sample_qc.tsv","research/transcriptomics/gse246115/results/contrast_summary.tsv","research/transcriptomics/gse246115/results/gene_descriptive.tsv","research/transcriptomics/gse246115/results/response_rank_correlations.tsv","research/transcriptomics/gse246115/results/analysis_summary.json"]'
node report-generator.mjs research/transcriptomics/gse246115/report-spec.json
```

To use this as a Terputer submodule, fork this repository to your GitHub account under the same name, `terpedia-pfmyst-dha-single-cell`, then attach slug `pfmyst-dha-single-cell` to your `terpedia-report` fork. The path will be `projects/pfmyst-dha-single-cell`.

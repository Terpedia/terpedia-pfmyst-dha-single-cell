# Dihydroartemisinin responses in a PfMYST perturbation context: a single-cell descriptive brief

> Generated evidence brief. Each statement is linked to a claim record; scientific interpretation still requires review.

**Research question:** Which DHA-associated transcript patterns agree across time and glucosamine strata, and what evidence would establish PfMYST dependence?

**Notebook:** `notebooks/terputer-pfmyst-dha-single-cell.ipynb` · SHA-256 `6eb4cda501562d829dbfb146588267fbf1c58ea611c1f32e9d279f3ea4e09229` · 2 executed code cells

## Abstract

GSE246115 includes Pfmyst-ty1-glmS parasite samples with and without glucosamine and with matched DHA-treated and untreated groups at 6 and 9 hours. (claim M01; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115), [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12394585/))

The checksum-pinned PfMYST subset contains 5,720 gene rows and 78,262 single-cell columns across ten GEO sample groups. (claim M02; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115))

Across 3,069 genes meeting the expression filter in all four controls, the four DHA-response rank lists have pairwise Spearman correlations from 0.814 to 0.917. (claim M04; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115))

## Background

GSE246115 includes Pfmyst-ty1-glmS parasite samples with and without glucosamine and with matched DHA-treated and untreated groups at 6 and 9 hours. (claim M01; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115), [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12394585/))

The primary study reports PfMYST knockdown, DHA survival, and multi-omics findings beyond the single-cell count matrix analyzed here. (claim M05; [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12394585/))

## Methods

The checksum-pinned PfMYST subset contains 5,720 gene rows and 78,262 single-cell columns across ten GEO sample groups. (claim M02; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115)) Artifacts: [research/transcriptomics/gse246115/results/analysis_summary.json](../../transcriptomics/gse246115/results/analysis_summary.json), [research/transcriptomics/gse246115/results/sample_qc.tsv](../../transcriptomics/gse246115/results/sample_qc.tsv).

## Results

The four time-matched DHA/control pseudobulk comparisons have median descriptive log2(CPM+1) ratios from -0.016 to -0.229 among genes with control CPM at least one. (claim M03; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115)) Artifacts: [research/transcriptomics/gse246115/results/contrast_summary.tsv](../../transcriptomics/gse246115/results/contrast_summary.tsv).

Across 3,069 genes meeting the expression filter in all four controls, the four DHA-response rank lists have pairwise Spearman correlations from 0.814 to 0.917. (claim M04; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115)) Artifacts: [research/transcriptomics/gse246115/results/analysis_summary.json](../../transcriptomics/gse246115/results/analysis_summary.json), [research/transcriptomics/gse246115/results/response_rank_correlations.tsv](../../transcriptomics/gse246115/results/response_rank_correlations.tsv).

## Interpretation

Across 3,069 genes meeting the expression filter in all four controls, the four DHA-response rank lists have pairwise Spearman correlations from 0.814 to 0.917. (claim M04; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115)) Artifacts: [research/transcriptomics/gse246115/results/analysis_summary.json](../../transcriptomics/gse246115/results/analysis_summary.json), [research/transcriptomics/gse246115/results/response_rank_correlations.tsv](../../transcriptomics/gse246115/results/response_rank_correlations.tsv).

The primary study reports PfMYST knockdown, DHA survival, and multi-omics findings beyond the single-cell count matrix analyzed here. (claim M05; [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12394585/))

## Limitations

The checksum-pinned PfMYST subset contains 5,720 gene rows and 78,262 single-cell columns across ten GEO sample groups. (claim M02; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115)) Artifacts: [research/transcriptomics/gse246115/results/analysis_summary.json](../../transcriptomics/gse246115/results/analysis_summary.json), [research/transcriptomics/gse246115/results/sample_qc.tsv](../../transcriptomics/gse246115/results/sample_qc.tsv).

The four time-matched DHA/control pseudobulk comparisons have median descriptive log2(CPM+1) ratios from -0.016 to -0.229 among genes with control CPM at least one. (claim M03; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115)) Artifacts: [research/transcriptomics/gse246115/results/contrast_summary.tsv](../../transcriptomics/gse246115/results/contrast_summary.tsv).

Across 3,069 genes meeting the expression filter in all four controls, the four DHA-response rank lists have pairwise Spearman correlations from 0.814 to 0.917. (claim M04; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115)) Artifacts: [research/transcriptomics/gse246115/results/analysis_summary.json](../../transcriptomics/gse246115/results/analysis_summary.json), [research/transcriptomics/gse246115/results/response_rank_correlations.tsv](../../transcriptomics/gse246115/results/response_rank_correlations.tsv).

## Next research steps

**Proposed:** Use independent parasite cultures at each glucosamine-by-DHA-by-time condition, verify PfMYST knockdown and stage balance, and fit a replicate-aware interaction model before attributing treatment-response differences to PfMYST. (claim M06; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115), [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12394585/))

## Data and code availability

The source specification is `research/transcriptomics/gse246115/report-spec.json` (SHA-256 `0d7d363295236eac6e708a990a8059cd008d82949278dc4066c4207f23578326`). The claim ledger and generation receipt accompany this report. File hashes identify the exact local inputs used. The [notebook execution receipt](../../execution-receipts/terputer-pfmyst-dha-single-cell.json) matches the saved notebook and records hashes for result files written during its fresh-kernel run. Notebook execution does not independently validate scientific interpretation.

## References

[1] GEO GSE246115. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE246115
[2] Primary PfMYST study. https://pmc.ncbi.nlm.nih.gov/articles/PMC12394585/

"""Streaming descriptive analysis of the public GSE246115 PfMYST count matrix."""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from urllib.request import urlretrieve

import numpy as np
import pandas as pd

URL = 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE246nnn/GSE246115/suppl/GSE246115_MYST_samples_scRNA_count_matrix.txt.gz'
SHA256 = '80c558a843104e98dd57753a1b9753bfde551616224d0433ef71b2e614a8f6bf'
GROUPS = [f'Myst_G{g}_DHA{d}_{h}h' for g,d,h in [(0,0,0),(0,0,6),(0,0,9),(0,1,6),(0,1,9),(1,0,0),(1,0,6),(1,0,9),(1,1,6),(1,1,9)]]
GSMS = ['GSM7855693','GSM7855694','GSM7855695','GSM7855696','GSM7855697','GSM7855698','GSM7855699','GSM7855700','GSM7855701','GSM7855702']
CONTRASTS = [(g,h) for g in (0,1) for h in (6,9)]


def run(root: Path) -> dict:
    base = root / 'research/transcriptomics/gse246115'
    data = base / 'data/GSE246115_MYST_samples_scRNA_count_matrix.txt.gz'
    data.parent.mkdir(parents=True, exist_ok=True)
    if not data.exists():
        urlretrieve(URL, data)
    if hashlib.sha256(data.read_bytes()).hexdigest() != SHA256:
        raise ValueError('GEO count-matrix checksum mismatch')
    with gzip.open(data, 'rt') as stream:
        header = stream.readline().rstrip('\n').split('\t')
        groups = [label.split('-')[0] for label in header[1:]]
        unexpected = set(groups) - set(GROUPS)
        if unexpected or not groups:
            raise ValueError(f'Unexpected matrix group labels: {unexpected}')
        indexes = np.asarray([GROUPS.index(group) for group in groups], dtype=np.int8)
        cells = len(groups)
        cell_umis = np.zeros(cells, dtype=np.int64)
        cell_detected = np.zeros(cells, dtype=np.int32)
        genes = []
        sums = []
        for line in stream:
            gene, values = line.split('\t', 1)
            counts = np.fromstring(values, sep='\t', dtype=np.int32)
            if counts.size != cells or np.any(counts < 0):
                raise ValueError(f'Invalid count row {gene}')
            genes.append(gene)
            sums.append(np.bincount(indexes, weights=counts, minlength=len(GROUPS)).astype(np.int64))
            cell_umis += counts
            cell_detected += counts > 0
    sums = np.vstack(sums)
    if len(set(genes)) != len(genes):
        raise ValueError('Duplicate gene identifiers')
    group_cells = np.bincount(indexes, minlength=len(GROUPS))
    total_umis = sums.sum(axis=0)
    if np.any(group_cells == 0) or np.any(total_umis == 0):
        raise ValueError('Empty group')
    cpm = sums / total_umis * 1_000_000
    qc = pd.DataFrame([{'group':group,'gsm':gsm,'cells':int(group_cells[i]),'total_umis':int(total_umis[i]),'median_umis_per_cell':float(np.median(cell_umis[indexes==i])),'median_detected_genes_per_cell':float(np.median(cell_detected[indexes==i]))} for i,(group,gsm) in enumerate(zip(GROUPS,GSMS))])
    gene_table = pd.DataFrame({'gene_id':genes})
    contrast_rows = []
    for g,h in CONTRASTS:
        control = GROUPS.index(f'Myst_G{g}_DHA0_{h}h')
        treated = GROUPS.index(f'Myst_G{g}_DHA1_{h}h')
        effects = np.log2(cpm[:,treated]+1) - np.log2(cpm[:,control]+1)
        label = f'G{g}_{h}h'
        gene_table[f'{label}_control_cpm'] = cpm[:,control]
        gene_table[f'{label}_dha_cpm'] = cpm[:,treated]
        gene_table[f'{label}_log2_cpm_plus_1_ratio'] = effects
        eligible = cpm[:,control] >= 1
        contrast_rows.append({'contrast':label,'control_gsm':qc.iloc[control].gsm,'dha_gsm':qc.iloc[treated].gsm,'eligible_control_cpm_at_least_1':int(eligible.sum()),'fraction_positive':float(np.mean(effects[eligible]>0)),'fraction_negative':float(np.mean(effects[eligible]<0)),'median_log2_cpm_plus_1_ratio':float(np.median(effects[eligible]))})
    contrast = pd.DataFrame(contrast_rows)
    eligible_all = np.logical_and.reduce([cpm[:,GROUPS.index(f'Myst_G{g}_DHA0_{h}h')] >= 1 for g,h in CONTRASTS])
    effect_columns = [f'G{g}_{h}h_log2_cpm_plus_1_ratio' for g,h in CONTRASTS]
    correlations = gene_table.loc[eligible_all,effect_columns].corr(method='spearman').round(4)
    output = base / 'results'
    output.mkdir(parents=True, exist_ok=True)
    qc.to_csv(output/'sample_qc.tsv',sep='\t',index=False)
    contrast.to_csv(output/'contrast_summary.tsv',sep='\t',index=False)
    gene_table.to_csv(output/'gene_descriptive.tsv',sep='\t',index=False,float_format='%.6g')
    correlations.to_csv(output/'response_rank_correlations.tsv',sep='\t',float_format='%.4f')
    summary = {'accession':'GSE246115','matrix_sha256':SHA256,'feature_rows':len(genes),'cell_columns':cells,'groups':len(GROUPS),'single_gsm_per_condition':True,'common_expressed_features_for_rank_comparison':int(eligible_all.sum()),'analysis':'Single-library pseudobulk CPM and gene-wise descriptive log2(CPM+1) ratios, separately by glucosamine stratum and time. No DE p-values or causal PfMYST interaction inference.'}
    (output/'analysis_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary

if __name__ == '__main__':
    print(json.dumps(run(Path(__file__).resolve().parents[3]),indent=2))

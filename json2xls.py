import json
import sys

# Converting Nirvana JSON to table
# delimiter is a semicolon

def getGenotype(txt):
    if txt == '1':
        return "homozygous"
    delim = "/"
    if '|' in txt:
        delim = '|'
    alleles = txt.split(delim)
    if len(alleles) == 2:
        if alleles[0] == alleles[1]:
            return "homozygous"
        else:
            return "heterozygous"
    return "multiallelic"

def processClinvar(v):
    clinvar = {'id':[], 'variationid':[], 'reviewstatus':[], 'refallele':[], 'altallele':[], 'phenotypes':[], 'medgenids':[], 'significance':[], 'lastUpdateData':[], 'pubmedIDS':[]}
    if 'clinvar' in v:
        cvs = v['clinvar']
        for cv in cvs:
            clinvar['id'].append(cv['id'])
            if 'variationId' in cv:
                clinvar['variationid'].append(cv['variationId'])
            clinvar['reviewstatus'].append(cv['reviewStatus'])
            clinvar['refallele'].append(cv['refAllele'])
            clinvar['altallele'].append(cv['altAllele'])
            if 'phenotypes' in cv:
                clinvar['phenotypes'].append(','.join(cv['phenotypes']))
            if 'medGenIds' in cv:
                clinvar['medgenids'].append(','.join(cv['medGenIds']))
            clinvar['significance'].append(','.join(cv['significance']))
            if 'lastUpdateDate' in cv:
                clinvar['lastUpdateData'].append(cv['lastUpdateDate'])
            if 'pubMedIds' in cv:
                clinvar['pubmedIDS'].append(','.join(cv['pubMedIds']))
    clinvar['id'] = ','.join(clinvar['id'])
    clinvar['variationid'] = ','.join(clinvar['variationid'])
    clinvar['reviewstatus'] = ','.join(clinvar['reviewstatus'])
    clinvar['refallele'] = ','.join(clinvar['refallele'])
    clinvar['altallele'] = ','.join(clinvar['altallele'])
    clinvar['phenotypes'] = ','.join(clinvar['phenotypes'])
    clinvar['medgenids'] = ','.join(clinvar['medgenids'])
    clinvar['significance'] = ','.join(clinvar['significance'])
    clinvar['lastUpdateData'] = ','.join(clinvar['lastUpdateData'])
    clinvar['pubmedIDS'] = ','.join(clinvar['pubmedIDS'])

    return clinvar

def processTrascript(v, genetable):
    transcript = {'hgvsc':[], 'hgvsp':[], 'geneId':[], 'function':[], 'impact':[], 'siftscore':[], 'siftpred':[], 'polyPhenScore':[], 'polyPhenPrediction':[], 'gene': [], 'omim_geneID': [], 'phenotype_omimid': [], 'phenotype': [], 'inheritance': []}
    if 'transcripts' in v:
        trs = v['transcripts']
        for tr in trs:
            if 'isCanonical' in tr and tr['isCanonical'] and tr['source'] == "RefSeq" and tr['hgnc'] in genetable and tr['consequence'] != 'upstream_gene_variant' and tr['consequence'] != 'downstream_gene_variant':
                if 'hgvsc' in tr:
                    transcript['hgvsc'].append(tr['hgvsc'])
                if 'hgvsp' in tr:
                    transcript['hgvsp'].append(tr['hgvsp'])
                if 'geneId' in tr:
                    transcript['geneId'].append(tr['geneId'])
                if 'bioType' in tr:
                    transcript['function'].append(tr['bioType'])
                if 'consequence' in tr:
                    transcript['impact'].append(','.join(tr['consequence']))
                if 'siftScore' in tr:
                    transcript['siftscore'].append(str(tr['siftScore']))
                if 'siftPrediction' in tr:
                    transcript['siftpred'].append(tr['siftPrediction'])
                if 'polyPhenScore' in tr:
                    transcript['polyPhenScore'].append(str(tr['polyPhenScore']))
                if 'polyPhenPrediction' in tr:
                    transcript['polyPhenPrediction'].append(tr['polyPhenPrediction'])
                transcript['gene'].append(tr['hgnc'])
                transcript['omim_geneID'].append(genetable[tr['hgnc']]['omim'])
                transcript['phenotype_omimid'].append(genetable[tr['hgnc']]['pheno'])
                transcript['phenotype'].append(genetable[tr['hgnc']]['phenotype'])
                transcript['inheritance'].append(genetable[tr['hgnc']]['inherit'])

    transcript['hgvsc'] = ','.join(transcript['hgvsc'])
    transcript['hgvsp'] = ','.join(transcript['hgvsp'])
    transcript['geneId'] = ','.join(transcript['geneId'])
    transcript['function'] = ','.join(transcript['function'])
    transcript['impact'] = ','.join(transcript['impact'])
    transcript['siftscore'] = ','.join(transcript['siftscore'])
    transcript['siftpred'] = ','.join(transcript['siftpred'])
    transcript['polyPhenScore'] = ','.join(transcript['polyPhenScore'])
    transcript['polyPhenPrediction'] = ','.join(transcript['polyPhenPrediction'])
    transcript['gene'] = ','.join(transcript['gene'])
    transcript['omim_geneID'] = ','.join(transcript['omim_geneID'])
    transcript['phenotype_omimid'] = ','.join(transcript['phenotype_omimid'])
    transcript['phenotype'] = ','.join(transcript['phenotype'])
    transcript['inheritance'] = ','.join(transcript['inheritance'])
    return transcript

jsonfile = open(sys.argv[1], "r")
rawjson = json.load(jsonfile)

genetable = dict()
for g in rawjson['genes']:
    gname = g['name']
    if gname not in genetable:
        omimid = []
        phenoid = []
        phenotype = []
        inheritance = []
        if 'omim' in g:
            for omim in g['omim']:
                omimid.append(str(omim['mimNumber']))
                if 'phenotypes' in omim:
                    for p in omim['phenotypes']:
                        if 'mimNumber' in p:
                            phenoid.append(str(p['mimNumber']))
                        if 'phenotype' in p:
                            phenotype.append(p['phenotype'])
                        if 'inheritances' in p:
                            inheritance.append(",".join(p['inheritances']))
        genetable[gname] = dict()
        genetable[gname]['omim'] = ','.join(omimid)
        genetable[gname]['pheno'] = ','.join(phenoid)
        genetable[gname]['phenotype'] = ','.join(phenotype)
        genetable[gname]['inherit'] = ','.join(inheritance)
    else:
        print(gname, "gene already exists")

for s in rawjson['positions']:
    chrx = s['chromosome']
    pos  = s['position']
    refa = s['refAllele']
    alta = ','.join(s['altAlleles'])

    samples = s['samples']
    gt = getGenotype(samples[0]['genotype'])
    coverage = samples[0]['totalDepth']
    variant_depth = samples[0]['alleleDepths'][1]
    variant_freq = samples[0]['variantFrequencies'][0]

    varis = s['variants']
    for v in varis:
        vid = v['vid']
        dbsnp = ""
        hgvsg = ""
        gnomADfreq = ""
        primateAI = ""
        dann_score = ""
        revel_score = ""
        if 'dbsnp' in v:
            dbsnp = ",".join(v['dbsnp'])
        cv = processClinvar(v)
        varit = v['variantType']
        if 'gnomad' in v:
            gnomADfreq = v['gnomad']['allAf']
        if 'primateAI' in v:
            primateAI = v['primateAI'][0]['scorePercentile']
        if 'dannScore' in v:
            dann_score = v['dannScore']
        if 'revel' in v:
            revel_score = v['revel']['score']
        tr = processTrascript(v, genetable)
        print(vid, chrx, pos, dbsnp, refa, alta, varit, gt, coverage, variant_depth, variant_freq, gnomADfreq, primateAI, dann_score, revel_score, tr['hgvsc'], tr['hgvsp'], tr['geneId'], tr['function'], tr['impact'], tr['siftscore'], tr['siftpred'], tr['polyPhenScore'], tr['polyPhenPrediction'], tr['gene'], tr['omim_geneID'], tr['phenotype_omimid'], tr['phenotype'], tr['inheritance'], cv['id'], cv['variationid'], cv['reviewstatus'], cv['refallele'], cv['altallele'], cv['phenotypes'], cv['medgenids'], cv['significance'], cv['lastUpdateData'], cv['pubmedIDS'], sep = ";")

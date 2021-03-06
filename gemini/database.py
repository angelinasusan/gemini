#!/usr/bin/env python
 
import sqlite3

def index_variation(cursor):
    cursor.execute('''create index var_chr_start_idx on\
                      variants(chrom, start)''')
    cursor.execute('''create index var_type_idx on variants(type)''')
    cursor.execute('''create index var_gt_counts_idx on \
                      variants(num_hom_ref, num_het, \
                               num_hom_alt, num_unknown)''')
    cursor.execute('''create index var_aaf_idx on variants(aaf)''')
    cursor.execute('''create index var_in_dbsnp_idx on variants(in_dbsnp)''')
    cursor.execute('''create index var_in_call_rate_idx on \
                      variants(call_rate)''')
    cursor.execute('''create index var_exonic_idx on variants(is_exonic)''')
    cursor.execute('''create index var_coding_idx on variants(is_coding)''')
    cursor.execute('''create index var_lof_idx on variants(is_lof)''')
    cursor.execute('''create index var_depth_idx on variants(depth)''')

def index_variation_impacts(cursor):
    cursor.execute('''create index varimp_exonic_idx on \
                      variant_impacts(is_exonic)''')
    cursor.execute('''create index varimp_coding_idx on \
                      variant_impacts(is_coding)''')
    cursor.execute('''create index varimp_lof_idx on variant_impacts(is_lof)''')
    cursor.execute('''create index varimp_impact_idx on \
                      variant_impacts(impact)''')

def index_samples(cursor):
    cursor.execute('''create unique index sample_name_idx on samples(name)''')

def create_indices(cursor):
    """
    Index our master DB tables for speed
    """
    index_variation(cursor)
    index_samples(cursor)

def create_tables(cursor):
    """
    Create our master DB tables
    """
    cursor.execute('''create table if not exists variants  (    \
                    chrom text,                                 \
                    start integer,                              \
                    end integer,                                \
                    variant_id integer,                         \
                    anno_id integer,                            \
                    ref text,                                   \
                    alt text,                                   \
                    qual float,                                 \
                    filter text,                                \
                    type text,                                  \
                    sub_type text,                              \
                    gts blob,                                   \
                    gt_types blob,                              \
                    gt_phases blob,                             \
                    gt_depths blob,                             \
                    call_rate float,                            \
                    in_dbsnp bool,                              \
                    rs_ids text default NULL,                   \
                    in_omim bool,                               \
                    clin_sigs text default NULL,                \
                    cyto_band text default NULL,                \
                    rmsk text default NULL,                     \
                    in_cpg_island bool,                         \
                    in_segdup bool,                             \
                    is_conserved bool,                          \
                    num_hom_ref integer,                        \
                    num_het integer,                            \
                    num_hom_alt integer,                        \
                    num_unknown integer,                        \
                    aaf float,                                  \
                    hwe float,                                  \
                    inbreeding_coeff float,                     \
                    pi float,                                   \
                    recomb_rate float,                          \
                    gene text,                                  \
                    transcript text,                            \
                    is_exonic bool,                             \
                    is_coding bool,                             \
                    is_lof bool,                                \
                    exon text,                                  \
                    codon_change text,                          \
                    aa_change text,                             \
                    aa_length text,                             \
                    biotype text,                               \
                    impact text default NULL,                   \
                    impact_severity text,                       \
                    polyphen_pred text,                         \
                    polyphen_score float,                       \
                    sift_pred text,                             \
                    sift_score float,                           \
                    anc_allele text,                            \
                    rms_bq float,                               \
                    cigar text,                                 \
                    depth integer default NULL,                 \
                    strand_bias float default NULL,             \
                    rms_map_qual float default NULL,            \
                    in_hom_run integer default NULL,            \
                    num_mapq_zero integer default NULL,         \
                    num_alleles integer default NULL,           \
                    num_reads_w_dels float default NULL,        \
                    haplotype_score float default NULL,         \
                    qual_depth float default NULL,              \
                    allele_count integer default NULL,          \
                    allele_bal float default NULL,              \
                    in_hm2 bool,                                \
                    in_hm3 bool,                                \
                    is_somatic,                                 \
                    in_esp bool,                                \
                    aaf_esp_ea float,                           \
                    aaf_esp_aa float,                           \
                    aaf_esp_all float,                          \
                    exome_chip bool,                            \
                    in_1kg bool,                                \
                    aaf_1kg_amr float,                          \
                    aaf_1kg_asn float,                          \
                    aaf_1kg_afr float,                          \
                    aaf_1kg_eur float,                          \
                    aaf_1kg_all float,                          \
                    grc text default NULL,                      \
                    gms_illumina float,                         \
                    gms_solid float,                            \
                    gms_iontorrent float,                       \
                    encode_tfbs,                                \
                    encode_consensus_gm12878 text,              \
                    encode_consensus_h1hesc text,               \
                    encode_consensus_helas3 text,               \
                    encode_consensus_hepg2 text,                \
                    encode_consensus_huvec text,                \
                    encode_consensus_k562 text,                 \
                    encode_segway_gm12878 text,                 \
                    encode_segway_h1hesc text,                  \
                    encode_segway_helas3 text,                  \
                    encode_segway_hepg2 text,                   \
                    encode_segway_huvec text,                   \
                    encode_segway_k562 text,                    \
                    encode_chromhmm_gm12878 text,               \
                    encode_chromhmm_h1hesc text,                \
                    encode_chromhmm_helas3 text,                \
                    encode_chromhmm_hepg2 text,                 \
                    encode_chromhmm_huvec text,                 \
                    encode_chromhmm_k562 text,                  \
                    PRIMARY KEY(variant_id ASC))''')

    cursor.execute('''create table if not exists variant_impacts  (   \
                    variant_id integer,                               \
                    anno_id integer,                                  \
                    gene text,                                        \
                    transcript text,                                  \
                    is_exonic bool,                                   \
                    is_coding bool,                                   \
                    is_lof bool,                                      \
                    exon text,                                        \
                    codon_change text,                                \
                    aa_change text,                                   \
                    aa_length text,                                   \
                    biotype text,                                     \
                    impact text,                                      \
                    impact_severity text,                             \
                    polyphen_pred text,                               \
                    polyphen_score float,                             \
                    sift_pred text,                                   \
                    sift_score float,                                 \
                    PRIMARY KEY(variant_id ASC, anno_id ASC))''')

    cursor.execute('''create table if not exists samples   (  \
                    sample_id integer,                        \
                    name text,                                \
                    family_id integer default NULL,           \
                    paternal_id integer default NULL,         \
                    maternal_id integer default NULL,         \
                    sex text default NULL,                    \
                    phenotype text default NULL,              \
                    ethnicity text default NULL,              \
                    PRIMARY KEY(sample_id ASC))''')

    cursor.execute('''create table if not exists sample_genotypes (  \
                    sample_id integer,                               \
                    gt_types BLOB,                                   \
                    PRIMARY KEY(sample_id ASC))''')
                                                                     
    cursor.execute('''create table if not exists sample_genotype_counts ( \
                     sample_id integer,                                   \
                     num_hom_ref integer,                                 \
                     num_het integer,                                     \
                     num_hom_alt integer,                                 \
                     num_unknown integer,                                 \
                     PRIMARY KEY(sample_id ASC))''')

def insert_variation(cursor, buffer):
    """
    Populate the variants table with each variant in the buffer.
    """
    cursor.execute("BEGIN TRANSACTION")
    cursor.executemany('insert into variants values (?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?,?,?,?,?,?,?,?,?,?, \
                                                     ?)', \
                                                     buffer)
    cursor.execute("END")
    

def insert_variation_impacts(cursor, buffer):
    """
    Populate the variant_impacts table with each variant in the buffer.
    """
    cursor.execute("BEGIN TRANSACTION")
    cursor.executemany('insert into variant_impacts values (?,?,?,?,?,?,?,?, \
                                                            ?,?,?,?,?,?,?,?, \
                                                            ?,?)', \
                                                            buffer)
    cursor.execute("END")


def insert_sample(cursor,sample_list):
    """
    Populate the samples with sample ids, names, and 
    other indicative information.
    """
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute('''insert into samples values \
                                  (?,?,?,?,?,?,?,?)''', sample_list)
    cursor.execute("END")


def close_and_commit(cursor, connection):
    """
    Commit changes to the DB and close out DB cursor.
    """
    connection.commit()
    cursor.close


def empty_tables(cursor):
    cursor.execute('''delete * from variation''')
    cursor.execute('''delete * from samples''')

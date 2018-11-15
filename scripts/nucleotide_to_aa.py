#!/usr/bin/python
'''
 convert the data from nucleotiodes into
 amino acid data for inclusion with the data in Amino Acids.
 wikipedia has a nice chart if you need more information
 at https://en.wikipedia.org/wiki/DNA_codon_table
'''

import pandas as pd
import re


def _codons_to_aa():
    _codons = {
        "TTT": "F",
        "TTC": "F",
        "TTA": "L",
        "TTG": "L",
        "CTT": "L",
        "CTC": "L",
        "CTA": "L",
        "CTG": "L",
        "ATT": "I",
        "ATC": "I",
        "ATA": "I",
        "ATG": "M",
        "GTT": "V",
        "GTC": "V",
        "GTA": "V",
        "GTG": "V",
        "TCT": "S",
        "TCC": "S",
        "TCA": "S",
        "TCG": "S",
        "CCT": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "ACT": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "GCT": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "TAT": "Y",
        "TAC": "Y",
        "TAA": "STOP",
        "TAG": "STOP",
        "CAT": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "AAT": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "GAT": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "TGT": "C",
        "TGC": "C",
        "TGA": "STOP",
        "TGG": "W",
        "CGT": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AGT": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GGT": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G"
    }
    return _codons


def _process_conversion_impl(_file_name, _column_name):
    try:
        df = pd.read_excel(_file_name)
    except OSError as e:
        print("Inavlid file name: {}\n{}".format(_file_name, e))

    _codons = _codons_to_aa()
    aa_lst = []
    for index, row in df.iterrows():
        converted_aa = ""
        nucleotide_list = re.findall('...', row[_column_name])
        for nucleotide in nucleotide_list:
            val = _codons.get(nucleotide.upper())
            if (val):
                if (val) == "STOP":
                    print("STOP detected in row: {}", format(index))
                converted_aa += val
        aa_lst.append(converted_aa)

    df['{}_converted_aa'.format(_column_name)] = aa_lst
    df.to_excel('{}_converted_aa.xlsx'.format(_file_name), index=False)


def process_conversion(file_name, column_name):

    return _process_conversion_impl(file_name, column_name)


if __name__ == "__main__":
    file_name = input("Enter file name to be processed: ")
    col_name = input("Enter column name containing nucleotiodes: ")
    process_conversion(file_name, col_name)
    print("Processed results are available in file: {}_converted_aa.xlsx".
          format(file_name))

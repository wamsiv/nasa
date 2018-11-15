#!/usr/bin/python
'''
Each amino acid has its own polarity. So when forming a junction for example "CER", how does we calculate charge and overall polarity for it? my mathematical assumption would be 
C -> neutral, polar
E -> negative, polar
R -> positive, polar

Charge: 0-+
Polarity: +++
'''

import pandas as pd
import re


def _polarity():
    _pol = {
        "A": "-",
        "R": "+",
        "N": "+",
        "D": "+",
        "C": "-",
        "E": "+",
        "Q": "+",
        "G": "-",
        "H": "+",
        "I": "-",
        "L": "-",
        "K": "+",
        "M": "-",
        "F": "-",
        "P": "-",
        "S": "+",
        "T": "+",
        "W": "-",
        "Y": "+",
        "V": "-"
    }
    return _pol


def _charge():
    _chrg = {
        "A": "0",
        "R": "+",
        "N": "0",
        "D": "-",
        "C": "0",
        "E": "-",
        "Q": "0",
        "G": "0",
        "H": "+",
        "I": "0",
        "L": "0",
        "K": "+",
        "M": "0",
        "F": "0",
        "P": "0",
        "S": "0",
        "T": "0",
        "W": "0",
        "Y": "0",
        "V": "0"
    }
    return _chrg


def _process_charge_polarity_impl(_file_name, _column_name):
    try:
        df = pd.read_excel(_file_name)
    except OSError as e:
        print("Inavlid file name: {}\n{}".format(_file_name, e))

    _charges = _charge()
    _polarities = _polarity()
    aa_pol = []
    aa_chg = []
    for index, row in df.iterrows():
        charge_aa = ""
        polarity_aa = ""
        aa_list = re.findall('.', row[_column_name])
        for acid in aa_list:
            val_chg = _charges.get(acid.upper())
            val_pol = _polarities.get(acid.upper())
            if (val_pol and val_chg):
                charge_aa += val_chg
                polarity_aa += val_pol
        aa_chg.append(charge_aa)
        aa_pol.append(polarity_aa)
    df['{}_charge'.format(_column_name)] = aa_chg
    df['{}_polarity'.format(_column_name)] = aa_pol
    df.to_excel('{}_polarity_charge.xlsx'.format(_file_name), index=False)


def process_charge_polarity(file_name, column_name):

    return _process_charge_polarity_impl(file_name, column_name)


if __name__ == "__main__":
    file_name = input("Enter file name to be processed: ")
    col_name = input("Enter column name containing Amino Acid Junction: ")
    process_charge_polarity(file_name, col_name)
    print("Processed results are available in file: {}_polarity_charge.xlsx".
          format(file_name))
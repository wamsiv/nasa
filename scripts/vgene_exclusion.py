#!/usr/bin/python

'''
Will exclude V-GENEs that are biologically
not removes any V-gene segment that isn't biologically possible.
Only if atleast 1 biologically possible gene segment remains in this
column the CDR3 is included for analysis.
'''

import pandas as pd


def _acceptable_vgenes():
    boilogical_vgenes = [
        "IGHV10-1\*01", "IGHV10-3\*01", "IGHV11-1\*01", "IGHV1-11\*01",
        "IGHV11-2\*01", "IGHV1-12\*01", "IGHV1-14\*01", "IGHV1-15\*01",
        "IGHV1-17-1\*01", "IGHV1-18\*01", "IGHV1-19\*01", "IGHV1-20\*01",
        "IGHV1-22\*01", "IGHV12-3\*01", "IGHV1-23\*01", "IGHV1-26\*01",
        "IGHV1-31\*01", "IGHV13-2\*01", "IGHV1-34\*01", "IGHV1-36\*01",
        "IGHV1-37\*01", "IGHV1-39\*01", "IGHV1-4\*01", "IGHV14-1\*01",
        "IGHV14-2\*01", "IGHV1-42\*01", "IGHV14-3\*01", "IGHV1-43\*01",
        "IGHV14-4\*01", "IGHV1-47\*01", "IGHV1-49\*01", "IGHV1-5\*01",
        "IGHV1-50\*01", "IGHV15-2\*01", "IGHV1-52\*01", "IGHV1-53\*01",
        "IGHV1-54\*01", "IGHV1-55\*01", "IGHV1-56\*01", "IGHV1-58\*01",
        "IGHV1-59\*01", "IGHV1-61\*01", "IGHV1-62-1\*01", "IGHV1-62-2\*01",
        "IGHV1-62-3\*01", "IGHV1-63\*01", "IGHV1-64\*01", "IGHV1-66\*01",
        "IGHV1-67\*01", "IGHV1-69\*01", "IGHV1-7\*01", "IGHV1-71\*01",
        "IGHV1-72\*01", "IGHV1-74\*01", "IGHV1-75\*01", "IGHV1-76\*01",
        "IGHV1-77\*01", "IGHV1-78\*01", "IGHV1-80\*01", "IGHV1-81\*01",
        "IGHV1-82\*01", "IGHV1-84\*01", "IGHV1-85\*01", "IGHV1-9\*01",
        "IGHV1S100\*01", "IGHV1S5\*01", "IGHV2-2\*01", "IGHV2-3\*01",
        "IGHV2-4\*01", "IGHV2-5\*01", "IGHV2-6\*01", "IGHV2-6-8\*01",
        "IGHV2-7\*01", "IGHV2-9\*01", "IGHV2-9-1\*01", "IGHV3-1\*01",
        "IGHV3-3\*01", "IGHV3-4\*01", "IGHV3-5\*01", "IGHV3-6\*01",
        "IGHV3-8\*01", "IGHV3S7\*01", "IGHV4-1\*01", "IGHV5-12\*01",
        "IGHV5-12-4\*01", "IGHV5-15\*01", "IGHV5-16\*01", "IGHV5-17\*01",
        "IGHV5-2\*01", "IGHV5-4\*01", "IGHV5-6\*01", "IGHV5-9\*01",
        "IGHV5-9-1\*02", "IGHV5S21\*01", "IGHV6-3\*01", "IGHV6-4\*01",
        "IGHV6-5\*01", "IGHV6-6\*01", "IGHV6-7\*01", "IGHV7-1\*01",
        "IGHV7-3\*01", "IGHV7-4\*01", "IGHV8-11\*01", "IGHV8-12\*01",
        "IGHV8-4\*01", "IGHV8-5\*01", "IGHV8-6\*01", "IGHV8-8\*01",
        "IGHV9-1\*01", "IGHV9-2\*01", "IGHV9-3\*01", "IGHV9-4\*01",
        "IGHD1-1\*01", "IGHD2-3\*01", "IGHD2-4\*01", "IGHD2-5\*01",
        "IGHD3-1\*01", "IGHD3-2\*02", "IGHD4-1\*01", "IGHD5-2\*01",
        "IGHD5-5\*01", "IGHD6-3\*01", "IGHD6-4\*01", "IGHJ1\*03", "IGHJ2\*01",
        "IGHJ3\*01", "IGHJ4\*01"
    ]
    return boilogical_vgenes


def _process_exclusion_impl(_file_name, _column_name):

    try:
        df = pd.read_excel(_file_name)
    except OSError as e:
        print("Inavlid file name: {}\n{}".format(_file_name, e))
    print("Total number of original records: {}".format(len(df)))

    df = df[df[_column_name].str.contains('|'.join(_acceptable_vgenes()))]
    print("Total number of records after exclusion: {}".format(len(df)))

    df.to_excel('{}_excluded_vgenes.xlsx'.format(_file_name), index=False)


def process_exclusion(file_name, column_name):

    return _process_exclusion_impl(file_name, column_name)


if __name__ == "__main__":
    file_name = input("Enter file name to be processed: ")
    col_name = input("Enter column name containing V-GENEs: ")
    process_exclusion(file_name, col_name)
    print("Processed results are available in file: {}_excluded_vgenes.xlsx".
          format(file_name))

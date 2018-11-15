Each heavy chain of the antibody is composed of the recombination of a specific V, D, and J gene segment. We're interested in the ontogeny of these CDR3s. Biologically, even if two different heavy chains have the SAME CDR3, if they do not have the same V/D/J Gene segments, they cannot be related.

Sample date is in `scripts\Example_Data.xlsx`

`scripts\vgene_exclusion.py` - Will exclude V-GENEs that are biologically not removes any V-gene segment that isn't biologically possible. Only if atleast 1 biologically possible gene segment remains in this column the CDR3 is included for analysis.

`scripts\nucleotide_to_aa.py` -  convert the data from nucleotiodes into amino acid data for inclusion with the data in Amino Acids. wikipedia has a nice chart if you need more information at https://en.wikipedia.org/wiki/DNA_codon_table
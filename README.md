# PhosphoSitePlus-Peptide-Search

A Python script to search for post-translational modifications in given peptides using the PhosphoSitePlus API. 

Takes an input table containing UniProt IDs and peptides, and returns any associated modifications.


## Installation

Python, then install the required dependencies:

pip install -r requirements.txt


## Usage

Prepare the input file (e.g. input.csv):

UniProt ID |	position |	peptide

HMHA1_HUMAN |	1083 |	REDGDGDE

Run the script:

python PullingPhosphosite.py

Results saved as phosphosite_results.csv


## Output Format

The output CSV file will contain the following columns:

UniProt ID: The UniProt identifier of the protein.

Peptide: The queried peptide sequence.

Modifications: Any modifications found in the peptide.


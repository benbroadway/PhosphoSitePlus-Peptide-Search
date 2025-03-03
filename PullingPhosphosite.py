import requests
import pandas as pd

"Pull from the PhosphoSitePlus API for modifications in a given peptide sequence"
def peptidephosphosite(peptide):
    base_url = "https://www.phosphosite.org/api/"
    endpoint = f"search?peptide={peptide}"
    
    response = requests.get(base_url + endpoint)
    
    if response.status_code == 200:
        data = response.json()
        return data 
    else:
        print(f"Error: Unable to fetch data for peptide {peptide}")
        return None

"Read peptide inputs from a file and query PhosphoSitePlus for modifications"
def p_input_file(input_file):
    df = pd.read_csv(input_file, sep=',') 
    
    results = []
    for _, row in df.iterrows():
        uniprot_id = row['UniProt ID']
        peptide = row['peptide']
        
        mod_data = peptidephosphosite(peptide)
        if mod_data:
            filtered_mods = [mod for mod in mod_data if mod.get('UniProt ID') == uniprot_id]
            results.append({
                "UniProt ID": uniprot_id,
                "Peptide": peptide,
                "Modifications": filtered_mods
            })
    
    output_df = pd.DataFrame(results)
    output_df.to_csv("results.csv", index=False)
    print("Results saved to results.csv")

if __name__ == "__main__":
    input_file = "test.csv"  # Change this to your file
    p_input_file(input_file)

import requests
import os

pdb_ids = ['1GU8','1L2G','1M0K'] # will input from text file eventually 

def get_mmCIF_files(pdb_ids, output_dir):
    # Download mmCIF files for the identified PDB IDs
    for pdb_id in pdb_ids:
        url = f"https://files.rcsb.org/download/{pdb_id}.cif"
        output_file = os.path.join(output_dir, f"{pdb_id}.cif")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(output_file, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {pdb_id}.cif")
            else:
                print(f"Failed to download {pdb_id}.cif")
        except Exception as e:
            print(f"Failed to download {pdb_id}.cif: {e}")

# Example usage:
output_dir = "/Users/alisonfaid1/Documents/GitHub/AF_openfold/training_data_af"


get_mmCIF_files(pdb_ids, output_dir)

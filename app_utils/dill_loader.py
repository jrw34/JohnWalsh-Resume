import dill
def undill_it(filepath:str):
    """Open dill files and return object to assigned variable"""
    with open(filepath, 'rb') as f:
        return dill.load(f)

def dill_it(parent_dir:str, filename:str, data_structure):
    """Serialize objects for use in streamlit app"""

    #create filepath string
    filepath = '/'.join([parent_dir, filename + '.dll'])
    
    #serialize object using dill
    with open(filepath, 'wb') as f:
        dill.dump(data_structure, f)
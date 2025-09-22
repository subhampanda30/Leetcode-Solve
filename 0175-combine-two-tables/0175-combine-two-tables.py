import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Left merge to keep all persons, even those without addresses
    result = person.merge(address, on='personId', how='left')
    
    # Select only the required columns in the specified order
    result = result[['firstName', 'lastName', 'city', 'state']]
    
    return result
    
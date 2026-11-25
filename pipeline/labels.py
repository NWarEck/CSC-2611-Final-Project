import geopandas as gpd

def unit_to_period(code: str):
    if(code[0].islower()):
        code = code[1:]

    if not (code[0].isupper() and code[1].isupper()):
        if(code[0] == "A"):
            return "Amazonian"
        if(code[0]== "N"):
            return "Noachian"
        if(code[0] == "H"):
            return "Hesperian"
        else:
            return "Unknown"
    
    return "Mixed"
    
    
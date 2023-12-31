import ETL.extract  as extract
import ETL.transform as transform

def run():
    extract.extract_aspus()
    data = transform.clean_aspus()
    return data

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def search_token(search_string):
    csv_file = "parser/token.csv"
    results = pd.DataFrame()
    df = pd.read_csv(csv_file)
    mask = df.apply(lambda row: row.astype(str).str.contains(search_string, case=False).any(), axis=1)
    filtered_df = df[mask]
    results = pd.concat([results, filtered_df])
    return results

def search_cc(search_string):
    csv_file = "parser/cc.csv"
    results = pd.DataFrame()
    df = pd.read_csv(csv_file)
    mask = df.apply(lambda row: row.astype(str).str.contains(search_string, case=False).any(), axis=1)
    filtered_df = df[mask]
    results = pd.concat([results, filtered_df])
    return results

# print(search_token("0xa1faa113cbE53436Df28FF0aEe54275c13B40975"))
print(search_cc("Ethereum"))
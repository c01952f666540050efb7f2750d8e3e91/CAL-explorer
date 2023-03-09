import urllib.request



# Use main or develop
def retreive_cal(version:str="main"):
    url = f"https://raw.githubusercontent.com/LedgerHQ/ledger-live/{version}/apps/ledger-live-desktop/cryptoassets.md"
    # Write to file
    urllib.request.urlretrieve(url, "cryptoassets.txt")


retreive_cal()
import pandas as pd

def import_sheet(url):
    df = pd.read_csv(url)
    print(df)


if __name__ == "__main__":
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTMIUP6_JIoxWSAFCe1h6Hz12r-41t6qHv5cCXIBmYJUK2KS188pKkZnkr4jJRpIcC3mRZV36z21oNv/pub?gid=0&single=true&output=csv"
    import_sheet(url)
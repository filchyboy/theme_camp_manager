def import_google_sheet(url):
    df = pd.read_csv(url)
    return df
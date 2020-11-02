
def date_cln(df, column):
    df[f"{column}"] = df[f"{column}"].str.extract(r'(\d\d\d\d.\d\d.\d\d)(.*)')
    return df[f"{column}"]

def species_ordering(df, column, shark):
    df[f"{column}"] = df[f"{column}"].str.replace(fr"(.*){shark}'(.*)", f"{shark} shark")

def deleting_nulls(df, column):
    df = df[~df[f"{column}"].isnull()]


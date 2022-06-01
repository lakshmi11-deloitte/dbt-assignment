import pandas as pd
df = pd.read_xml(open(input("filename : "),"r").read())
trim = df.loc[:1000]
trim.to_csv(input("output filename :"),index=False)
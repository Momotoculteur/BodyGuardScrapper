import pandas as pd

def cleanDuplicateData:
    data = pd.read_csv('data.txt', sep=",", header=None)
    data.columns = ["text", "result"]
    print(data.shape)

    # Supprimer les row en doubles
    df2 = data.drop_duplicates(subset='text', keep="last").reset_index(drop=True)
    # Nb total de lignes

    #file = open('data.txt', 'w')
    #file.close()
    print(df2.shape)
    df2.to_csv('cleanData.txt', header=None, index=None, sep=',', mode='w')


def showValuesCount:
    data = pd.read_csv('cleanData.txt', sep=",", header=None)
    data.columns = ["text", "result"]
    print(data['result'])

def cleanResultName:
    goodResult = ['0', '1']

    for index, row in data.iterrows():
        if not (row['result'] in goodResult):
            print(row)




if __name__ == "__main__":
    # execute only if run as a script
    #cleanDuplicateData()
    showValuesCount()
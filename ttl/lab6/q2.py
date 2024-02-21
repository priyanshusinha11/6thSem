import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_csv(filename):
    return pd.read_csv(filename)

def boxplot_analysis(dataframe, attribute):
    sns.boxplot(x=attribute, data=dataframe)
    plt.title(f'Boxplot Analysis for {attribute}')
    plt.show()

if __name__ == "__main__":
    filename = 'data.csv'
    df = read_csv(filename)
    print("Data loaded successfully.")

    attribute_to_analyze = 'Age'  
    boxplot_analysis(df, attribute_to_analyze)

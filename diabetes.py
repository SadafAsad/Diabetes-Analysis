import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyodide.http import pyfetch
import asyncio

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


asyncio.run(download(filename, "diabetes.csv"))
# df = pd.read_csv("diabetes.csv")


# print("The first 5 rows of the dataframe") 
# print(df.head(5))

# df.shape

# df.info()

# df.describe()

# missing_data = df.isnull()
# missing_data.head(5)

# for column in missing_data.columns.values.tolist():
#     print(column)
#     print (missing_data[column].value_counts())
#     print("")    


# df.dtypes

# labels= 'Not Diabetic','Diabetic'
# plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
# plt.legend()
# plt.show()

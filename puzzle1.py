# import pandas as pd

# df = pd.read_csv("csv-sample.csv")


# total_rows = len(df.axes[0])

# print("Number of Rows: "+str(total_rows))

import pandas as pd

rows = pd.read_csv('csv-sample.csv')

print(f"Number of rows : {len(rows)}")

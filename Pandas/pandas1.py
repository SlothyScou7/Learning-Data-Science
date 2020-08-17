import pandas as pd

df=pd.DataFrame(    # to manually store a data we use a data frame!
    {
        "Name":["Braund, Mr. Owen Harris",
                 "Allen, Mr. William Henry",
                 "Bonnell, Miss. Elizabeth"],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"]
    }
)
# print(df["Age"])
print(df.describe().count())   



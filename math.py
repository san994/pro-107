import plotly.express as px
import pandas as pd
import csv

df = pd.read_csv("pro 107/data.csv")

student_data = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()

fig  = px.scatter(student_data,x="student_id",y="level",size="attempt",color='attempt',size_max=20)

fig.show()
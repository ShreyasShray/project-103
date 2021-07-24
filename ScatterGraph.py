import pandas as pd
import plotly.express as px

df = pd.read_csv("dataOfCovid.csv")

Scatter_graph = px.scatter(df, x = "date", y = "cases", color = "country")

Scatter_graph.show()
import plotly.graph_objects as go

figure_config = dict({
    "data":[
                {
                "type":"bar",
                "x":["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
                 "y":[28, 27, 25, 31, 32, 35, 36]
                }
            ],
             "Layout":{"title":"Temperatures of the weak", "x": 0.5, "font":{'color':'red','size':15} }
})
fig = go.Figure(figure_config)
fig.show()
import plotly.graph_objects as go

#def function to display animation of 24/7 Software internship
def animated_intern_graph(intern_data, intern_pos_dict):
    """
    Input:  intern_data::dict
                Dictionary containing label with corresponding hoverinfo as key,value pairs respectively
                
            intern_pos_dict::dict
                Dictionary containing label with corresponding tuple w/ locations of the form (x,y)

    Output:
            plotly figure object
    """
    animated_intern_plot = go.Figure(
        data = [go.Scatter(x = [0], y = [10], mode = 'markers', name = '')],
        layout = go.Layout(
            updatemenus = [dict(
                type = 'buttons',
                buttons = [dict(label = "Build Graph",
                                method = "animate",
                                args = [None])])],
            yaxis = dict(tickmode = 'array',
                         tickvals = [15, 10, 7, 4, 1, -2, -5, -10],
                         ticktext = ['', 'Company', 'Role and Timeframe', 'Project Name', 
                                     'Project Description', 'Some Interesting Results', 'Project Impact', ''],
                         tickfont = dict(size = 15),
                         range = [-10, 15]
                        ),
            xaxis = dict(range = [-3, 3]),
            title = dict(text = 'Internship At 24/7 Software', x = 0.55, y=0.9, 
                         xanchor = 'center', yanchor = 'top'),
            plot_bgcolor = 'lightgray',
            width = 800,
            height = 600,
            font = dict(color = '#1A0A53', size = 14),
            hoverlabel = dict(font = dict(family = 'sans-serif', size = 16), bgcolor='white')),
            frames = [ #start frames list
                  go.Frame(data = [go.Scatter(x = [0], 
                                              y = [10], 
                                              mode = 'markers',
                                              marker_color = 'blue',
                                              marker_size = 20)]), #frame 1 (still at root) 
                  
                  go.Frame(data = [go.Scatter(x = [0, -0.25, 0.25], 
                                              y = [10, 8.5, 8.5], 
                                              mode = 'markers',
                                              marker_color = 'blue')]), #frame 2 (move to leaves 1 & 2)
                  
                  go.Frame(data = [go.Scatter(x = [0, -1, 1], 
                                              y = [10, 7, 7], 
                                              mode = 'markers')]), #frame 3 (still at leaves 1 & 2)
                  
                  go.Frame(data = [go.Scatter(x = [0, -1, 1, -0.25, 0.25], 
                                              y = [10, 7, 7, 5.5, 5.5], 
                                              mode = 'markers')]), #frame 4 (move to leaf 3)
                  
                  go.Frame(data = [go.Scatter(x = [0, -1, 1, 0], 
                                              y = [10, 7, 7, 4], 
                                              mode = 'markers')]), #frame 5 (still at leaf 3)
                  
                  go.Frame(data = [go.Scatter(x = [0, -1, 1, 0, -1, -0.5, 0.5, 1], 
                                              y = [10, 7, 7, 4, 1.5, 1.5, 1.5, 1.5], 
                                              mode = 'markers')]), #frame 6 (move to leaves 4,5,6,7)
                  
                  go.Frame(data = [go.Scatter(x = [0, -1, 1, 0, -2, -1, 1, 2], 
                                              y = [10, 7, 7, 4, 1, 1, 1, 1], 
                                              mode = 'markers')]), #frame 7 (still at leaves 4,5,6,7)

                  go.Frame(data = [go.Scatter(x = [0, -1, 1, 0, -2, -1, 1, 2, -0.25, 0.25],
                                              y = [10, 7, 7, 4, 1, 1, 1, 1, -1, -1],
                                              mode = 'markers')]), #frame 8 (move to leaves 8 & 9)

                  go.Frame(data = [go.Scatter(x = [0, -1, 1, 0, -2, -1, 1, 2, -0.5, 0.5],
                                              y = [10, 7, 7, 4, 1, 1, 1, 1, -2, -2],
                                              mode = 'markers')]), #frame 9 (still at leaves 8 & 9)
                  
                  go.Frame(data = [go.Scatter(x = [0, -1, 1, 0, -2, -1, 1, 2, -0.5, 0.5, -0.25, 0.25],
                                              y = [10, 7, 7, 4, 1, 1, 1, 1, -2, -2, -2.5, -2.5],
                                              mode = 'markers')]), #frame 8 (move)
                  go.Frame(data = go.Scatter(x = [pos[0] for pos in intern_pos_dict.values()],
                                             y = [pos[1] for pos in intern_pos_dict.values()],
                                             mode = 'markers',
                                             hovertemplate = list(intern_data.values()),
                                             marker_color = 'blue',
                                             marker_size = [35] + [25]*9 + [35]))  #final frame
                 ] #end frames list
                                ).update_xaxes(showticklabels=False, 
                                               showgrid = False, 
                                               zeroline = False, 
                                               fixedrange = True)\
                                 .update_yaxes(showgrid = True, 
                                               zeroline = False, 
                                               tickfont = dict(size = 20, color = '#1A0A53'),
                                               fixedrange = True)

    return animated_intern_plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#def function to return plotly figure displaying Treemap containing education data
def education_treemap(tdi_data, fau_data): #add in sector color spefications to function args ... maybe kwargs
    #create subplot template
    education_trees = make_subplots(
        cols = 2, 
        rows = 1,
        column_widths = [0.4, 0.6],
        subplot_titles = ('<b>The Data Incubator<b>', '<b>Florida Atlantic University<b>'),
        specs = [[{'type' : 'treemap', 'rowspan' : 1}, {'type': 'treemap'}]]
                                )\
                        .add_trace(go.Treemap( #add TDI trace to subplot figure
                    labels = tdi_data,
                    parents = [""] + [tdi_data[0]]*4,
                    values = [16] + [4]*4,
                    branchvalues = 'total',
                    insidetextfont = dict(size = 15),
                    outsidetextfont = dict(size = 25),
                    hoverinfo = 'skip',
                    marker_colors = ['lightgray'] + ['lightgreen','blue']*2),
                    row = 1, 
                    col = 1)\
                        .add_trace(go.Treemap( #add FAU trace to subplot figure
                    labels = fau_data,
                    parents = [""] + [fau_data[0]]*6,
                    values = [18] + [3]*6,
                    branchvalues = 'total',
                    hoverinfo = 'skip',
                    insidetextfont = dict(size = 15),
                    outsidetextfont = dict(size = 25),
                    marker_colors = ['lightgray'] + ['blue', 'red']*3),
                    row = 1, 
                    col = 2)\
                        .update_annotations(yshift=20, font_size = 28) #set titles above figures to create more space and increase font
    
    #return plotly figure object
    return education_trees


import plotly.graph_objects as go
from plotly.subplots import make_subplots

#def function to return plotly figure displaying Treemap containing education data
def education_treemap(tdi_data, fau_data, color_1, color_2, sector_bg_color, sector_font_color):
    #create subplot template
    education_trees = make_subplots(
        cols = 2, 
        rows = 1,
        column_widths = [0.4, 0.6],
        subplot_titles = ('The Data Incubator', 'Florida Atlantic University'),
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
                    marker_colors = [sector_bg_color] + [color_1, color_2]*2,
                    textfont=dict(
                                size=18,
                                color=sector_font_color)),
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
                    marker_colors = [sector_bg_color] + [color_1, color_2]*3,
                    textfont=dict(
                                size=18,
                                color=sector_font_color)),
                    row = 1, 
                    col = 2)\
                        .update_annotations(yshift=20, font_size = 28, font_color = sector_font_color)
    
    #return plotly figure object
    return education_trees


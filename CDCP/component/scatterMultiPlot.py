#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import plotly.graph_objects as go
from plotly.subplots import make_subplots

from datatable import f




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 18


    def drawMultiScatter(self, cluster_class, sources):
        """"""

        self.FIGURE = make_subplots(1, len(sources), subplot_titles=(sources))
        
        for i in range(0, len(sources)):

            if cluster_class == 'Cell Type':

                for trace in self.METADATA.FEATURE['typeSet']:

                    tip = trace + ' | ' + self.METADATA.COLOR[f.GROUP == trace, 'CLUSTER'][0, 0]

                    if 'MARKER' in self.METADATA.COLOR.keys():
                        tip = tip + '<br />Marker: ' + self.METADATA.COLOR[f.GROUP == trace, 'MARKER'][0, 0]

                    X = self.METADATA.DATATABLE[(f.SOURCE == sources[i]) & (f.TYPE == trace), 'UMAP1'].to_list()[0]
                    Y = self.METADATA.DATATABLE[(f.SOURCE == sources[i]) & (f.TYPE == trace), 'UMAP2'].to_list()[0]

                    self.FIGURE.add_trace(
                        go.Scattergl(
                            name=trace,

                            x=X,
                            y=Y,

                            mode='markers',
                            marker=dict(
                            
                                size=2,
                                color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],

                            ),

                            hoverinfo='text',
                            hovertext=tip,

                            showlegend=False
                        ),

                        1, i + 1
                    )

            if cluster_class == 'Brain Area':

                tip = self.METADATA.DATATABLE[f.SOURCE == sources[i], 'TYPE'].to_list()[0]

                X = self.METADATA.DATATABLE[f.SOURCE == sources[i], 'UMAP1'].to_list()[0]
                Y = self.METADATA.DATATABLE[f.SOURCE == sources[i], 'UMAP2'].to_list()[0]

                self.FIGURE.add_trace(
                    go.Scattergl(
                        name=sources[i],

                        x=X,
                        y=Y,

                        mode='markers',
                        marker=dict(
                        
                            size=2,
                            color=self.METADATA.COLOR[f.GROUP == sources[i], 'COLOR'][0, 0],

                        ),

                        hoverinfo='text',
                        hovertext=tip,

                        showlegend=False
                    ),

                    1, i + 1
                )
                

        self.FIGURE.update_xaxes(matches='x')
        self.FIGURE.update_yaxes(matches='y')

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                x=0.5,

                text='Cluster by Cell Type among Different ' + cluster_class, 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE
                    
                )

            ),

            legend=dict(

                itemsizing='constant'

            )
            
        )
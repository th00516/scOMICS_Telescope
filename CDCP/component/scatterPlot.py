#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import plotly.graph_objects as go

from datatable import f




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 18


    def drawScatter(self, cluster_class):
        """"""

        self.FIGURE = go.Figure()

        if cluster_class == 'Cell Type':

            for trace in self.METADATA.FEATURE['typeSet']:

                tip = trace + ' | ' + self.METADATA.COLOR[f.GROUP == trace, 'CLUSTER'][0, 0]

                if 'MARKER' in self.METADATA.COLOR.keys():
                    tip = tip + '<br />Marker: ' + self.METADATA.COLOR[f.GROUP == trace, 'MARKER'][0, 0]

                X = self.METADATA.DATATABLE[f.TYPE == trace, 'UMAP1'].to_list()[0]
                Y = self.METADATA.DATATABLE[f.TYPE == trace, 'UMAP2'].to_list()[0]

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
                        hovertext=tip    
                    )
                )

        if cluster_class == 'Brain Area':

            for trace in self.METADATA.FEATURE['sourceSet']:

                tip = trace + ' | ' + self.METADATA.COLOR[f.GROUP == trace, 'CLUSTER'][0, 0]

                X = self.METADATA.DATATABLE[f.SOURCE == trace, 'UMAP1'].to_list()[0]
                Y = self.METADATA.DATATABLE[f.SOURCE == trace, 'UMAP2'].to_list()[0]

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
                        hovertext=tip
                    )
                )


        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                x=0.5,

                text='Cluster by ' + cluster_class,
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            ),

            annotations=[

                dict(
                    x=0.5,
                    y=-0.12,
                    showarrow=False,
                    xref='paper',
                    yref='paper',

                    text='UMAP 1'
                ),

                dict(
                    x=-0.1,
                    y=0.5,
                    textangle=-90,
                    showarrow=False,
                    xref='paper',
                    yref='paper',

                    text="UMAP 2"
                )

            ],

            legend=dict(

                itemsizing='constant'

            ),

            showlegend=True

        )
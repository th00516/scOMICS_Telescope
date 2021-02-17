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


    def drawViolin(self, cluster_class, fieldName):
        """"""

        self.FIGURE = go.Figure()

        if cluster_class == 'Cell Type':

            for trace in self.METADATA.FEATURE['typeSet']:

                self.FIGURE.add_trace(
                    go.Violin(
                        name=trace,

                        y=self.METADATA.DATATABLE[f.TYPE == trace, fieldName].to_list()[0],

                        fillcolor=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                        line_color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],

                        line_width=2,

                        points=False,
                        spanmode='hard',

                        hoverinfo='text',
                        hovertext=trace,

                        showlegend=False
                    )
                )

        if cluster_class == 'Brain Area':

            for trace in self.METADATA.FEATURE['sourceSet']:

                self.FIGURE.add_trace(
                    go.Violin(
                        name=trace,

                        y=self.METADATA.DATATABLE[f.SOURCE == trace, fieldName].to_list()[0],

                        fillcolor=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                        line_color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],

                        line_width=2,

                        points=False,
                        spanmode='hard',

                        hoverinfo='text',
                        hovertext=trace,

                        showlegend=False
                    )
                )


        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                x=0.5,

                text='Expression of <i>' + fieldName + '</i> in Different ' + cluster_class,
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE
                    
                )

            ),

            xaxis_tickangle=-45
        )

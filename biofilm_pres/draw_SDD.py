import graphviz

# Create the System Dynamics (SD) diagram
dot = graphviz.Digraph()

dot.attr(rankdir='LR')
dot.attr('node',shape='rectangle',style='filled',fillcolor='white')

# Define sources
with dot.subgraph(name='cluster_sources') as sources:
    sources.attr(rank="same",style='filled')
    sources.attr(label="sources",shape="box")
    sources.node('source_A','',shape='circle')
    sources.node('source_B','',shape='circle')

# Define stocks
with dot.subgraph(name='cluster_stocks') as stocks:
    stocks.attr(rank="same",style='filled')
    stocks.attr(label='stocks',shape='box')
    stocks.node('stock_A','biofilm mass')
    stocks.node('stock_B','substrate')

with dot.subgraph(name='cluster_sinks') as sinks:
    sinks.attr(rank='same',style='filled')
    sinks.attr(label='sinks',shape='box')
    sinks.node('sink_A','',shape='circle')
    sinks.node('sink_B','',shape='circle')

# Define valves
with dot.subgraph(name='cluster_valves_left') as valves_left:
   valves_left.attr(rank='same')
   valves_left.node('valve_A1','',shape='point',width='0.1', \
                    fillcolor='black')
   valves_left.node('valve_B1','',shape='point',width='0.1', \
                    fillcolor='black')

with dot.subgraph(name='cluster_valves_right') as valves_right:
   valves_right.attr(rank='same')
   valves_right.node('valve_A2','',shape='point',width='0.1', \
                     fillcolor='black')
   valves_right.node('valve_B2','',shape='point',width='0.1', \
                     fillcolor='black')

# Define flow rate moderators
with dot.subgraph(name='effects') as effects:
   effects.attr(rank='same')
   effects.node('gradient','pressure gradient',shape='none')
   effects.node('velocity','fluid velocity',shape='none')
   effects.node('sloughing','sloughing',shape='none')

# Add edges
dot.edge('source_A','valve_A1',arrowhead='none',penwidth='5', \
         color='coral')
dot.edge('valve_A1','stock_A',penwidth='5',color='coral')
dot.edge('stock_A','valve_A2',arrowhead='none',penwidth='5', \
         color='coral')
dot.edge('valve_A2','sink_A',penwidth='5', \
         color='coral')
dot.edge('source_B','valve_B1',arrowhead='none',penwidth='5', \
         color='red')
dot.edge('valve_B1','stock_B',penwidth='5',color='red')
dot.edge('stock_B','valve_B2',arrowhead='none',penwidth='5', \
         color='red')
dot.edge('valve_B2','sink_B',penwidth='5',color='red')
dot.edge('stock_B','valve_A1')
dot.edge('sloughing','valve_A2')
dot.edge('velocity','sloughing')
dot.edge('velocity','valve_B1')
dot.edge('gradient','velocity')
dot.edge('stock_A','valve_A1',constraint='false')
dot.edge('stock_A','valve_B2',constraint='false')

# Render the SDD
dot.format = 'png'  # You can also use 'pdf', 'svg', 'jpg', etc.
dot.render('system_dynamics_diagram', view=True)

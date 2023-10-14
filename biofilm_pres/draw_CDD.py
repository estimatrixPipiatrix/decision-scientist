import graphviz

# Create the Causal Decision Diagram (CDD)
dot = graphviz.Digraph()

dot.attr(rankdir='LR')
dot.attr('node',shape='rectangle',style='filled',fillcolor='white')

# Define decision levers (actions)
with dot.subgraph(name='cluster_actions') as actions:
    actions.attr(rank="same",style="filled")
    actions.attr(label="levers",shape="box")
    actions.node('pressure', 'pressure differential')
    actions.node('filter_design', 'filter design')
    actions.node('maintenance', 'optimize maintenance')
    actions.node('chemical','chemical treatment')

# Define external constraints
with dot.subgraph(name='cluster_constraints') as constraints:
    constraints.attr(rank='same',style="filled")
    constraints.attr(label='externals', shape='box')
    constraints.node('budget', 'budget constraints')
    constraints.node('EPA','EPA requirements')

# Define intermediate processes
with dot.subgraph(name='cluster_intermed') as intermed:
    intermed.attr(rank="same",style="filled")
    intermed.attr(label='intermediates',shape='box')
    intermed.node('operation','operation cost')
    intermed.node('flushing','flushing rate')
    intermed.node('cleaning','cleaning time')
    intermed.node('parts','machine parts')
    intermed.node('longevity','system longevity')

# Define measurable outcomes
with dot.subgraph(name='cluster_outcomes') as outcomes:
    outcomes.attr(rank='same',style='filled')
    outcomes.attr(label='outcomes',shape='box')
    outcomes.node('cost', \
                  'total cost')
    outcomes.node('flow_rate', \
                  'volumetric flow rate')

# Add edges to show causal relationships
dot.edge('pressure','flushing',label='SD',color='blue')
dot.edge('pressure','operation')
dot.edge('cleaning','operation')
dot.edge('chemical','cleaning')
dot.edge('EPA','cleaning',color='red')
dot.edge('flushing','flow_rate')
dot.edge('parts','operation')
dot.edge('operation','cost')
dot.edge('filter_design','parts')
dot.edge('maintenance','parts',label='MC',color='blue')
dot.edge('chemical','flushing')
dot.edge('parts','longevity',label='ML',color='blue')
dot.edge('longevity','operation')
dot.edge('pressure','longevity')
dot.edge('budget','flushing',color='red')
dot.edge('budget','cleaning',color='red')
dot.edge('budget','parts',color='red')

# Render the CDD
dot.format = 'png'  # You can also use 'pdf', 'svg', 'jpg', etc.
dot.render('causal_decision_diagram', view=True)

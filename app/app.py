from dash import Dash, html, dcc, State, Input, Output, exceptions  # pip install dash
import dash_bootstrap_components as dbc   # pip install dash-bootstrap-components
import dash
import pickle
import matplotlib      # pip install matplotlib
matplotlib.use('agg')
import base64
from io import BytesIO
from tianshou.data import Batch
import environment, observation
from trained_agent import agent_learned

env = environment._get_env()
obs = env.env.last()[0]

with open('app/store/env.pkl', 'wb') as outp:
    pickle.dump(env, outp, pickle.HIGHEST_PROTOCOL)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("9qumalaq app", className='mb-2', style={'textAlign':'center'}),
    html.Button('Make action', id='human-act', n_clicks=0),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='human-action',
                value='Please select action',
                clearable=False,
                options=[i for i in range(9) if obs['action_mask'][i]])
        ], width=3)
    ]),
    html.Button('Make agents action', id='agent-act', n_clicks=0),
    dcc.Store(id='session-env', storage_type='session'),
    dbc.Row([
        dbc.Col([
            html.Img(id='bar-graph-matplotlib-human')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.Img(id='bar-graph-matplotlib-agent')
        ], width=12)
    ]),
])



# Create interactivity between dropdown component and graph
@app.callback(
    Output(component_id='bar-graph-matplotlib-human', component_property='src'),
    [Input('human-act', 'n_clicks'),
     Input('human-action', 'value')]
)

def make_human_action(n_clicks, human_act):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    print('changed_id', changed_id)
    with open('app/store/env.pkl', 'rb') as inp:
        env = pickle.load(inp)
    obs, rew, term, trunc, info = env.env.last()

    if 'human-act.n_clicks' in changed_id and n_clicks > 0:
        print('human_act', human_act)
        print('n_clicks', n_clicks)
        next_obs = env.step(human_act)[0]
        next_obs['observation'] = next_obs['obs']
        next_obs['action_mask'] = next_obs['mask']
        obs = next_obs
    with open('app/store/env.pkl', 'wb') as outp:
        pickle.dump(env, outp, pickle.HIGHEST_PROTOCOL)
    tuzdyq = obs['observation'][18:20]
    otaular = list(obs['observation'][:18])

    qazandar = obs['observation'][20:]
    fig = observation.render(otaular=otaular, tuzdyq=tuzdyq, qazandar=qazandar)

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

@app.callback(
    Output(component_id='bar-graph-matplotlib-agent', component_property='src'),
    [Input('agent-act', 'n_clicks')],
    prevent_initial_call=True
)

def make_agent_action(n_clicks):
    if n_clicks == 0:
        raise exceptions.PreventUpdate
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    with open('app/store/env.pkl', 'rb') as inp:
        env = pickle.load(inp)
    obs, rew, term, trunc, info = env.env.last()
    agent = env.env.agent_selection
    if 'agent-act' in changed_id:
        batch = Batch(obs=Batch(agent_id=agent, obs=[obs['observation']], mask=[obs['action_mask']]), info='?')
        agent_learned.eval()
        logits = agent_learned(batch=batch)['logits'].detach().numpy()
        max_val = -1e+21
        action = -1
        for idx, logit in enumerate(logits[0]):
            if max_val < logit and obs['action_mask'][idx]:
                max_val = logit
                action = idx
        next_obs, rewards, term, trunc, _ = env.step(action)
        next_obs['observation'] = next_obs['obs']
        next_obs['action_mask'] = next_obs['mask']
        obs = next_obs
    with open('app/store/env.pkl', 'wb') as outp:
        pickle.dump(env, outp, pickle.HIGHEST_PROTOCOL)
    tuzdyq = obs['observation'][18:20]
    otaular = list(obs['observation'][:18])

    qazandar = obs['observation'][20:]
    fig = observation.render(otaular=otaular, tuzdyq=tuzdyq, qazandar=qazandar)

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

if __name__ == '__main__':
    app.run_server(debug=True, port=8002)
from tianshou.policy import DQNPolicy
from tianshou.utils.net.common import Net
import torch
import environment

model = 95
env = environment._get_env()
net = Net(
            state_shape=(22,),
            action_shape=env.action_space.shape or env.action_space.n,
            hidden_sizes=[256, 512, 512, 256],
            device="cuda" if torch.cuda.is_available() else "cpu",
        ).to("cuda" if torch.cuda.is_available() else "cpu")

agent_learned = DQNPolicy(
            model=net,
            optim=torch.optim.Adam(net.parameters(), lr=1e-4),
            discount_factor=0.9,
            estimation_step=3,
            target_update_freq=320,
            action_space=env.action_space
        ).to("cuda" if torch.cuda.is_available() else "cpu")

agent_learned.load_state_dict(
    torch.load(f"./models/qostaushy/policy_dqn_256x512x512x256_{model}.pth")
)

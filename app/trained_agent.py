from tianshou.policy import DQNPolicy
from tianshou.utils.net.common import Net
import torch
import environment

model = 0
env = environment._get_env()
net = Net(
            state_shape=(23,),
            action_shape=env.action_space.shape or env.action_space.n,
            hidden_sizes=[2048,4096,4096,2048],
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
    torch.load(f"trained_models/dqn/policy_dqn_2048x4096x4096x2048_4.pth")
)

import gym
import util
env = gym.make("Acrobot-v1")
obs = env.reset()
R = 0
while True:
    util.render(env)
    action = -1 if obs[4] < 0 else 0
    obs, reward, done, info = env.step(action)
    R += reward
    if done:
        util.render(env)
        print(R)
        break

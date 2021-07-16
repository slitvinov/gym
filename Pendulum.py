import gym
import util

env = gym.make("Pendulum-v0")
obs = env.reset()
R = 0
while True:
    util.render(env)
    action = -9*obs[1] - 2*obs[2] if obs[0] > 0 else obs[2]
    obs, reward, done, info = env.step([action])
    R += reward
    if done:
        util.render(env)
        print(R)
        break


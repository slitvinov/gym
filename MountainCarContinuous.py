import gym
import util
env = gym.make("MountainCarContinuous-v0")
obs = env.reset()
R = 0
while True:
    util.render(env)
    action = -1 if obs[1] < 0 else 1
    obs, reward, done, info = env.step([action])
    R += reward
    if done:
        util.render(env)
        print(R)
        break

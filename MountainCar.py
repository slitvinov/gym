import gym
import util
env = gym.make("MountainCar-v0")
obs = env.reset()
R = 0
while True:
    util.render(env)
    action = 2 if obs[1] > 0 else 0
    obs, reward, done, info = env.step(action)
    R += reward
    if done:
        util.render(env)
        print(R)
        break

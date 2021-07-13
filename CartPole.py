import gym
import random
env = gym.make("CartPole-v1")
obs = env.reset()
R = 0
while True:
    env.render()
    action = 0 if obs[2] + obs[3] < 0 else 1
    obs, reward, done, info = env.step(action)
    R += reward
    if done:
        print(R)
        break

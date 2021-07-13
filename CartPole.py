import gym
import util
env = gym.make("CartPole-v1")
obs = env.reset()
R = 0
while True:
    util.render(env)
    action = 0 if 2 * obs[2] + obs[3] < 0 else 1
    obs, reward, done, info = env.step(action)
    R += reward
    if done:
        util.render(env)
        print(R)
        break

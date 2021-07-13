import gym
env = gym.make("MountainCar-v0")
obs = env.reset()
R = 0
while True:
    env.render()
    action = 0 if obs[1] < 0 else 2
    obs, reward, done, info = env.step(action)
    R += reward
    if done:
        print(R)
        break

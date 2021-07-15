import gym
import util

'''
                  s[0] is the horizontal coordinate
                  s[1] is the vertical coordinate
                  s[2] is the horizontal speed
                  s[3] is the vertical speed
                  s[4] is the angle
                  s[5] is the angular speed
                  s[6] 1 if first leg has contact, else 0
                  s[7] 1 if second leg has contact, else 0
'''                  

env = gym.make("LunarLander-v2")
obs = env.reset()
R = 0
while True:
    util.render(env)
    action = 0
    obs, reward, done, info = env.step(action)
    print(*obs[:2])
    R += reward
    if done:
        util.render(env)
        print(R)
        break


import random
import gym

env = gym.make('FrozenLake-v0')

# 4x4 grid info
print(env.observation_space)

# 4 directoins 0-3(left, down, right, up)
print(env.action_space)

score = 0
for i in range(10000):
    env.reset()
    for _ in range(1000):
        action = env.action_space.sample()  # random action
        observation, reward, done, info = env.step(random.randint(1, 2))
        env.render()  # displays environment

        if done:
            score += reward
            break
print(score)

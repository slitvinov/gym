<H2>Heuristic solutions for classic control problems in OpenAI Gym</H2>

<a href="/slitvinov/gym/blob/main/Acrobot.py">Acrobot-v1</a>: Swing up a two-link robot<br>
<a href="/slitvinov/gym/blob/main/CartPole.py">CartPole-v1</a>: Balance a pole on a cart<br>
<a href="/slitvinov/gym/blob/main/MountainCar.py">MountainCar-v0</a>: Drive up a big hill<br>
<a href="/slitvinov/gym/blob/main/Pendulum.py">Pendulum-v0</a>: Swing up a pendulum<br>
<a href="/slitvinov/gym/blob/main/MountainCarContinuous.py">MountainCarContinuous-v0</a>: Drive up a big hill with continuous control<br>

<PRE>
$ while python Acrobot.py; do :; done
-76.0
-75.0
-102.0
-80.0
-77.0
-103.0
-115.0
-75.0
-77.0
-75.0
  C-c
</PRE>

<PRE>
$ while python MountainCar.py ; do :; done
-121.0
-114.0
-118.0
-115.0
-121.0
-113.0
-114.0
  C-c
</PRE>

<p align="center"><img src="img/Acrobot.gif"/></p>
<p align="center"><img src="img/CartPole.gif"/></p>
<p align="center"><img src="img/MountainCar.gif"/></p>
<p align="center"><img src="img/Pendulum.gif"/></p>

<H2>Install</H2>
<PRE>
$ python -m pip install gym
</PRE>

<H2>References</H2>
https://gym.openai.com/envs/#classic_control

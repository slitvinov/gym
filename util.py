import os
def render_ppm(env):
    self = render_ppm
    array = env.render(mode='rgb_array')
    if not hasattr(self, "cnt"):
        self.cnt = 0
    else:
        self.cnt += 1
    path = "%05d.ppm" % self.cnt
    m, n, dim = array.shape
    with open(path, "wb") as file:
        file.write(b"P6\n%d %d\n255\n" % (n, m))
        file.write(array.tobytes())
    return array

def render_none(env):
    return env.render()

def render(env):
    return render_ppm(env) if "PPM" in os.environ else render_none(env)

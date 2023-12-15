class ChaosTrigPlot:

    def __init__(self, font_size, plot_width, plot_height, start, end, samples, frames, filenum, home_dir):
        self.fz = font_size
        self.pw = plot_width
        self.ph = plot_height
        self.a = start
        self.b = end
        self.u = samples
        self.z = frames
        self.fn = filenum
        self.home_dir = home_dir

    def fplot(self):
        import matplotlib.pyplot as plt
        import warnings as w
        import numpy as np
        import os
        import gc

        w.filterwarnings('ignore')
        plt.rcParams.update({'font.size': self.fz})
        plt.figure(figsize=(self.pw, self.ph))
        plt.tight_layout()

        p = []
        q = []
        interval = np.linspace(self.a / self.z, self.b / self.z, self.u)
        for s in interval:
            q.append(s)
            # p.append(np.sin((1-s)/s))
            # p.append(2*np.cos(s/(1-s))*np.sin(1/s))
            # p.append(1/s*np.sin(1/s) + 1/s*np.cos(1/s))
            # p.append(np.sin((1/s)*(1/(1-s))))
            # p.append(np.sin((1/(s)*(100/(1-s)))))
            # p.append(2*np.sin(3/s) + np.cos(5/s) + 4*np.sin(6/s) + np.cos(3/s))
            p.append(np.sin(3/s)*np.sin(5/(1-s)))
            # p.append(np.sin(1/s)+2*np.sin(1/(1-s)))
            # p.append(np.cos(1/s)**3 - 2*np.cos(s)*np.sin(s) - np.sin(1/s)**5)
            # p.append(np.cos(1/s)**3 - np.sin(1/s)**2 - np.cos(s)*np.sin(s))
            # p.append(np.sin(1 / (1 - s)) - np.cos(1 / s) * np.sin(1 / s ** 3))
            # p.append(np.abs(np.sin(1/s**3) + np.cos(1/s**5)))

        if self.fn % 2 == 1:
            outputfile = str(self.fn) + '.svg'
            plt.plot(q, p, color='blue')
            plt.title('fplot', fontsize=9)
            plt.ticklabel_format(useOffset=False)
            os.chdir(self.home_dir)
            plt.savefig(outputfile, format='svg', dpi=1200)
            plt.clf()
            gc.collect()

        elif self.fn % 2 == 0:
            outputfile = str(self.fn) + '.svg'
            plt.plot(q, p, color='blue')
            plt.title('fplot', fontsize=9)
            plt.ticklabel_format(useOffset=False)
            os.chdir(self.home_dir)
            plt.savefig(outputfile, format='svg', dpi=1200)
            plt.clf()
            gc.collect()

    @staticmethod
    def random_colour():
        import random
        colours = ['lime', 'orange', 'cyan', 'blue', 'red', 'purple', 'lightblue', 'purple']
        return random.choice(colours)


class LogisticMap:

    def __init__(self, font_size, plot_width, plot_height, plot_number, steps, factor, x1, y1, home_dir):
        self.fz = font_size
        self.pw = plot_width
        self.ph = plot_height
        self.pn = plot_number
        self.s = steps
        self.r = factor
        self.x1 = x1
        self.y1 = y1
        self.home_dir = home_dir

    def growth(self):
        import matplotlib.pyplot as plt
        import numpy as np
        import warnings as w
        import os
        import uuid

        w.filterwarnings('ignore')
        plt.rcParams.update({'font.size': self.fz})
        fig, ax = plt.subplots(self.pn, figsize=(self.pw, self.ph))
        plt.tight_layout()

        for j in range(self.pn):
            x = np.zeros(self.s + 1)
            y = np.zeros(self.s + 1)
            x[0], y[0] = self.x1, self.y1
            for k in range(self.s):
                y[k + 1] = self.r * y[k] * (1 - y[k])
                # print fixed points
                if np.round(y[k + 1], 3) == np.round(y[k], 3):
                    if y[k - 1] != y[k]:
                        print(k, round(self.r, 3), np.round(y[k], 3))
                x[k + 1] = x[k] + 1
            ax[j].plot(x, y, color=LogisticMap.random_colour(), linewidth=1.0)
            ax[j].set_title("%s" % np.round(self.r, 2), fontsize=6, fontweight='bold')
            ax[j].yaxis.get_offset_text().set_visible(False)
            self.r = self.r + 0.1
        outputfile = str(uuid.uuid4()) + '.png'
        os.chdir(self.home_dir)
        plt.savefig(outputfile, format='png', dpi=1200)

    @staticmethod
    def random_colour():
        import random
        colours = ['lime', 'orange', 'cyan', 'blue', 'red', 'purple', 'lightblue', 'purple']
        return random.choice(colours)

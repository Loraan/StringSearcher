import matplotlib.pyplot as plt


class GraphPainter:
    def __init__(self, data_x, data_y, deviation, title, x_label, y_label):
        self.title = title
        self.data_x = data_x
        self.data_y = data_y
        self.deviation = deviation
        self.x_label = x_label
        self.y_label = y_label
        self.plt = plt
        self.fig, self.axes = self.plt.subplots()

    def make_graph(self):
        self.plt.gcf()
        self.plt.title(self.title)
        self.plt.xlabel(self.x_label, color='gray')
        self.plt.ylabel(self.y_label, color='gray')
        self.plt.grid()
        self.axes.plot(self.data_x, self.data_y['BF'], 'rd')
        self.axes.plot(self.data_x, self.data_y['KMP'], 'g*')
        self.axes.plot(self.data_x, self.data_y['RK'], 'bX')
        self.axes.plot(self.data_x, self.data_y['BM'], 'ms')
        self.axes.plot(self.data_x, self.data_y['BMH'], 'co')
        legend_deviation = self.plt.legend(list(self.deviation.values()),
                                           loc=4, title='Deviation',
                                           fontsize=6, title_fontsize=8)
        self.plt.gca().add_artist(legend_deviation)
        self.plt.legend(list(self.data_y.keys()), loc=2,
                        title='Algorithms', fontsize=6, title_fontsize=8)

    def run(self):
        self.make_graph()
        self.plt.show()
from graphs.graph_painter import GraphPainter
from graphs.graph_maker import GraphFormer
from pathlib import Path
import datetime
import json


def save_results(dir_name, file_name, new_data, graph=None):
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    file_name = Path.cwd() / dir_name / file_name
    dir_path = Path.cwd() / dir_name
    if not Path.exists(dir_path):
        Path.mkdir(dir_path)
    if not Path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump({}, file)
    with open(file_name, 'r') as file:
        saved_data = json.load(file)
    saved_data[time_now] = new_data
    with open(file_name, 'w') as file:
        json.dump(saved_data, file)
    if graph is not None:
        if 'Memory' in graph.title:
            pic_name = dir_name + '\\mem-' + time_now + '.png'
        else:
            pic_name = dir_name + '\\time-' + time_now + '.png'
        graph.fig.savefig(pic_name)


def get_graphs(graph_type):
    graph_data = {'mem': ['memory_tests_data.json',
                          'Memory By Substring Length',
                          'Substring Length',
                          'Memory [Mb]'],
                  'time': ['time_tests_data.json',
                           'Time By Substring Length',
                           'Substring Length',
                           'Time [ms]']
                  }
    former = GraphFormer(graph_type)
    test_y_data, deviation = former.run()
    test_x_data = list(range(16))
    gp = GraphPainter(test_x_data, test_y_data, deviation,
                      graph_data[graph_type][1],
                      graph_data[graph_type][2],
                      graph_data[graph_type][3])
    gp.run()
    save_results('saved_results',
                 graph_data[graph_type][0],
                 test_y_data, gp)

from algorithms import *
import time
import argparse
from logs_parser import parser
from memory_profiler import profile
from graphs.graph_saver import get_graphs


def inp():
    parse = argparse.ArgumentParser(description='Substring Searcher')
    parse.add_argument("-t", "--time", dest="time",
                       help="Checking and output of the algorithm "
                            "operation time",
                       action="store_true")
    parse.add_argument("-m", '--memory', dest='memory',
                       help="Checking and outputting "
                            "in logs.txt and console used memory",
                       action="store_true")
    parse.add_argument("-s", '--string', dest='string',
                       help="Enables input text (by default text "
                            "in a file text.txt)",
                       type=str)
    parse.add_argument("substring",
                       help='Input substring for search')
    parse.add_argument("-mg", '--memorygraph', dest='memorygraph', action='store_true', help='Give a memory usage graph')
    parse.add_argument("-tg", '--timegraph', dest='timegraph', action='store_true', help='Give a time usage graph')
    return parse


def check_memory(text, substring, list_algo):
    logs_file = open('logs.txt', 'w+')
    for algo in list_algo:
        algorithm = algo(text, substring)
        profile(algorithm.run(), logs_file)
    logs_file.close()
    return parser()


def check_time(text, substring, list_algo):
    result = []
    for algo in list_algo:
        start = time.time()
        answer = algo(text, substring).run()
        finish = time.time()
        time_ms = round((finish - start) * 1000)
        result.append([answer, time_ms])
    return result


def print_result(result, time_f, memory):
    names = [
        'Brute Force',
        'Knuth Morris Pratt',
        'Rabin Karp',
        'Boyer Moore',
        'Boyer Moore Horspul']
    for i in range(len(result)):
        if time_f:
            if len(memory) == 0:
                print(f'Name: {names[i]}, '
                      f'Position: {result[i][0]}, '
                      f'Time: {result[i][1]} ms')
            else:
                print(f'Name: {names[i]}, '
                      f'Position: {result[i][0]}, '
                      f'Time: {result[i][1]} ms, '
                      f'Memory: {memory[i]} MiB')
        else:
            if len(memory) == 0:
                print(f'Name: {names[i]}, '
                      f'Position: {result[i][0]}')
            else:
                print(f'Name: {names[i]}, '
                      f'Position: {result[i][0]}, '
                      f'Memory: {memory[i]} MiB')


def execute_graphs(graph_type):
    print(f'Рисуем график по ' +
          f'{"памяти" if graph_type == "mem" else "времени"}...')
    get_graphs(graph_type)


if __name__ == '__main__':
    argument = inp().parse_args()
    substring = argument.substring
    time_f = argument.time
    memory_f = argument.memory
    string = argument.string
    memorygraph = argument.memorygraph
    timegraph = argument.timegraph
    memory = []
    list_algo = [
        BruteForce,
        KnuthMorrisPratt,
        RabinKarp,
        BoyerMoore,
        BoyerMooreHorspul]
    if string is None:
        with open('text.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            result = check_time(text, substring, list_algo)
            if memory_f:
                memory = check_memory(text, substring, list_algo)
            if memorygraph:
                get_graphs('mem')
            if timegraph:
                get_graphs('time')
            print_result(result, time_f, memory)
    else:
        result = check_time(string, substring, list_algo)
        if memory_f:
            memory = check_memory(string, substring, list_algo)
        print_result(result, time_f, memory)
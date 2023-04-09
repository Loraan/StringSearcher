from algorithms import BruteForce as BF, \
    KnuthMorrisPratt as KMP, \
    RabinKarp as RK, \
    BoyerMoore as BM, \
    BoyerMooreHorspul as BMH
import random

class InformationContainer:
    def __init__(self, name):
        self.name = name
        self.memory_data = []
        self.time_data = []
        self.average_deviation_time = 0
        self.average_deviation_data = 0

    def add_data(self, time, memory):
        self.time_data.append(time)
        self.memory_data.append(memory)

    def get_data(self, data_type):
        if data_type == 'mem':
            return {self.name: self.memory_data}
        else:
            return {self.name: self.time_data}

    def calculate_deviation(self, data_type):
        if data_type == 'mem':
            measure_results = self.memory_data
        else:
            measure_results = self.time_data
        n = len(measure_results)
        m = sum(measure_results) / n
        deviation = sum([(x - m)**2 for x in measure_results]) / n
        return deviation


class GraphFormer:
    def __init__(self, test_type,
                 test_text='text.txt',
                 substring_start_pos=50512):
        with open(test_text, encoding='utf-8') as file:
            self.text = file.read()
        start = substring_start_pos
        self.substrings = []
        for i in range(16):
            c = random.randint(0, 100000)
            self.substrings.append(self.text[c:c + 1000*i + 1])
        self.test_type = test_type

    def run(self, loops_count=10):
        data = {'BF': InformationContainer('BF'), 'KMP': InformationContainer('KMP'),
                'RK': InformationContainer('RK'), 'BM': InformationContainer('BM'), 'BMH': InformationContainer('BMH')}
        deviation = {}
        for i in range(16):
            time, memory = BF(self.text, self.substrings[i]).test(loops_count)
            data['BF'].add_data(time, memory)
            time, memory = KMP(self.text, self.substrings[i]).test(loops_count)
            data['KMP'].add_data(time, memory)
            time, memory = RK(self.text, self.substrings[i]).test(loops_count)
            data['RK'].add_data(time, memory)
            time, memory = BM(self.text, self.substrings[i]).test(loops_count)
            data['BM'].add_data(time, memory)
            time, memory = BMH(self.text, self.substrings[i]).test(loops_count)
            data['BMH'].add_data(time, memory)
        for alg in data.keys():
            deviation[alg] = f'{data[alg].calculate_deviation(self.test_type):.2e}'
        return ({**data['BF'].get_data(self.test_type),
                 **data['RK'].get_data(self.test_type),
                 **data['KMP'].get_data(self.test_type),
                 **data['BM'].get_data(self.test_type),
                 **data['BMH'].get_data(self.test_type)}, deviation)

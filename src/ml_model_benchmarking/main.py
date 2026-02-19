import time
import numpy as np
import matplotlib.pyplot as plt

class ModelBenchmark:
    def __init__(self, model):
        self.model = model

    def benchmark(self, data):
        start_time = time.time()
        self.model.predict(data)
        return time.time() - start_time

    def visualize_results(self, results):
        plt.plot(results)
        plt.title('Model Performance Benchmarking')
        plt.xlabel('Model')
        plt.ylabel('Time (seconds)')
        plt.show()
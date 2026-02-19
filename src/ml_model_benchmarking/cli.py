import argparse
from .main import ModelBenchmark

def main():
    parser = argparse.ArgumentParser(description='Benchmark ML models.')
    parser.add_argument('model', help='The ML model to benchmark')
    parser.add_argument('data', help='Data for benchmarking')
    args = parser.parse_args()

    model = # Load or instantiate model based on args.model
    data = # Load or prepare data based on args.data
    benchmark = ModelBenchmark(model)
    time_taken = benchmark.benchmark(data)
    print(f'Time taken: {time_taken} seconds')
import algorithm
import importlib
from pathlib import Path


algo_path = Path("./algorithms")

for f in algo_path.iterdir():
    if f.suffix == ".py":
        importlib.import_module(f"algorithms.{f.stem}")


algo1 = algorithm.get_algo("algo1")
algo2 = algorithm.get_algo("Algo2")

...

from abc import ABC
from typing import Dict, Type


class Tensor:
    ...


class IAlgorithm(ABC):
    _all_algorithms: Dict[str, Type["IAlgorithm"]] = {}

    def forward(self, x: Tensor) -> Tensor:
        ...


def register_algo_auto_name(cls: Type[IAlgorithm]):
    IAlgorithm._all_algorithms[cls.__name__] = cls
    return cls


def register_algo(name: str):
    def _wrapper(cls: Type[IAlgorithm]):
        IAlgorithm._all_algorithms[name] = cls
        return cls

    return _wrapper


def get_algo(algo_name: str, *args, **kwargs) -> IAlgorithm:
    # _dict: Dict[str, Type[Algorithm]] = {"algo1": Algo1, "algo2": Algo2}
    _dict = IAlgorithm._all_algorithms
    return _dict[algo_name](*args, **kwargs)

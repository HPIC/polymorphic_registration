import inspect
import importlib
from pathlib import Path
from typing import Generic, TypeVar, Type, Dict, List


T = TypeVar("T")


class ModuleGetter(Generic[T]):
    def __init__(self, module_name: str, type: Type[T]) -> None:
        super().__init__()
        self._m_name = module_name
        self._t = type
        self._dict: Dict[str, Type[T]] = {}

        submodule_path = Path(module_name)
        if not submodule_path.exists():
            raise ValueError(f"Module {module_name} does not exist.")

        for f in submodule_path.iterdir():
            if f.suffix != ".py":
                continue
            module = importlib.import_module(f"{module_name}.{f.stem}")

            for name, cls in inspect.getmembers(module):
                if inspect.isclass(cls) and issubclass(cls, type):
                    self._dict[name] = cls

    def get(self, name: str, **kwargs) -> T:
        cls = self._dict.get(name)
        if not cls:
            raise ValueError(f"Invalid module name {name}")

        return cls(**kwargs)

    def registered_classes(self) -> List[str]:
        return list(self._dict.keys())


def test():
    import algorithm

    m = ModuleGetter("algorithms", algorithm.IAlgorithm)
    assert issubclass(type(m.get("Algo1")), algorithm.IAlgorithm)


if __name__ == "__main__":
    test()

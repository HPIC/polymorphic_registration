from algorithm import IAlgorithm, register_algo_auto_name, register_algo, Tensor


@register_algo("algo1")
class Algo1(IAlgorithm):
    def forward(self, x: Tensor) -> Tensor:
        return super().forward(x)
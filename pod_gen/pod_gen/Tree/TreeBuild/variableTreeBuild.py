from .pod_gen.Tree.BranchNodes.Sum import Sum
from .pod_gen.Tree.BranchNodes.Product import Product
from .pod_gen.Tree.BranchNodes.Power import Power
from .pod_gen.Tree.LeafNodes.Constant import Constant
from .pod_gen.Tree.LeafNodes.Variable import Variable
from .pod_gen.Tree.TreeBuild.randomNumber import randomNumber


def variableTreeBuild(power: int, name: str):
    if power == 1:
        return Product(Constant(randomNumber()),
                       Power(Variable(name),
                             Constant(power)))

    return Sum(Product(Constant(randomNumber()),
                       Power(Variable(name),
                             Constant(power))),
               variableTreeBuild(power - 1, name))

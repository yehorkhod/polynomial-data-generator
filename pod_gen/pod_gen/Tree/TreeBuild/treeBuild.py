from .pod_gen.Tree.LeafNodes.Constant import Constant
from .pod_gen.Tree.BranchNodes.Sum import Sum
from .pod_gen.Tree.TreeBuild.randomNumber import randomNumber
from .pod_gen.Tree.TreeBuild.baseTreeBuild import baseTreeBuild


def treeBuild(powers: list[int]):
    return Sum(Constant(randomNumber()),
               baseTreeBuild(powers))

from .graph_problem_interface import *
from .best_first_search import BestFirstSearch
from typing import Optional
import numpy as np


class GreedyStochastic(BestFirstSearch):
    def __init__(self, heuristic_function_type: HeuristicFunctionType,
                 T_init: float = 1.0, N: int = 5, T_scale_factor: float = 0.95):
        # GreedyStochastic is a graph search algorithm. Hence, we use close set.
        super(GreedyStochastic, self).__init__(use_close=True)
        self.heuristic_function_type = heuristic_function_type
        self.T = T_init
        self.N = N
        self.T_scale_factor = T_scale_factor
        self.solver_name = 'GreedyStochastic (h={heuristic_name})'.format(
            heuristic_name=heuristic_function_type.heuristic_name)

    def _init_solver(self, problem: GraphProblem):
        super(GreedyStochastic, self)._init_solver(problem)
        self.heuristic_function = self.heuristic_function_type(problem)

    def _open_successor_node(self, problem: GraphProblem, successor_node: SearchNode):
        """
        TODO: implement this method!
        """
        if self.open.has_state(successor_node.state):
            old_node = self.open.get_node_by_state(successor_node.state)
            if successor_node.expanding_priority < old_node.expanding_priority:
                self.open.extract_node(old_node)
                self.open.push_node(successor_node)
        elif self.close.has_state(successor_node.state):
            old_node = self.close.get_node_by_state(successor_node.state)
            if successor_node.expanding_priority < old_node.expanding_priority:
                self.close.remove_node(old_node)
                self.open.push_node(successor_node)
        else:
            self.open.push_node(successor_node)


    def _calc_node_expanding_priority(self, search_node: SearchNode) -> float:
        """
        TODO: implement this method!
        Remember: `GreedyStochastic` is greedy.
        """
        return self.heuristic_function.estimate(search_node.state)

    def _extract_next_search_node_to_expand(self) -> Optional[SearchNode]:
        """
        Extracts the next node to expand from the open queue,
         using the stochastic method to choose out of the N
         best items from open.
        TODO: implement this method!
        Use `np.random.choice(...)` whenever you need to randomly choose
         an item from an array of items given a probabilities array `p`.
        You can read the documentation of `np.random.choice(...)` and
         see usage examples by searching it in Google.
        Notice: You might want to pop min(N, len(open) items from the
                `open` priority queue, and then choose an item out
                of these popped items. The other items have to be
                pushed again into that queue.
        """
        best_N = []
        best_N_heuristics = []
        size = self.open.__len__()
        for _ in range((min(self.N, size))):
            temp = self.open.pop_next_node()
            best_N.append(temp)
            best_N_heuristics.append(self._calc_node_expanding_priority(temp))

        alpha = min(best_N_heuristics)

        def get_sum(t):
            sum = 0
            for x in best_N_heuristics:
                sum = sum + pow((x/alpha), (-1/t))
            return sum

        def get_probability(i, t):
            sum = get_sum(t)
            current = best_N_heuristics[i]/alpha
            return pow(current, (-1 / t))/sum

        P = []
        for i in range(len(best_N)):
            P.append(get_probability(i, self.T))

        self.T = self.T*self.T_scale_factor
        rand = (np.random.choice(a=best_N, size=1, p=P))[0]
        best_N.remove(rand)
        for _ in range(best_N.__len__()):
            self.open.push_node(best_N.pop())

        return rand
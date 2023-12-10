"""Some core module."""
import pandas as pd


class AbstractCalculator:

    def run(self):
        pass

class AbstractOptimizer:
    """Some Ruler."""

    def __init__(self):
        self.parameter = dict()
        self.objectives = dict()
        self.history = History()

    def add_parameter(self, name, init, lb, ub):
        self.parameter[name] = [init, lb, ub]

    def add_objective(self, name, fun):
        self.objectives[name] = fun

    def f(self, x):

        row = []
        row.extend(x)

        ret = []
        for key, value in self.objectives.items():
            ret.append(value(x))

        row.extend(ret)

        self.history.record(row)

        return ret


    def main(self):
        # optimize(objectives, parameters)
        pass



class History:
    """History of ruler"""
    def __init__(self):
        self._data = []
        self.data = pd.DataFrame()

    def record(self, row):
        self._data.append(row)
        self.data = pd.DataFrame(self._data)


class ProcessController:
    """Multi process controller"""
    def __init__(self):
        pass




import numpy as np

import optuna

from ray import tune
from ray.tune.search.optuna import OptunaSearch
from ray.tune.search.bayesopt import BayesOptSearch
from ray.air.config import RunConfig

from .core import AbstractOptimizer


class Ray(AbstractOptimizer):

    def _objective(self, config):
        param = []
        for name, _ in self.parameter.items():
            param.append(config[name])
        x = np.array(param)
        ret = self.f(x)
        return {"score": ret}

    def main(self):
        search_space = dict()
        for name, (init, lb, ub) in self.parameter.items():
            search_space[name] = tune.uniform(lb, ub)

        tuner = tune.Tuner(self._objective, param_space=search_space)

        tuner.fit()


class Optuna(AbstractOptimizer):

    def _objective(self, trial):
        param = []
        for key, (init, lb, ub) in self.parameter.items():
            param.append(trial.suggest_float(key, lb, ub))
        x = np.array(param)
        return tuple(self.f(x))


    def main(self, n_trials=10, method='TPE'):
        if method == 'TPE':
            sampler = optuna.samplers.TPESampler(n_startup_trials=10)
        elif method == 'botorch':
            sampler = optuna.integration.BoTorchSampler(n_startup_trials=10)

        study = optuna.create_study(
            sampler=sampler,
            directions=['minimize']*len(self.objectives),
        )

        study.optimize(
            func=self._objective,
            n_trials=n_trials,
        )

        return study

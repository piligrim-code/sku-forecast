from typing import List
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.linear_model import QuantileRegressor
from tqdm import tqdm


class MultiTargetModel:
    def __init__(
        self,
        features: List[str],
        horizons: List[int] = [7, 14, 21],
        quantiles: List[float] = [0.1, 0.5, 0.9],
    ) -> None:
        
        self.quantiles = quantiles
        self.horizons = horizons
        self.sku_col = "sku_id"
        self.date_col = "day"
        self.features = features
        self.targets = [f"next_{horizon}d" for horizon in self.horizons]

        self.fitted_models_ = {}

    def fit(self, data: pd.DataFrame, verbose: bool = False) -> None:
    model_dict = {}
    for sku in df_train['sku_id'].unique():
        for horizon in horizons:
                for quantile in quantiles:
                    df_train = df_train.dropna()
                    X_train = df_train.drop(columns=['next_7d', 'next_14d', 'next_21d', 'day', 'sku'], axis=True)
                    y_train = df_train[['next_7d', 'next_14d', 'next_21d']]
                    for target_column in ['next_7d', 'next_14d', 'next_21d']:
                            model = QuantileRegressor(quantile=quantile)
                            model.fit(X_train, y_train[target_column])
                            model_dict[f'{sku}_{horizon}_{quantile}'] = model

    def predict(self, data: pd.DataFrame) -> pd.DataFrame:
        return predictions
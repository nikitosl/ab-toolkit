import unittest

import numpy as np
import pandas as pd

from src.continuous.utils import estimate_mde_by_sample_size
from src.continuous.utils import estimate_sample_size_by_mde


class TestSampleSizeEstimation(unittest.TestCase):
    def test_calculate_sample_size_by_mde(self):
        sample_size = estimate_sample_size_by_mde(3, 0.05, 0.8, 2)
        self.assertTrue(isinstance(sample_size, int), f"Estimated sample size has wrong type: {sample_size}")
        self.assertTrue(sample_size > 0, f"Estimated sample size has negative value: {sample_size}")

    def test_calculate_mde_by_sample_size(self):
        mde = estimate_mde_by_sample_size(3, 0.05, 0.8, 36)
        self.assertTrue(isinstance(mde, float), f"Estimated MDE has wrong type: {mde}")

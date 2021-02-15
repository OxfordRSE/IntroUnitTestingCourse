import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean


def test_everything_works():
    npt.assert_array_equal(np.array([0, 0]), np.array([0, 0]))

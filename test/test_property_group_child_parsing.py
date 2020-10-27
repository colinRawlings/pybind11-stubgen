import pytest
import typing

import EmFdtdSimulator # TODO get test classes from XCore

from pybind11_stubgen import XCorePropertyGroupStubsGenerator

@pytest.mark.parametrize(
    "test_class, expected_result",
    [
        (EmFdtdSimulator.EmFdtdCurrentSensorSettings,
        ['@property', 'def SteadyStateCheck(self) -> XCore.PropertyEnum: ...', '', '@property', 'def ConvergenceLevel(self) -> XCore.PropertyReal: ...', '', '@property', 'def SamplesPerPeriod(self) -> XCore.PropertyInt: ...', '', '@property', 'def IsDirectionReverted(self) -> XCore.PropertyBool: ...', '', '@property', 'def IsInterpolated(self) -> XCore.PropertyBool: ...', ''] ),
        (EmFdtdSimulator.EmFdtdGlobalBoundarySettings, []) # cannot be constructed
    ])
def test_eval(test_class, expected_result: str):

    pg = XCorePropertyGroupStubsGenerator(test_class)

    pg.parse()
    result = pg.to_lines()

    print(result)

    assert result == expected_result
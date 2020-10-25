import pytest
import ast

from pybind11_stubgen import FunctionSignature as FS


@pytest.mark.parametrize(
    "boost_test_args, formatted_args",
    [
        (
            '(object)arg1 [, (float)value=0.0 [, (float)min=0.0 [, (float)max=1.0 [, (Unit)unit=Unit("", kNone)]]]]',
            'arg1: typing.Any, value: float = 0.0, min: float = 0.0, max: float = 1.0, unit: Unit = Unit("", kNone)',
        ),
        ("", ""),
        (
            "(Uuid)arg1, (object)self, byte_array",
            "arg1: Uuid, self: typing.Any, byte_array: typing.Any",
        ),
        (
            "[  (bool)use_mother_console=False [, (bool)visible=True]]",
            "use_mother_console: bool = False, visible: bool = True",
        ),
        (
             "[  (Color)color=Color(0.868925, 0.025000, 0.975000, 1.000000)]",
             "color: Color = Color(0.868925, 0.025000, 0.975000, 1.000000)"
        ),
        (
             "(object)self, (float)red, (float)green, (float)blue [, (float)alpha]",
             "self: typing.Any, red: float, green: float, blue: float, alpha: float"
        )
    ],
)
def test_eval(boost_test_args: str, formatted_args: str):

    ok, reformatted_args = FS._format_boost_doc_args(boost_test_args)

    assert reformatted_args == formatted_args
    assert ok

    function_def_str = "def {}({}) -> {}: ...".format(
        "a_func", reformatted_args, "bool"
    )
    ast.parse(function_def_str)
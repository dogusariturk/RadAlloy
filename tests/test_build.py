"""
tests/test_build.py

Exercises the wheel produced by radalloy’s build-hook to ensure the compiled
Nimplex extensions and plotting helpers are present and behave correctly,
using Python’s built-in ``unittest`` framework so it can run in any
environment where pytest is unavailable.

Run with:
    python -m unittest -v tests.test_build
"""

import importlib
import pathlib
import os
import unittest


def _bindings_dir():
    pkg = pathlib.Path(__file__).parent.parent
    return pkg / "src" / "radalloy" / "_bindings"


class BuildArtifactsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize the test class with necessary attributes."""
        cls.ext_suffix = ".so"
        cls.bindings_dir = _bindings_dir()

        # Try to import compiled modules once; reuse across tests
        cls.nimplex = importlib.import_module("radalloy._bindings.nimplex")
        cls.plotting = importlib.import_module("radalloy._bindings.plotting")

    def test_shared_objects_present(self):
        """Both compiled binaries should exist in _bindings/."""
        for name in ("nimplex", "plotting"):
            so_path = os.path.join(self.bindings_dir, f"{name}{self.ext_suffix}")
            self.assertTrue(
                os.path.exists(so_path),
                msg=f"missing shared object: {so_path}",
            )

    def test_importable(self):
        """Sanity-check imports."""
        self.assertTrue(self.nimplex.__name__.endswith("nimplex"))
        self.assertTrue(self.plotting.__name__.endswith("plotting"))

    def test_expected_functions_exist(self):
        expected = {
            "simplex_internal_grid_fractional_py",
            "simplex_sampling_mc_py",
        }
        missing = [fn for fn in expected if not hasattr(self.nimplex, fn)]
        self.assertFalse(missing, f"missing functions: {missing}")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

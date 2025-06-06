from __future__ import annotations

import pathlib
import shutil
import subprocess
import sysconfig

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

ROOT = pathlib.Path(__file__).parent
NIMPLEX_SRC = ROOT / "third_party" / "nimplex"
PLOT_SRC = NIMPLEX_SRC / "utils" / "plotting.nim"
PKG_DIR = ROOT / "src" / "radalloy" / "_bindings"
PKG_DIR.mkdir(parents=True, exist_ok=True)


class NimplexHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict) -> None:
        if self.target_name != "wheel":
            return

        subprocess.run(
            ["nimble", "install", "--depsOnly", "-y"],
            cwd=NIMPLEX_SRC,
            check=True,
        )

        out_core = NIMPLEX_SRC / f"nimplex.so"
        subprocess.run(
            [
                "nim",
                "c",
                "--threads:on",
                "-d:release",
                "--app:lib",
                f"--out:{out_core}",
                "nimplex",
            ],
            cwd=NIMPLEX_SRC,
            check=True,
        )

        out_plot = PLOT_SRC.parent / f"plotting.so"
        subprocess.run(
            [
                "nim",
                "c",
                "--threads:on",
                "-d:release",
                "--app:lib",
                f"--out:{out_plot}",
                str(PLOT_SRC),
            ],
            cwd=PLOT_SRC.parent,
            check=True,
        )

        forced = build_data.setdefault("force_include", {})

        for built in (out_core, out_plot):
            dst_path = PKG_DIR / built.name
            shutil.copy2(built, dst_path)
            src_rel = dst_path.relative_to(ROOT).as_posix()
            wheel_rel = f"radalloy/_bindings/{built.name}"
            forced[src_rel] = wheel_rel

"""Smoke test: the package imports and its entry point runs."""

import pytest

from taintline import main


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "taintline" in captured.out

from pathlib import Path

import numpy as np
import pandas as pd

from pygama.vis import WaveformBrowser

config_dir = Path(__file__).parent / "configs"


def test_waveform_browser(lgnd_test_data):
    wb = WaveformBrowser(
        lgnd_test_data.get_path("lh5/LDQTA_r117_20200110T105115Z_cal_geds_raw.lh5"),
        "/geds/raw",
        dsp_config=f"{config_dir}/hpge-dsp-config.json",
        lines=["wf_blsub", "wf_trap", "trapEmax"],
        legend=["waveform", "trapezoidal", "energy = {trapEmax:0.1f}"],
        styles="seaborn",
        n_drawn=2,
        x_lim=("20*us", "60*us"),
        x_unit="us",
    )

    wb.draw_next()
    wb.draw_entry(24)
    wb.draw_entry((2, 24))


def test_entry_mask(lgnd_test_data):
    selection = pd.Series(
        [
            False, False, False, False, False, False, False, True, False, True,
            False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, True, False, True, False,
            False, False, False, False, True, False, False, False, False, True,
            False, False, False, False, False, False, False, True, False,
            False, False, False, False, True, False, False, False, False, True,
            False, True, False, False, False, False, False, False, False, True,
            False, False, False, True, True, False, False, False, False, False,
            False, False, False, False, True, False, False, False, False,
            False, False, False, True, False, True, True, True, False, False,
            True, False, False]
    )
    wb = WaveformBrowser(
        lgnd_test_data.get_path("lh5/LDQTA_r117_20200110T105115Z_cal_geds_raw.lh5"),
        "/geds/raw",
        entry_mask=selection,
        n_drawn=5
    )

    wb.draw_next()

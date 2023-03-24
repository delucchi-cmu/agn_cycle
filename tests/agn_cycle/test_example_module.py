"""Test this shit."""

from dataclasses import dataclass, field

import pandas as pd

from agn_cycle import example_module


@dataclass
class AGN:
    """hold AGN data"""
    file: str = ""
    centroid: list[int] = field(default_factory=list)
    bristol_scale: int = 1


def test_read_bmp():
    """Verify the output of the `greetings` function"""

    agns = [
        AGN("/home/delucchi/bmp/001.bmp", [155, 195], 3),
        AGN("/home/delucchi/bmp/001.bmp", [307, 398], 3),
        AGN("/home/delucchi/bmp/002.bmp", [276, 233], 6),
        AGN("/home/delucchi/bmp/003.bmp", [227, 140], 6),
        AGN("/home/delucchi/bmp/004.bmp", [261, 260], 4),
        AGN("/home/delucchi/bmp/011.bmp", [375, 193], 6),
        AGN("/home/delucchi/bmp/012.bmp", [288, 231], 1),
        AGN("/home/delucchi/bmp/012.bmp", [239, 280], 3),
        AGN("/home/delucchi/bmp/013.bmp", [260, 283], 6),
        AGN("/home/delucchi/bmp/014.bmp", [210, 307], 4),
        AGN("/home/delucchi/bmp/021.bmp", [310, 260], 4),
        AGN("/home/delucchi/bmp/022.bmp", [354, 295], 7),
        AGN("/home/delucchi/bmp/023.bmp", [306, 312], 6),
        AGN("/home/delucchi/bmp/024.bmp", [259, 240], 7),
        AGN("/home/delucchi/bmp/031.bmp", [299, 202], 4),
        AGN("/home/delucchi/bmp/032.bmp", [92, 218], 7),
        AGN("/home/delucchi/bmp/033.bmp", [218, 343], 6),
        AGN("/home/delucchi/bmp/034.bmp", [221, 331], 4),
        AGN("/home/delucchi/bmp/041.bmp", [234, 230], 7),
        AGN("/home/delucchi/bmp/042.bmp", [199, 212], 3),
        AGN("/home/delucchi/bmp/042.bmp", [296, 255], 3),
        AGN("/home/delucchi/bmp/043.bmp", [236, 367], 4),
        AGN("/home/delucchi/bmp/044.bmp", [270, 201], 4),
    ]

    results = []
    for agn in agns:
        qtable = example_module.read_bmp(agn.file, centroid=agn.centroid)
        result = qtable.to_pandas()
        # result["file"] = agn.file
        result["bristol"] = agn.bristol_scale
        results.append(result)

    final = pd.concat(results, ignore_index=True, sort=False)
    print(final)

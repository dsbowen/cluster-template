import os
import sys

import pandas as pd

RESULTS_DIR = "results"

if __name__ == "__main__":
    sim_no, variable = sys.argv[1:]
    pd.DataFrame({"sim_no": [sim_no], "variable": [variable]}).to_csv(
        os.path.join(RESULTS_DIR, f"sim_no={sim_no}-variable={variable}.csv"),
        index=False
    )

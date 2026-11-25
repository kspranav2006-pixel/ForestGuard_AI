"""Central configuration for ForestGuard AI.

All paths, region bounds, dates and modelling constants live here so that
no other module hard-codes them.
"""
from pathlib import Path

# ---------------------------------------------------------------- paths
ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"
REPORTS_DIR = ROOT / "reports"

for _p in (DATA_RAW, DATA_PROCESSED, MODELS_DIR, REPORTS_DIR):
    _p.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------- study region
REGION_NAME = "Uttarakhand, India"
# Provisional bounding box: to be verified against a boundary file in Phase 2.
LAT_MIN, LAT_MAX = 28.7, 31.5
LON_MIN, LON_MAX = 77.5, 81.1

# ----------------------------------------------------------------- grid
GRID_RES_DEG = 0.1  # matches AgERA5 native resolution (to be confirmed)

# --------------------------------------------------------------- season
SEASON_START_MD = (2, 1)   # 1 February
SEASON_END_MD = (6, 30)    # 30 June
YEARS_ALL = list(range(2020, 2026))   # 2026 added in Phase 2 if data exists

# ------------------------------------------- provisional chronological split
# FIXED BEFORE MODEL TRAINING. Revisit only after checking fire counts per year
# in Phase 2, and never after seeing model results.
TRAIN_YEARS = [2020, 2021, 2022]
VAL_YEARS = [2023]
TEST_YEARS = [2024, 2025]

# --------------------------------------------------------------- target
PREDICTION_WINDOW_DAYS = 1  # fire on day D+1
RANDOM_STATE = 42

TARGET_COL = "fire_next_day"
from pathlib import Path

ROOT = Path(__file__).parent.parent

GEOLOGY_PATH = ROOT / "data/raw/SIM3292_Shapefiles/SIM3292_Global_Geology.shp"

MOSAIC_PATH = ROOT / "data/raw/Mars_Viking_MDIM21_Mosaic_global_232m.tif"

TILES_DIR = ROOT / "data/processed/tiles"

MANIFEST_PATH = ROOT / "data/processed/manifest.csv"

TILE_DEG = 1.0

PXLS_PER_DEG = 256

LAT_MIN = -45

LAT_MAX = 45

LON_MIN = -180

LON_MAX = 180

PERIODS = ["Noachian", "Hesperian", "Amazonian"]

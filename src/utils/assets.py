from pathlib import Path

class Assets:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("../../assets")

    @staticmethod
    def asset_path(path: str) -> Path:
        return Assets.ASSETS_PATH / Path(path)

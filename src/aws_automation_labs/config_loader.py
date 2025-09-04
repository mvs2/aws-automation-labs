from pathlib import Path
import yaml

def load_config(filename: str = "default.yaml") -> dict:
    """
    Load a YAML config file from the project's config directory.
    Defaults to 'default.yaml'.
    """
    # Go from this file → up 2 levels → into config/
    config_path = Path(__file__).resolve().parents[2] / "config" / filename
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

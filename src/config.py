import os
import json
import logging
from pathlib import Path
from src.data_types import Parameters
from src.data_types import SearchResult


def get_project_root() -> Path:
    """"""
    return Path(__file__).parent.parent


PROJECT_ROOT_DIR = get_project_root()

with open(os.path.join(PROJECT_ROOT_DIR, "data", "config.json"), "r") as jf:
    config_dict = json.load(jf)

parameters = Parameters.parse_obj(config_dict)


empty_result = SearchResult(templateId=0, templateText="", topic="", sbert_score=0.0, jaccard=0.0, entrance=False, best_etalon="").dict()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', )

logger = logging.getLogger()
logger.setLevel(logging.INFO)
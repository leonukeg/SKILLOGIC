import json
import os
from SKILLOGIC.data.lesson_1_1 import LESSON_1_1
from SKILLOGIC.data.lesson_1_2 import LESSON_1_2
from SKILLOGIC.data.lesson_1_3 import LESSON_1_3
from SKILLOGIC.data.lesson_1_4 import LESSON_1_4
from SKILLOGIC.data.lesson_1_5 import LESSON_1_5
from SKILLOGIC.data.lesson_2_1 import LESSON_2_1
from SKILLOGIC.data.lesson_2_2 import LESSON_2_2
from SKILLOGIC.data.lesson_2_3 import LESSON_2_3
from SKILLOGIC.data.lesson_2_4 import LESSON_2_4

DATA_FILE = os.path.join(os.path.dirname(__file__), "curriculum.json")

LESSONS_DB = {
    "lesson_1_1": LESSON_1_1,
    "lesson_1_2": LESSON_1_2,
    "lesson_1_3": LESSON_1_3,
    "lesson_1_4": LESSON_1_4,
    "lesson_1_5": LESSON_1_5,
    "lesson_2_1": LESSON_2_1,
    "lesson_2_2": LESSON_2_2,
    "lesson_2_3": LESSON_2_3,
    "lesson_2_4": LESSON_2_4,
}

def load_curriculum() -> dict:
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_curriculum(data: dict):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_lesson_by_id(lesson_id: str) -> dict | None:
    return LESSONS_DB.get(lesson_id)

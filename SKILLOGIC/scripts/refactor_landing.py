import os
import re

landing_path = r"c:\Users\Freddy\Desktop\Cosas_Python\SKILLOGIC\SKILLOGIC\pages\landing.py"
out_dir = r"c:\Users\Freddy\Desktop\Cosas_Python\SKILLOGIC\SKILLOGIC\components\landing"

with open(landing_path, "r", encoding="utf-8") as f:
    content = f.read()

# We need the imports for the new files
imports = """import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
from SKILLOGIC.components.landing.helpers import t
"""

# Extract the t helper
t_match = re.search(r'(def t\(es: str, en: str\) -> rx\.Component:.*?)(?=def )', content, re.DOTALL)
if t_match:
    with open(os.path.join(out_dir, "helpers.py"), "w", encoding="utf-8") as f:
        f.write("import reflex as rx\nfrom SKILLOGIC.state.app_state import AppState\n\n" + t_match.group(1))

# Mapping of function names to filenames
file_map = {
    "landing_navbar": "navbar.py",
    "hero_section": "hero.py",
    "stats_section": "stats.py",
    "problem_solution_section": "problem_solution.py",
    "features_section": "features.py",
    "how_it_works_section": "how_it_works.py",
    "testimonials_section": "testimonials.py",
    "faq_section": "faq.py",
    "bottom_cta_section": "cta.py",
    "footer": "footer.py"
}

new_landing_content = """import reflex as rx
from SKILLOGIC.styles import theme as T
from SKILLOGIC.state.app_state import AppState
"""

for func, filename in file_map.items():
    # Find the function
    pattern = rf"(def {func}\(.*?)(?=def \w|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        func_content = match.group(1)
        # Write to file
        with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
            f.write(imports + "\n" + func_content)
        # Add import to new landing
        new_landing_content += f"from SKILLOGIC.components.landing.{filename[:-3]} import {func}\n"

# Add the landing_page function
lp_match = re.search(r'(def landing_page\(\) -> rx\.Component:.*?)\Z', content, re.DOTALL)
if lp_match:
    new_landing_content += "\n" + lp_match.group(1)

with open(landing_path, "w", encoding="utf-8") as f:
    f.write(new_landing_content)

print("Landing refactor complete!")

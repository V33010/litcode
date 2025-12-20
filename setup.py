import re
import sys
from pathlib import Path

# ---------------- CONFIG ----------------
VALID_DIFFICULTIES = {"easy", "medium", "hard"}
PROBLEMS_DIR = Path("problems")
# ---------------------------------------


def exit_with_error(msg: str):
    print(f"Error: {msg}")
    sys.exit(1)


def main():
    # --------------------------------------------------
    # 1. Strict argument count check
    # --------------------------------------------------
    if len(sys.argv) != 4:
        exit_with_error(
            "Usage: python setup.py <difficulty> <question_number> <problem_name>"
        )

    _, difficulty, question_number, problem_name = sys.argv

    # --------------------------------------------------
    # 2. Validate difficulty
    # --------------------------------------------------
    if difficulty not in VALID_DIFFICULTIES:
        exit_with_error(
            f"Invalid difficulty '{difficulty}'. Must be one of {VALID_DIFFICULTIES}."
        )

    # --------------------------------------------------
    # 3. Validate question number (must be digits)
    # --------------------------------------------------
    if not question_number.isdigit():
        exit_with_error("Question number must contain digits only.")

    # --------------------------------------------------
    # 4. Validate problem name
    #    Allowed: A-Z a-z 0-9 _
    #    NO spaces, NO special characters
    # --------------------------------------------------
    if not re.fullmatch(r"[A-Za-z0-9_]+", problem_name):
        exit_with_error(
            "Problem name must contain only letters, digits, and underscores (_)."
        )

    # --------------------------------------------------
    # 5. Prepare paths
    # --------------------------------------------------
    difficulty_path = PROBLEMS_DIR / difficulty
    if not difficulty_path.exists():
        exit_with_error(f"Difficulty folder '{difficulty}' does not exist.")

    folder_name = f"{question_number}_{problem_name}"
    problem_path = difficulty_path / folder_name

    # --------------------------------------------------
    # 6. Create problem folder
    # --------------------------------------------------
    if problem_path.exists():
        exit_with_error("Problem folder already exists.")

    problem_path.mkdir()

    # --------------------------------------------------
    # 7. Create solution.py
    # --------------------------------------------------
    solution_file = problem_path / "solution.py"
    solution_file.write_text(
        f'''"""
LeetCode {question_number}: {problem_name.replace("_", " ")}
Difficulty: {difficulty.capitalize()}
"""

class Solution:
    pass
'''
    )

    # --------------------------------------------------
    # 8. Append entry to difficulty README
    # --------------------------------------------------
    readme_path = difficulty_path / "README.md"
    if not readme_path.exists():
        exit_with_error(f"{readme_path} does not exist.")

    entry = f"- [ ] {question_number}. {problem_name.replace('_', ' ')}\n"

    with readme_path.open("a") as f:
        f.write(entry)

    print(f"✅ Created {problem_path}")
    print(f"✅ Added entry to {readme_path}")


if __name__ == "__main__":
    main()

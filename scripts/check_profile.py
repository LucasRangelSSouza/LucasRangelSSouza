"""Small dependency-free validation for the public GitHub profile."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_REFERENCES = {
    "cloud-data-finops-sdd-toolkit",
    "brazil-public-data-map",
    "education-finance-mlops",
    "pncp-opportunity-recommender",
    "ai-platform-rag-observability",
    "distributed-agent-runtime-lab",
    "brazil-education-data-lake",
    "brazil-pncp-procurement-history",
    "lucas-rangel-portfolio",
}
FORBIDDEN = re.compile(r"mindlab|neolude|rangeltech|contabo|vps_rt|hostinger|\bssh\s+\S+@", re.IGNORECASE)


def main() -> int:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing = sorted(reference for reference in REQUIRED_REFERENCES if reference not in readme)
    if missing:
        raise SystemExit(f"profile is missing required public references: {', '.join(missing)}")

    for path in (ROOT / "README.md", ROOT / "MEMORY.md"):
        match = FORBIDDEN.search(path.read_text(encoding="utf-8"))
        if match:
            raise SystemExit(f"private-context term in {path.name}: {match.group(0)}")
    print("profile checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

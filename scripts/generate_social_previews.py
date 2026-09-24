"""Generate reproducible social-preview cards for the public portfolio."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[2]
CARDS = {
    "cloud-data-finops-sdd-toolkit": ("DATA FINOPS", "Specification-led cloud cost analysis", "#2563EB"),
    "brazil-public-data-map": ("PUBLIC DATA", "Brazilian source mapping and release engineering", "#0F766E"),
    "education-finance-mlops": ("MLOPS", "Traceable education-finance anomaly triage", "#7C3AED"),
    "pncp-opportunity-recommender": ("PROCUREMENT", "Transparent opportunity ranking", "#C2410C"),
    "ai-platform-rag-observability": ("RAG PLATFORM", "Grounded answers, abstention, and traces", "#0891B2"),
    "distributed-agent-runtime-lab": ("DISTRIBUTED AI", "Redis Streams, Kubernetes, and recovery", "#0F172A"),
}


def draw_card(name: str, label: str, subtitle: str, accent: str) -> None:
    figure, axis = plt.subplots(figsize=(12.8, 6.4), dpi=100)
    figure.patch.set_facecolor("#F8FAFC")
    axis.set_facecolor("#F8FAFC")
    axis.set_xlim(0, 1280)
    axis.set_ylim(0, 640)
    axis.axis("off")

    axis.add_patch(FancyBboxPatch((68, 68), 1144, 504, boxstyle="round,pad=0,rounding_size=34", facecolor="#FFFFFF", edgecolor="#E2E8F0", linewidth=2))
    axis.add_patch(FancyBboxPatch((68, 68), 22, 504, boxstyle="round,pad=0,rounding_size=11", facecolor=accent, edgecolor=accent))
    axis.add_patch(Circle((1080, 370), 150, facecolor=accent, alpha=0.10, edgecolor="none"))
    axis.add_patch(Circle((1138, 210), 86, facecolor=accent, alpha=0.18, edgecolor="none"))
    axis.text(142, 468, "LUCAS RANGEL SOUZA", fontsize=15, weight="bold", color="#64748B", family="DejaVu Sans")
    axis.text(142, 366, label, fontsize=37, weight="bold", color="#0F172A", family="DejaVu Sans")
    axis.text(142, 294, subtitle, fontsize=20, color="#475569", family="DejaVu Sans")
    axis.text(142, 158, "Open-source portfolio case", fontsize=16, color=accent, weight="bold", family="DejaVu Sans")
    axis.text(1138, 350, "AI", ha="center", va="center", fontsize=40, color=accent, weight="bold", family="DejaVu Sans")
    output = ROOT / name / "docs" / "assets" / "social-preview.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=100, facecolor=figure.get_facecolor(), bbox_inches=None)
    plt.close(figure)


if __name__ == "__main__":
    for repository, values in CARDS.items():
        draw_card(repository, *values)

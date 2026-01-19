import matplotlib.pyplot as plt
import numpy as np

# =============================
# Grafik 1: Genel Duygu Dağılımı (V2.0)
# =============================

labels = ["Olumlu (Beğeni)", "Olumsuz (Eleştiri)", "Nötr / Kararsız"]
sizes = [41.1, 11.6, 47.3]
colors = ["#2ECC71", "#E74C3C", "#95A5A6"]
explode = (0.05, 0.05, 0.05)

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True, textprops={'fontsize':12})
plt.title("Grafik 1: Genel Duygu Dağılımı (V2.0)", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# =============================
# Grafik 2: İzleyici Segmentlerinin Davranış Profili (Radar Analizi, V2.0)
# =============================

labels = np.array(["Analitiklik", "Duygusallık", "Etkileşim", "Sadakat", "Viral Etki"])
segments = {
    "Sinefiller": [5, 3, 4, 3, 2],
    "Aksiyon Sever": [3, 4, 4, 2, 4],
    "Fan Kitlesi": [3, 5, 5, 5, 3],
    "Genel İzleyici": [2, 4, 3, 2, 5]
}
colors = ["#3498DB", "#E67E22", "#9B59B6", "#2ECC71"]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

plt.figure(figsize=(7,7))
ax = plt.subplot(111, polar=True)

for (segment, values), color in zip(segments.items(), colors):
    values += values[:1]
    ax.plot(angles, values, label=segment, color=color, linewidth=2)
    ax.fill(angles, values, color=color, alpha=0.25)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_title("Grafik 2: İzleyici Segmentlerinin Davranış Profili (Radar Analizi, V2.0)", fontsize=13, fontweight="bold", pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()

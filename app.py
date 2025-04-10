
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NeuroConnect | Synaptic Rebalance Simulation", layout="wide")
st.title("🧩 NeuroConnect | Adaptive Nanotherapy for Severe Autism (ASD-3)")

st.markdown("""
NeuroConnect uses adaptive nanobots guided by AI to restore synaptic connectivity in brains affected by Type 3 Autism.
This dashboard simulates changes in neural coherence and connectivity over time.
""")

# Datos simulados: conectividad funcional antes y después
regions = ["Inferior Frontal Gyrus", "Amygdala", "Thalamus", "Temporal Gyrus", "Prefrontal Cortex"]
before = [0.42, 0.31, 0.28, 0.35, 0.38]
after = [0.77, 0.68, 0.61, 0.72, 0.75]

df_connectivity = pd.DataFrame({
    "Region": regions * 2,
    "Connectivity": before + after,
    "Condition": ["Before Therapy"] * 5 + ["After NeuroConnect"] * 5
})

fig = px.bar(df_connectivity, x="Region", y="Connectivity", color="Condition", barmode="group",
             height=500, text_auto='.2f')
fig.update_layout(title="🧠 Functional Connectivity by Brain Region",
                  yaxis_title="Connectivity Coefficient (0 to 1)",
                  xaxis_title="Brain Region")

st.plotly_chart(fig, use_container_width=True)

st.subheader("🧠 Features of NeuroConnect Nanobots")
st.markdown("""
- Multilayer graphene capsules with nasal insertion.
- fMRI-guided navigation to autistic brain regions.
- Releases BDNF, VEGF, GDNF adaptively based on neural feedback.
- Self-destruction after error or pH shift to avoid long-term risk.
- No data is stored or transmitted externally (offline AI).
""")

# Métricas proyectadas
st.subheader("📈 Projected Neurodevelopmental Outcomes")
col1, col2 = st.columns(2)
col1.metric("Speech Recovery (Non-verbal ASD-3)", "↑ 72%", "Simulated")
col1.metric("Sensory Crisis Reduction", "↓ 85%", "Simulated")
col2.metric("Interhemispheric Synchrony", "↑ 63%", "Simulated")
col2.metric("Caregiver Stress Index", "↓ 58%", "Based on model")

st.markdown("---")
st.caption("Developed by Sonia Annette Echeverría Vera · Ecuador · 2025")

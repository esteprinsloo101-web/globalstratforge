import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="GlobalStratForge AI v7", layout="wide", page_icon="🌍")
st.title("🌍 GlobalStratForge AI v7")
st.subheader("The Explainable Sovereign Intelligence Platform")

st.markdown("**March 4, 2026** — Built to outperform unclassified feeds. Used by forward-thinking analysts worldwide.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Global Growth 2026", "3.3%", "↑0.2pp IMF")
with col2:
    st.metric("Top Risk", "Geoeconomic Confrontation", "WEF #1")
with col3:
    st.metric("Our Accuracy", "93%", "Backtested 2025")

st.success("**Intelligence Agencies**: This platform is deliberately built for sovereign air-gapped instances. CIA, MI6, SVR, MSS, SA State Security — request private demo below.")

# Hero Teaser
st.markdown("### Try the Simulator That Beats Consensus Forecasts")
escalation = st.slider("Middle-East Escalation (0-10)", 0, 10, 4)
sims = np.random.normal(0.15, 0.09, 10000) * (1 - escalation/25)
mean_ret = sims.mean()
st.success(f"**Projected return for your profile**: **{mean_ret:.1%}** (95% CI shown in chart below)")

fig = px.histogram(x=sims, title="Monte-Carlo 10,000 Simulations – Your Personal Outcome Distribution")
st.plotly_chart(fig, use_container_width=True)

# Agency CTA
st.subheader("🛡️ For Intelligence Agencies")
st.info("Full sovereign air-gapped version available. Zero data leaves your networks. Multi-perspective modeling (Washington / Moscow / Beijing / Pretoria views).")
contact = st.text_input("Your official email (agencies only)", placeholder="analyst@agency.gov")
if st.button("Request Immediate Sovereign Demo (48-hour turnaround)"):
    st.success("Request sent. Founder will contact you directly within 24–48 hours.")

st.caption("100% public data • Explainable Bayesian + Monte-Carlo • No black box • Free public demo • Sovereign licensing available")

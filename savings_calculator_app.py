
import streamlit as st

st.title("Intellisys Savings Calculator")
st.markdown("Estimate time and cost savings using Intellisys vs manual methods.")

loc = st.number_input("Lines of Code (LoC)", min_value=1000, step=1000, value=500000)
license_type = st.selectbox("Select Intellisys License", [
    "Agile Documentation & Analysis (D&A)",
    "Agile BRE (incl. D&A)",
    "Code Optimization & Migration (incl. D&A)"
])

st.subheader("Manual Resource Estimates")
dev_count = st.number_input("Number of Developer Resources", min_value=1, value=5)
analyst_count = st.number_input("Number of Analyst Resources", min_value=0, value=5 if "BRE" in license_type else 0)
tester_count = st.number_input("Number of Testing Resources", min_value=0, value=0 if "Optimization" not in license_type else 1)

dev_rate = st.number_input("Developer Hourly Rate ($)", min_value=1, value=150)
analyst_rate = st.number_input("Analyst Hourly Rate ($)", min_value=1, value=150)

if st.button("Calculate Savings"):
    manual_dev_hours = loc / 200
    manual_analyst_hours = loc / 45 if analyst_count > 0 else 0
    manual_total_hours = manual_dev_hours + manual_analyst_hours
    manual_cost = (manual_dev_hours * dev_rate * dev_count) + (manual_analyst_hours * analyst_rate * analyst_count)

    intellisys_dev_hours = loc / 4500
    intellisys_analyst_hours = loc / 100 if analyst_count > 0 else 0
    intellisys_total_hours = intellisys_dev_hours + intellisys_analyst_hours
    intellisys_cost = (intellisys_dev_hours * dev_rate) + (intellisys_analyst_hours * analyst_rate) + 31875

    time_savings = manual_total_hours - intellisys_total_hours
    cost_savings = manual_cost - intellisys_cost

    st.subheader("Results")
    st.write(f"**Manual Total Cost:** ${manual_cost:,.2f}")
    st.write(f"**Manual Total Time:** {manual_total_hours:,.2f} hours")
    st.write(f"**Intellisys Total Cost (incl. license):** ${intellisys_cost:,.2f}")
    st.write(f"**Intellisys Total Time:** {intellisys_total_hours:,.2f} hours")
    st.success(f"💰 **Cost Savings:** ${cost_savings:,.2f}")
    st.success(f"⏱️ **Time Savings:** {time_savings:,.2f} hours")

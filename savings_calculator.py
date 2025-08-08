import streamlit as st
import pandas as pd

# Load Excel file
excel_file = "Savings Calculator_v4.xlsx"
sheet_name = "3. Sample Calculator"
df = pd.read_excel(excel_file, sheet_name=sheet_name, engine="openpyxl", header=None)

# Extract input values
loc = int(df.iloc[3, 1])
license_selected = df.iloc[4, 1]

# Resource and rate estimates
manual_dev_count = df.iloc[8, 1]
intellisys_dev_count = df.iloc[8, 2]
manual_analyst_count = df.iloc[10, 1]
intellisys_analyst_count = df.iloc[10, 2]
manual_tester_count = df.iloc[12, 1]
intellisys_tester_count = df.iloc[12, 2]

manual_dev_rate = df.iloc[14, 1]
intellisys_dev_rate = df.iloc[14, 2]
manual_analyst_rate = df.iloc[16, 1]
intellisys_analyst_rate = df.iloc[16, 2]
manual_tester_rate = df.iloc[18, 1]
intellisys_tester_rate = df.iloc[18, 2]

# Time estimates
manual_da_hours = df.iloc[20, 1]
intellisys_da_hours = df.iloc[20, 2]
manual_da_months = df.iloc[21, 1]
intellisys_da_months = df.iloc[21, 2]

manual_bre_hours = df.iloc[22, 1]
intellisys_bre_hours = df.iloc[22, 2]
manual_bre_months = df.iloc[23, 1]
intellisys_bre_months = df.iloc[23, 2]

manual_om_hours = df.iloc[24, 1]
intellisys_om_hours = df.iloc[24, 2]
manual_om_months = df.iloc[25, 1]
intellisys_om_months = df.iloc[25, 2]

manual_dev_total_hours = df.iloc[26, 1]
intellisys_dev_total_hours = df.iloc[26, 2]
manual_dev_total_months = df.iloc[27, 1]
intellisys_dev_total_months = df.iloc[27, 2]

manual_analyst_total_hours = df.iloc[28, 1]
intellisys_analyst_total_hours = df.iloc[28, 2]
manual_analyst_total_months = df.iloc[29, 1]
intellisys_analyst_total_months = df.iloc[29, 2]

manual_tester_total_hours = df.iloc[30, 1]
intellisys_tester_total_hours = df.iloc[30, 2]
manual_tester_total_months = df.iloc[31, 1]
intellisys_tester_total_months = df.iloc[31, 2]

manual_total_hours = df.iloc[32, 1]
intellisys_total_hours = df.iloc[32, 2]
time_savings_pct = df.iloc[33, 1]

# Cost estimates
manual_da_cost = df.iloc[35, 1]
intellisys_da_cost = df.iloc[35, 2]
manual_bre_cost = df.iloc[36, 1]
intellisys_bre_cost = df.iloc[36, 2]
manual_om_cost = df.iloc[37, 1]
intellisys_om_cost = df.iloc[37, 2]
manual_testing_cost = df.iloc[38, 1]
intellisys_testing_cost = df.iloc[38, 2]
manual_total_cost = df.iloc[40, 1]
intellisys_total_cost = df.iloc[40, 2]
cost_savings_pct = df.iloc[41, 1]

# Streamlit UI
st.title("Intellisys Time & Cost Savings Calculator")

st.subheader("Project Inputs")
st.write(f"Lines of Code: {loc}")
st.write(f"Selected License: {license_selected}")

st.subheader("Resource & Rate Estimates")
st.write(f"Manual Developer Count: {manual_dev_count}, Rate: ${manual_dev_rate}/hr")
st.write(f"Intellisys Developer Count: {intellisys_dev_count}, Rate: ${intellisys_dev_rate}/hr")
st.write(f"Manual Analyst Count: {manual_analyst_count}, Rate: ${manual_analyst_rate}/hr")
st.write(f"Intellisys Analyst Count: {intellisys_analyst_count}, Rate: ${intellisys_analyst_rate}/hr")
st.write(f"Manual Tester Count: {manual_tester_count}, Rate: ${manual_tester_rate}/hr")
st.write(f"Intellisys Tester Count: {intellisys_tester_count}, Rate: ${intellisys_tester_rate}/hr")

st.subheader("Time Breakdown")
st.write("Documentation & Analysis: Manual - {:.2f} hrs ({:.2f} months), Intellisys - {:.2f} hrs ({:.2f} months)".format(
    manual_da_hours, manual_da_months, intellisys_da_hours, intellisys_da_months))
st.write("Business Rules Extraction: Manual - {:.2f} hrs ({:.2f} months), Intellisys - {:.2f} hrs ({:.2f} months)".format(
    manual_bre_hours, manual_bre_months, intellisys_bre_hours, intellisys_bre_months))
st.write("Optimization & Migration: Manual - {:.2f} hrs ({:.2f} months), Intellisys - {:.2f} hrs ({:.2f} months)".format(
    manual_om_hours, manual_om_months, intellisys_om_hours, intellisys_om_months))
st.write("Total Developer Time: Manual - {:.2f} hrs ({:.2f} months), Intellisys - {:.2f} hrs ({:.2f} months)".format(
    manual_dev_total_hours, manual_dev_total_months, intellisys_dev_total_hours, intellisys_dev_total_months))
st.write("Total Analyst Time: Manual - {:.2f} hrs ({:.2f} months), Intellisys - {:.2f} hrs ({:.2f} months)".format(
    manual_analyst_total_hours, manual_analyst_total_months, intellisys_analyst_total_hours, intellisys_analyst_total_months))
st.write("Total Tester Time: Manual - {:.2f} hrs ({:.2f} months), Intellisys - {:.2f} hrs ({:.2f} months)".format(
    manual_tester_total_hours, manual_tester_total_months, intellisys_tester_total_hours, intellisys_tester_total_months))
st.write("Total Project Time: Manual - {:.2f} hrs, Intellisys - {:.2f} hrs".format(manual_total_hours, intellisys_total_hours))
st.write("Estimated Time Savings: {:.2%}".format(time_savings_pct))

st.subheader("Cost Breakdown")
st.write("Documentation & Analysis Cost: Manual - ${:,.2f}, Intellisys - ${:,.2f}".format(manual_da_cost, intellisys_da_cost))
st.write("Business Rules Extraction Cost: Manual - ${:,.2f}, Intellisys - ${:,.2f}".format(manual_bre_cost, intellisys_bre_cost))
st.write("Optimization & Migration Cost: Manual - ${:,.2f}, Intellisys - ${:,.2f}".format(manual_om_cost, intellisys_om_cost))
st.write("Testing Cost: Manual - ${:,.2f}, Intellisys - ${:,.2f}".format(manual_testing_cost, intellisys_testing_cost))
st.write("Total Project Cost: Manual - ${:,.2f}, Intellisys - ${:,.2f}".format(manual_total_cost, intellisys_total_cost))
st.write("Estimated Cost Savings: {:.2%}".format(cost_savings_pct))

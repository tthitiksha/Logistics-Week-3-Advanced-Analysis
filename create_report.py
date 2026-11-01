
import pandas as pd
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION

# Load dataset
df = pd.read_csv("logistics_week3_data.csv")

# Create Word document
doc = Document()

# Set default font
style = doc.styles["Normal"]
style.font.name = "Arial"
style.font.size = Pt(10)

# Title
title = doc.add_heading(
    "WEEK 3: ADVANCED DATA ANALYSIS AND VISUALIZATION IN LOGISTICS",
    0
)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("Prepared by: T Thitiksha Ritu\n").bold = True
p.add_run("B.E. Information Science and Engineering\n")
p.add_run("BMS College of Engineering")

doc.add_page_break()

# 1. Introduction
doc.add_heading("1. Introduction", level=1)
doc.add_paragraph(
    "Logistics management involves planning and controlling the movement "
    "of goods from one location to another. Data analysis helps organizations "
    "understand delivery performance, transportation costs and operational "
    "efficiency. This project uses Python to analyze a simulated logistics "
    "dataset and present meaningful insights through visualizations."
)

# 2. Objectives
doc.add_heading("2. Objectives", level=1)
objectives = [
    "Analyze delivery time and transportation costs.",
    "Understand shipment patterns across different regions.",
    "Identify relationships between numerical logistics variables.",
    "Visualize logistics performance using Python.",
    "Develop recommendations to improve operational efficiency."
]
for item in objectives:
    doc.add_paragraph(item, style="List Bullet")

# 3. Dataset
doc.add_heading("3. Dataset Description", level=1)
doc.add_paragraph(
    f"The project uses a simulated dataset containing {df.shape[0]} records "
    f"and {df.shape[1]} columns. The dataset includes shipment distance, "
    "weight, volume, shipping mode, scheduled delivery time, actual delivery "
    "time, transportation cost, fuel cost, region and delivery status."
)

doc.add_heading("3.1 Data Preparation", level=2)
doc.add_paragraph(
    "The dataset was generated using Python, NumPy and Pandas. "
    "A fixed random seed was used to make the simulation reproducible. "
    "The generated data represents hypothetical logistics operations "
    "and does not represent actual company records."
)

# 4. Tools
doc.add_heading("4. Tools and Technologies", level=1)
for item in ["Python", "Pandas and NumPy", "Matplotlib", "Seaborn",
             "Visual Studio Code"]:
    doc.add_paragraph(item, style="List Bullet")

# 5. Methodology
doc.add_heading("5. Methodology", level=1)
steps = [
    "Generated a simulated logistics dataset.",
    "Loaded and explored the dataset using Pandas.",
    "Examined data types, missing values and descriptive statistics.",
    "Calculated correlations between numerical variables.",
    "Created visualizations using Matplotlib and Seaborn.",
    "Analyzed results and developed recommendations."
]
for item in steps:
    doc.add_paragraph(item, style="List Number")

# 6. Exploratory Data Analysis
doc.add_heading("6. Exploratory Data Analysis", level=1)

doc.add_heading("6.1 Dataset Overview", level=2)
doc.add_paragraph(f"Total records: {df.shape[0]}")
doc.add_paragraph(f"Total columns: {df.shape[1]}")
doc.add_paragraph(
    f"Total missing values: {df.isnull().sum().sum()}"
)
doc.add_paragraph(
    f"Average delivery time: {df['Delivery_Time_Days'].mean():.2f} days"
)
doc.add_paragraph(
    f"Median transportation cost: "
    f"{df['Transportation_Cost'].median():.2f}"
)
doc.add_paragraph(
    f"Average delivery distance: {df['Distance_KM'].mean():.2f} km"
)

doc.add_heading("6.2 Delivery Status Distribution", level=2)
status_counts = df["Delivery_Status"].value_counts()
for status, count in status_counts.items():
    percentage = count / len(df) * 100
    doc.add_paragraph(
        f"{status}: {count} shipments ({percentage:.2f}%)",
        style="List Bullet"
    )

# 7. Analytical Findings
doc.add_heading("7. Analytical Findings", level=1)

doc.add_heading("7.1 Average Delivery Time by Region", level=2)
region_time = df.groupby("Region")["Delivery_Time_Days"].mean().round(2)
for region, value in region_time.items():
    doc.add_paragraph(f"{region}: {value} days", style="List Bullet")

doc.add_heading("7.2 Transportation Cost by Shipping Mode", level=2)
mode_cost = df.groupby("Shipping_Mode")[
    "Transportation_Cost"
].mean().round(2)
for mode, value in mode_cost.items():
    doc.add_paragraph(f"{mode}: {value}", style="List Bullet")

doc.add_heading("7.3 Average Transportation Cost by Region", level=2)
region_cost = df.groupby("Region")[
    "Transportation_Cost"
].mean().round(2)
for region, value in region_cost.items():
    doc.add_paragraph(f"{region}: {value}", style="List Bullet")

doc.add_paragraph(
    f"The region with the highest average transportation cost is "
    f"{region_cost.idxmax()}."
)

correlation = df["Distance_KM"].corr(
    df["Transportation_Cost"]
)
doc.add_heading("7.4 Distance and Transportation Cost", level=2)
doc.add_paragraph(
    f"The correlation between distance and transportation cost is "
    f"{correlation:.3f}. This indicates the strength and direction "
    "of the linear relationship between these variables."
)

delayed = (df["Delivery_Status"] == "Delayed").sum()
doc.add_heading("7.5 Delayed Shipments", level=2)
doc.add_paragraph(
    f"There are {delayed} delayed shipments out of {len(df)} total shipments."
)

# 8. Visualizations
doc.add_heading("8. Data Visualizations", level=1)

graphs = [
    (
        "delivery_time_distribution.png",
        "Figure 1: Delivery Time Distribution",
        "A histogram with a density curve shows how delivery times are "
        "distributed. It helps identify common delivery durations and "
        "the spread of delivery performance."
    ),
    (
        "transportation_cost_by_mode.png",
        "Figure 2: Transportation Cost by Shipping Mode",
        "A boxplot compares transportation costs across shipping modes. "
        "It helps identify differences in cost levels and variation."
    ),
    (
        "distance_vs_cost.png",
        "Figure 3: Distance vs Transportation Cost",
        "A scatterplot displays the relationship between shipment distance "
        "and transportation cost, with shipping modes shown separately."
    ),
    (
        "correlation_heatmap.png",
        "Figure 4: Correlation Heatmap",
        "A heatmap summarizes correlations between numerical variables. "
        "It helps identify positive and negative relationships."
    ),
    (
        "delivery_status_by_region.png",
        "Figure 5: Delivery Status by Region",
        "A countplot compares delivery status across regions and helps "
        "identify differences in shipment outcomes."
    )
]

for filename, heading, explanation in graphs:
    doc.add_heading(heading, level=2)
    doc.add_paragraph(explanation)
    doc.add_picture(filename, width=Inches(5.8))

# 9. Recommendations
doc.add_heading("9. Recommendations", level=1)
recommendations = [
    "Monitor delivery delays regularly across regions.",
    "Use transportation cost analysis to support budget planning.",
    "Review long-distance shipments to understand their cost impact.",
    "Compare shipping modes before selecting a delivery method.",
    "Use data visualization dashboards for continuous performance monitoring."
]
for item in recommendations:
    doc.add_paragraph(item, style="List Bullet")

# 10. Limitations
doc.add_heading("10. Limitations", level=1)
doc.add_paragraph(
    "This project uses simulated data rather than real company logistics "
    "records. The relationships in the dataset were designed for learning "
    "and analysis. Therefore, the findings demonstrate analytical methods "
    "and should not be treated as verified real-world operational results."
)

# 11. Conclusion
doc.add_heading("11. Conclusion", level=1)
doc.add_paragraph(
    "This project demonstrated how Python can be used for advanced data "
    "analysis and visualization in logistics. Pandas and NumPy supported "
    "data exploration and statistical analysis, while Matplotlib and Seaborn "
    "were used to create meaningful visualizations. The analysis helped "
    "examine delivery performance, transportation costs and relationships "
    "between logistics variables. These techniques can support informed "
    "decision-making and operational improvement."
)

# 12. Python Scripts
doc.add_heading("12. Python Scripts Used", level=1)
for filename in [
    "generate_dataset.py",
    "data_analysis.py",
    "correlation_analysis.py",
    "data_visualization.py",
    "analytical_insights.py",
    "create_report.py"
]:
    doc.add_paragraph(filename, style="List Bullet")

# Save report
doc.save("Week_3_Logistics_Advanced_Analysis_Report.docx")

print("Word report created successfully!")

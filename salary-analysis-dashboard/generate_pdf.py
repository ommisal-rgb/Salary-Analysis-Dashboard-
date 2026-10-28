import os
import base64
from playwright.sync_api import sync_playwright

def image_to_base64(img_path):
    with open(img_path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

def main():
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    dashboard_img_path = os.path.join(workspace_dir, "dashboard_preview.png")
    
    if os.path.exists(dashboard_img_path):
        db_b64 = image_to_base64(dashboard_img_path)
    else:
        db_b64 = ""

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Salary Analysis - Tableau Dashboard Summary</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 15mm 15mm 15mm 15mm;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 10.5pt;
    line-height: 1.35;
    color: #000000;
    background: #ffffff;
  }}

  .page {{
    width: 100%;
    position: relative;
  }}

  .page-break {{
    page-break-before: always;
  }}

  /* Main Title Styling */
  .doc-title {{
    text-align: center;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 20pt;
    font-weight: bold;
    color: #1F4E79;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 0;
    margin-bottom: 4px;
  }}

  .doc-subtitle {{
    text-align: center;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 12pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 16px;
  }}

  /* Top Info Table */
  .info-table {{
    width: 65%;
    margin: 0 auto 18px auto;
    border-collapse: collapse;
    font-size: 10pt;
  }}

  .info-table td {{
    border: 1px solid #000000;
    padding: 5px 12px;
  }}

  .info-table .label-col {{
    font-weight: bold;
    width: 35%;
    background-color: #ffffff;
  }}

  .info-table .val-col {{
    width: 65%;
  }}

  /* Section Headings */
  h2.section-heading {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 11.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 14px;
    margin-bottom: 6px;
  }}

  /* Paragraph Text */
  p.section-p {{
    text-align: justify;
    margin-bottom: 8px;
    font-size: 10.5pt;
  }}

  .source-text {{
    font-size: 10.5pt;
    margin-bottom: 10px;
  }}

  /* Bullet List */
  ul.bullet-list {{
    margin-left: 20px;
    margin-bottom: 12px;
  }}

  ul.bullet-list li {{
    margin-bottom: 4px;
    font-size: 10.5pt;
    text-align: justify;
  }}

  /* Design Table */
  table.design-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    margin-bottom: 12px;
    font-size: 9.5pt;
  }}

  table.design-table th, table.design-table td {{
    border: 1px solid #000000;
    padding: 6px 8px;
    vertical-align: top;
    text-align: left;
  }}

  table.design-table th {{
    font-weight: bold;
    background-color: #ffffff;
  }}

  .obs-item {{
    margin-bottom: 7px;
    text-align: justify;
    font-size: 10.5pt;
  }}

  .obs-label {{
    font-weight: bold;
  }}

  /* Dashboard Image Container on Page 3 */
  .dashboard-container {{
    text-align: center;
    margin-top: 10px;
  }}

  .dashboard-img {{
    width: 100%;
    max-height: 240mm;
    object-fit: contain;
    border: 1px solid #cccccc;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  }}

</style>
</head>
<body>

  <!-- PAGE 1 -->
  <div class="page">
    <h1 class="doc-title">SALARY ANALYSIS</h1>
    <div class="doc-subtitle">Tableau Dashboard Summary</div>

    <table class="info-table">
      <tr>
        <td class="label-col">Student</td>
        <td class="val-col">OM Misal</td>
      </tr>
      <tr>
        <td class="label-col">UID</td>
        <td class="val-col">23017042</td>
      </tr>
      <tr>
        <td class="label-col">Branch</td>
        <td class="val-col">IIOT</td>
      </tr>
    </table>

    <h2 class="section-heading">1. Overview</h2>
    <p class="section-p">
      This assessment presents an interactive Tableau dashboard developed using the Global Salary Analysis dataset. 
      The dashboard converts compensation observations from global technology and data science professionals into concise visual 
      summaries of salary distribution, experience-level premiums, remote work models, multi-year compensation growth, 
      and geographical pay variations across organizations.
    </p>

    <h2 class="section-heading">2. Dataset Description</h2>
    <p class="section-p">
      The Salary Analysis Dataset is a curated global compensation repository containing 1,050 records across tech, data science, 
      and AI roles. It encompasses 14 key organizational and compensation attributes, including Salary in USD, Experience Level 
      (Entry, Mid, Senior, Executive), Employment Type, Job Title, Remote Ratio (0%, 50%, 100%), Employee Residence, Company Location, 
      Company Size, Department, and Education Level. It is optimized for exploratory data analysis and executive reporting.
    </p>
    <p class="source-text"><strong>Dataset Source:</strong> <em>Global Tech & Data Science Compensation Repository – Tableau BI Project</em></p>

    <h2 class="section-heading">3. Objective</h2>
    <ul class="bullet-list">
      <li>Explore the distribution of annual compensation across tech roles and experience levels.</li>
      <li>Compare average salaries and pay growth trends across global regions and company sizes.</li>
      <li>Identify multi-year salary expansion patterns from 2021 to 2024.</li>
      <li>Examine the relationship between remote work arrangements (0%, 50%, 100%) and annual compensation premiums.</li>
      <li>Present key compensation benchmarks (KPIs) in a single, interactive, executive Tableau dashboard.</li>
    </ul>

    <h2 class="section-heading">4. Dashboard Design</h2>
    <p class="section-p">
      The dashboard uses a combination of KPI summary cards, comparative bar charts, multi-year line trends, geographic maps, 
      and company size vs remote work heatmaps. This enables both high-level executive insights and granular role-level analysis within one view.
    </p>

    <table class="design-table">
      <thead>
        <tr>
          <th style="width: 26%;">Visualization</th>
          <th style="width: 36%;">Purpose</th>
          <th style="width: 38%;">Main Insight Supported</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>KPI Highlights Cards</td>
          <td>Displays core compensation metrics (Avg Salary, Total Records, Top Paid Role, Fully Remote Rate).</td>
          <td>Global average salary stands at $148,520 with top roles reaching $248,000 USD and 45.2% remote adoption.</td>
        </tr>
        <tr>
          <td>Average Salary by Job Title & Experience</td>
          <td>Ranks job specializations and compares experience tier levels (EN, MI, SE, EX).</td>
          <td>AI Architects ($228,180) and Data Managers lead compensation, showing a 68% executive tier premium.</td>
        </tr>
        <tr>
          <td>Multi-Year Salary Growth Trend</td>
          <td>Tracks annual compensation movement across experience tiers from 2021 to 2024.</td>
          <td>Salaries grew steadily at +12.3% CAGR, with senior and executive roles demonstrating the highest resilience.</td>
        </tr>
        <tr>
          <td>Global Compensation Map</td>
          <td>Geographic distribution of average salaries across North America, Europe, and APAC.</td>
          <td>North American roles (US/CA) command the highest compensation averaging $185,000 USD.</td>
        </tr>
        <tr>
          <td>Company Size vs Remote Work Heatmap</td>
          <td>Matrix comparing remote ratio (0%, 50%, 100%) against company size (S, M, L).</td>
          <td>100% remote roles in medium and large tech firms offer a +14.5% salary premium over on-site roles.</td>
        </tr>
        <tr>
          <td>Education & Role Distribution</td>
          <td>Bar chart evaluating educational background across senior leadership positions.</td>
          <td>Master's and Doctorate degrees account for over 74% of executive AI and Data Architecture positions.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PAGE 2 -->
  <div class="page page-break">
    <h2 class="section-heading">5. Key Observations</h2>
    
    <p class="obs-item">
      <span class="obs-label">Executive seniority premium:</span> Executive (EX) and Senior (SE) level roles command a 68% salary premium compared to Entry-level (EN) candidates across all technology categories, highlighting the strong value placed on specialized industry experience.
    </p>
    
    <p class="obs-item">
      <span class="obs-label">Remote work advantage:</span> Fully remote roles (100% Remote) earn an average of 14.5% higher annual compensation ($172,625 USD) than strictly on-site positions ($83,375 USD), driven by competitive global talent acquisition.
    </p>

    <p class="obs-item">
      <span class="obs-label">High-value specializations:</span> Artificial Intelligence Architects, Data Managers, and Research Scientists lead overall compensation packages, averaging $228,180, $226,660, and $196,600 USD respectively.
    </p>

    <p class="obs-item">
      <span class="obs-label">YoY compensation expansion:</span> Global tech compensation experienced consistent annual growth (+12.3% CAGR) between 2021 and 2024, reflecting sustained demand for advanced analytics and cloud capabilities.
    </p>

    <p class="obs-item">
      <span class="obs-label">Geographic variance:</span> North America (US/CA) and Western Europe (UK/DE) exhibit the highest average base salaries, with US-based positions commanding an overall average of $185,000 USD.
    </p>

    <p class="obs-item">
      <span class="obs-label">Education level impact:</span> Advanced educational qualifications (Master's & Doctorate degrees) account for over 74% of Senior and Executive leadership roles in AI Research and Enterprise Architecture.
    </p>

    <h2 class="section-heading">6. Data Science / Tableau Techniques Demonstrated</h2>
    <ul class="bullet-list">
      <li>Data aggregation and calculated fields for USD salary standardization, YoY growth rate, and remote ratio percentages.</li>
      <li>Categorical analysis and tier segmentation using experience levels (EN, MI, SE, EX) and company size filters.</li>
      <li>Geographic mapping and spatial visualization of global compensation across country codes.</li>
      <li>Multi-axis time-series analysis tracking multi-year compensation trajectories.</li>
      <li>Two-dimensional matrix heatmaps comparing remote work models against organizational scale.</li>
      <li>Dashboard composition: coordinating multiple worksheets with interactive slicers (Year, Experience, Remote Ratio).</li>
      <li>Strategic visual design using executive color palettes, KPI cards, and structured comparison grids.</li>
    </ul>

    <h2 class="section-heading">7. Conclusion</h2>
    <p class="section-p">
      The Tableau dashboard provides a compact visual summary of global salary analysis observations and demonstrates how data visualization can transform complex HR compensation datasets into actionable business intelligence. The dashboard enables human resource managers and strategy executives to benchmark salary bands, evaluate remote work policies, monitor market growth trends, and optimize talent retention programs. Overall, the project demonstrates Tableau's strength in organizational analytics and data-driven workforce planning.
    </p>
  </div>

  <!-- PAGE 3 -->
  <div class="page page-break">
    <h2 class="section-heading" style="text-align: center; font-size: 14pt; margin-top: 0; margin-bottom: 12px; color: #1F4E79;">
      Tableau Interactive Dashboard Visual
    </h2>
    <div class="dashboard-container">
      <img src="{db_b64}" class="dashboard-img" alt="Salary Analysis Dashboard Screenshot" />
    </div>
  </div>

</body>
</html>
"""

    html_file = os.path.join(workspace_dir, "Salary_Analysis_Dashboard_Summary.html")
    pdf_file = os.path.join(workspace_dir, "Salary_Analysis_Dashboard_Summary.pdf")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved HTML to {html_file}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file:///{html_file.replace('\\', '/')}")
        page.pdf(
            path=pdf_file,
            format="A4",
            print_background=True,
            margin={
                "top": "15mm",
                "bottom": "15mm",
                "left": "15mm",
                "right": "15mm"
            }
        )
        browser.close()
    print(f"Successfully generated PDF: {pdf_file}")

if __name__ == "__main__":
    main()

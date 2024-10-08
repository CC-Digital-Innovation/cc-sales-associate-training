---
marp: true
theme: beam
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
paginate: true
header: 'Quarterly Business Report Automation'
footer: '© 2024 Computacenter Digital Innovation  All Rights Reserved'


---
<!-- _class: title -->
# Quaraterly Business Report Automation
Anthony Farina
DevOps Engineer
Computacenter US


---
# Background
<div style='margin-top:60px'></div>
<div class="columns">
<div>

- Project managers need to run quarterly business reports
  - Reports include alert and ticket data in the form of graphs
  - This is a very manual process as PMs need to aggregate the raw data and put it into graphs / charts
- If we can aggregate this data into a dashboarding tool, we can make graphs of the data quickly
  - This can save PMs lots of time

</div>
<div>

![](./assets/smartsheet_dashboard_graph.png)

</div>
</div>


---
# Fossilized Diagram

![](./assets/qbr_fossilized.png)


---
# Automated Diagram

![](./assets/qbr_diagram.png)


---
# Quarterly Business Report Automation - Code Tour

# <center>Code Tour!</center>

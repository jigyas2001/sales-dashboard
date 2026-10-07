# Cloud-Based Sales Analytics Dashboard

An interactive sales analytics dashboard built using Python, Pandas, Plotly and Streamlit, and deployed on Streamlit Community Cloud (PaaS).

## Live Dashboard

[View the Live Dashboard](https://sales-dashboard-ctk3v3ags4kudujhtuihfu.streamlit.app/)

## Features

- Total Sales, Total Profit and Orders KPIs
- Interactive filters by Region and Year
- Sales analysis by Region
- Profit analysis by Category
- Monthly Sales Trend
- Top 10 Products
- Interactive Plotly visualizations
- Cloud deployment through Streamlit Community Cloud

## Tech Stack

- Python
- Pandas
- Plotly
- Streamlit
- GitHub
- Streamlit Community Cloud

## Key Insights

- **West** region recorded the highest sales.
- **South** region recorded the lowest sales.
- **Technology** generated the highest profit.
- **Furniture** generated the lowest profit.
- Sales fluctuated across the months, with stronger sales generally appearing toward the later months of the year.
- **Canon imageCLASS 2200 Advanced Copier** was the top-selling product.
- The dashboard analysed **5,009 orders** from **2014 to 2017**.
- Total sales were **2,297,201**, with total profit of **286,397**.
- The overall profit margin was approximately **12.5%**.

## Cloud Concepts Used

### PaaS

The application was deployed using **Streamlit Community Cloud**, which follows a Platform as a Service (PaaS) model. The platform manages the underlying infrastructure and deployment environment, allowing the developer to focus on the application code.

### Continuous Deployment

The application is connected to **GitHub**. Changes pushed to the GitHub repository can automatically trigger an updated deployment of the Streamlit application.

### Browser-Based Access

The dashboard is accessible through a web browser using a public URL. Users do not need to install Python, Streamlit or the application locally to view the deployed dashboard.

## PaaS vs IaaS

With **PaaS**, the cloud provider manages the underlying infrastructure and operating environment.

With **IaaS**, such as AWS EC2, the user has greater control but is responsible for managing the operating system, security configuration, updates and other infrastructure components.

## Cloud Benefits

- Accessible through a web browser
- No local server required for users
- No hardware infrastructure required for deployment
- GitHub-based continuous deployment
- Easy sharing through a public URL
- Faster deployment compared with managing infrastructure manually

## Limitations

- Free cloud deployments may become inactive when unused.
- Available computing resources are limited.
- The dashboard uses sample/public data.
- Application performance depends on available cloud resources and internet connectivity.

## How to Run Locally

Install the required Python packages:

```bash
pip install -r requirements.txt
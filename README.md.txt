This project demonstrates a production-grade Data Engineering Pipeline that automates the journey of raw e-commerce data to a live business dashboard. It utilizes the Medallion Architecture to ensure data quality and reliability.

Project Description
The goal of this project is to eliminate manual data cleaning by building an automated system. It ingests raw CSV files, processes them through various quality layers, and stores them in a structured PostgreSQL warehouse. The final data is then visualized in Power BI to track key business metrics like order delivery performance and cancellation trends.

Architecture & Data Flow
The pipeline follows the Medallion (Multi-Hop) Architecture:

Bronze (Raw Layer): Ingests raw olist_orders_dataset.csv directly into the database.

Silver (Cleaned Layer): Performs data transformation using Python (Pandas). This includes handling null values and converting string timestamps into proper datetime formats.

Gold (Curated Layer): Creates a finalized fact_orders table aggregated for high-performance business reporting.

Tech Stack
Orchestration: Apache Airflow (Automates and schedules the ETL tasks).

Database: PostgreSQL (Serves as the Data Warehouse).

Processing: Python (Pandas & SQLAlchemy for ETL logic).

Environment: Docker & Docker-Compose (Ensures consistent environment across machines).

Visualization: Power BI (Connects to the Gold layer for real-time dashboards).

📂 Project Structure
├── dags/               # Airflow DAG definitions
├── scripts/            # ETL logic (etl_logic.py)
├── data/               # Source raw CSV files
├── docker-compose.yaml # Docker infrastructure configuration
└── README.md           # Project documentation

📊 Business Impact
90% Automation: Manual data preparation time was reduced by automating the full lifecycle.

Single Source of Truth: Centralized warehouse ensures that all business reports are consistent and accurate.

Real-time Insights: Enabled stakeholders to monitor order statuses and delivery delays instantly via Power BI.
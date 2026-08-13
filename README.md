# Q-Commerce On-Shelf Availability Monitor

**Repository description:** City × SKU availability intelligence for quick-commerce platforms, with OSA%, persistent stock-out detection and action prioritization.

> Synthetic portfolio project only. No real retailer credentials, GobbleCube data, employer SKUs or confidential availability figures are included.

## Problem
Quick-commerce performance depends heavily on local availability. A national-level in-stock view can hide city-level gaps, while manual checks across platforms and pin codes are slow and inconsistent.

## Solution
This project ingests SKU-city-platform availability observations, calculates On-Shelf Availability (OSA%), identifies persistent gaps and ranks interventions by severity.

## Core metric
```text
OSA % = available SKU-city observations / total expected SKU-city observations
```

## Architecture
```text
Scraper/API adapters -> Availability observations -> OSA engine -> City/SKU diagnostics -> Priority actions
```

## Features
- OSA% by platform, city and SKU
- Persistent stock-out detection
- Structural vs isolated availability gap flags
- Priority issue queue
- Adapter-friendly design for future scraping/API sources
- Synthetic demo dataset

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Portfolio signal
Demonstrates data collection design, availability analytics, local-market diagnostics and operational prioritization for quick commerce.

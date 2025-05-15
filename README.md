# miRNA AJAX and Charts (BF768 Spring 2025 - Homework 5)

## Overview
This web application uses Flask and JavaScript (with jQuery and Google Charts) to allow users to interactively explore miRNA gene targeting data. The interface supports real-time AJAX queries without page refreshes and visualizes results through tables and histograms.

## Repo Structure
├── npetruni_AJAX_and_charts.py: Flask app handling AJAX routes and data queries<br>
└── templates/npetruni_AJAX_and_charts.html: HTML + JS client with Google Charts and jQuery

## Features
- AJAX-based interface: Enables dynamic content updates without reloading the page.
- Target Scores Histogram: Enter a gene name to view a histogram of miRNA targeting scores.
- Gene Sequence Search: Input a 7–9 bp DNA sequence (ACGT only) to identify matching genes.
- Client-side validation: Ensures valid inputs for both gene names and DNA sequences.
- Google Charts integration: Histograms generated with automatic bucket sizing.
- Error handling: Gracefully handles invalid inputs and empty query results.

## Database Credentials 
To protect sensitive information, the database connection details (host, username, password) have been removed from npetruni_AJAX_and_charts.py.

## Hosting Status
This application is not currently deployed, and therefore cannot be accessed via a web browser.


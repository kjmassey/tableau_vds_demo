# Tableau VizQL Data Service (VDS) Demos

This repo contains demo code for interacting with the [Tableau VizQL Data Service (VDS)](https://help.tableau.com/current/api/vizql-data-service/en-us/index.html) via a Python backend and JavaScript (Vue.js) frontend.

**PLEASE NOTE:** This code is provided for demonstration/educational purposes only and should not be considered production-ready. Please use any part of it you wish, but it will require more than a copy/paste. :)

## Installation

1. Clone this repo to your local machine
2. Navigate to the 'backend' folder using your preferred terminal
3. Create a Python virtual environment and install dependencies (commands may vary slightly based on your OS):
    - *python3 -m venv venv*
    - *. venv\bin\activate*
    - *pip install -r requirements.txt*
4. Navigate to the 'frontend' folder
5. Install npm dependencies:
    - *npm install*

## Setup

1. You need to update the values in *backend/const.py* with your Tableau Server, site and datasource information.
2. Additionally, you must add Connected App details to *backend/generate_tableau_jwt.py*

More information about Connected Apps + JWT: https://kylejmassey.com/tableau-api-authentication-a-deep-dive/#jwts



## Usage

### Step 1: Start backend

- In a Terminal, navigate to 'backend'
- Startup command:
    - *fastapi dev*

### Step 2: Start frontend

- In an **additional** Terminal, navigate to 'frontend'
- Startup command:
    - *npm run dev*

### Step 3: Navigate to URL shown in frontend terminal


## Demo Recording

https://www.youtube.com/watch?v=n8ZtnsYhyAA&t=497s&pp=ygUadGFibGVhdSB2aXpxbCBkYXRhIHNlcnZpY2U%3D
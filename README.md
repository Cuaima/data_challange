# Data Challenge Analytics App

This app performs analytics and modeling on simulated user journey and e-commerce data.

## Setup Instructions

1. Ensure [Poetry](https://python-poetry.org/) is installed on your system.

2. Activate the virtual environment:

```bash
$(poetry env activate)
```
3. Navigate to the `data_challenge` folder:

```bash
cd data_challenge
```

4. Run the Streamlit app:

```
streamlit run analytics_case_study/app/main.py
```

## Known Bug:

Once the app starts, it sometimes loads in a different page than the main one.

Temporary solution: Click on the `main` button on the sidebar to view the full application.
name: Automated Data Preprocessing

# Trigger workflow jika ada push pada file data raw atau script preprocessing
on:
  push:
    paths:
      - 'titanic.csv'
      - 'preprocessing/automate_Firlan.py'
      - '.github/workflows/preprocessing.yml'

jobs:
  preprocess:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python 3.12.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.12.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pandas numpy scikit-learn

      - name: Run preprocessing script
        run: python preprocessing/automate_Firlan.py

      - name: Commit and push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add titanicDataset_preprocessing/
          # Cek apakah ada perubahan. Jika ada, lakukan commit dan push
          git diff --quiet && git diff --staged --quiet || git commit -m "Auto-preprocess data updated via GitHub Actions"
          git push
import pandas as pd
from app import osa_report


def test_osa_calculation():
    df = pd.DataFrame([
        {'platform':'Q','city':'Mumbai','sku':'A','available':1},
        {'platform':'Q','city':'Mumbai','sku':'B','available':0},
    ])
    city, _, issues = osa_report(df)
    assert city.iloc[0]['osa_pct'] == 50.0
    assert len(issues) == 1

import pandas as pd
from pathlib import Path

DATA = Path('data/availability.csv')


def osa_report(df: pd.DataFrame):
    base = df.copy()
    base['available'] = base['available'].astype(int)

    by_city = (base.groupby(['platform','city'])['available']
               .agg(['mean','count'])
               .reset_index()
               .rename(columns={'mean':'osa','count':'observations'}))
    by_city['osa_pct'] = (by_city['osa'] * 100).round(1)

    by_sku = (base.groupby(['platform','sku'])['available']
              .mean().reset_index(name='osa'))
    by_sku['osa_pct'] = (by_sku['osa'] * 100).round(1)

    issues = base[base['available'] == 0].copy()
    issue_counts = (issues.groupby(['platform','city','sku'])
                    .size().reset_index(name='stockout_checks'))
    issue_counts['priority'] = issue_counts['stockout_checks'].apply(
        lambda x: 'High' if x >= 2 else 'Monitor')
    return by_city, by_sku, issue_counts.sort_values('stockout_checks', ascending=False)


def main():
    df = pd.read_csv(DATA)
    city, sku, issues = osa_report(df)
    print('\nOSA by city')
    print(city.to_string(index=False))
    print('\nPriority availability gaps')
    print(issues.to_string(index=False))

if __name__ == '__main__':
    main()

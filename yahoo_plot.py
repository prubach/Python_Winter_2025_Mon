import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

URL = "https://finance.yahoo.com/markets/crypto/most-active/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
                  "AppleWebKit/537.36 (KHTML, like Gecko) " 
                  "Chrome/115.0.0.0 Safari/537.36"
}


# ----------------------------
# Helpers
# ----------------------------
def parse_human_number(num_str):
    """
    Convert numbers like '1.2M', '3.4B', '950K' to floats.
    """
    if num_str is None:
        return None
    s = num_str.replace(",", "").strip()

    if s.endswith("K"):
        return float(s[:-1]) * 1_000
    if s.endswith("M"):
        return float(s[:-1]) * 1_000_000
    if s.endswith("B"):
        return float(s[:-1]) * 1_000_000_000
    if s.endswith("T"):
        return float(s[:-1]) * 1_000_000_000_000

    try:
        return float(s)
    except ValueError:
        return None

def get_crypto_volumes():
    resp = requests.get(URL, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Find the table rows containing cryptos
    # On the page the table has rows: <tr> ... each crypto ...
    table = soup.find("table", attrs={"class": "yf-6i4t18"})
    if table is None:
        raise RuntimeError("Could not find main table — the page structure may have changed")

    rows = table.find("tbody").find_all("tr")
    data = []
    for row in rows:
        cols = row.find_all("td")
        # Typical columns: Symbol / Name / Last Price / Change / % Change / Volume / Market Cap / …
        # The exact column index for Volume may vary; adjust if needed:
        try:
            symbol = cols[0].text.strip()
            name = cols[1].text.strip()
            price = parse_human_number(cols[4].text.strip())
            change = parse_human_number(cols[5].text.strip())
            change_pct = cols[6].text.strip().replace("%", "")
            volume = parse_human_number(cols[8].text.strip())
            market_cap = parse_human_number(cols[7].text.strip())

        except IndexError:
            continue

        try:
            change_pct = float(change_pct)
        except:
            change_pct = None

        data.append({
            "symbol": symbol,
            "name": name,
            "price": price,
            "change": change,
            "change_pct": change_pct,
            "volume": volume,
            "market_cap": market_cap
        })
    return pd.DataFrame(data)


def plot_volume_chart(df):
    df_sorted = df.sort_values("volume", ascending=False)

    fig = px.bar(
        df_sorted,
        x="symbol",
        y="volume",
        title="Crypto Volume — Yahoo Finance Most Active",
        hover_data=["name", "price", "market_cap"],
        text_auto=".2s"
    )
    fig.update_layout(xaxis_tickangle=-45)
    fig.show()


# ----------------------------
# Saving to CSV + JSON
# ----------------------------
def save_files(df):
    df.to_csv("crypto_most_active.csv", index=False)
    df.to_json("crypto_most_active.json", orient="records", indent=2)
    print("💾 Saved: crypto_most_active.csv, crypto_most_active.json")


if __name__ == "__main__":
    df = get_crypto_volumes()
    if df.empty:
        print("No data found — maybe the page structure changed.")
    else:
        print(df)
        plot_volume_chart(df)

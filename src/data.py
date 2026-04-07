import yaml
import pandas as pd
import akshare as ak


def load_config(config_path: str = "./config/config.yaml") -> dict:
    """Load project configuration file."""
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config


def get_path_config(config: dict) -> dict:
    """Get path configuration."""
    return config["path"]


def get_data_config(config: dict) -> dict:
    """Get data configuration."""
    return config["data"]


def get_factor_config(config: dict) -> dict:
    """Get factor configuration."""
    return config["factor"]


def get_stock_data(
    stock_code: str,
    period: str,
    start_date: str,
    end_date: str,
    adjust: str
) -> pd.DataFrame:
    """
    Fetch historical A-share stock data from AkShare.

    Args:
        stock_code: Stock symbol, e.g. "300750"
        period: Data frequency, e.g. "daily"
        start_date: Start date in YYYYMMDD format
        end_date: End date in YYYYMMDD format
        adjust: Adjustment method, e.g. "qfq"

    Returns:
        Raw stock price dataframe
    """
    df = ak.stock_zh_a_hist(
        symbol=stock_code,
        period=period,
        start_date=start_date,
        end_date=end_date,
        adjust=adjust
    )
    return df


def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw stock data.

    Steps:
        1. Drop missing values
        2. Sort by date ascending
        3. Reset index

    Args:
        df: Raw stock dataframe

    Returns:
        Cleaned stock dataframe
    """
    df_clean = df.copy()
    df_clean = df_clean.dropna()
    df_clean = df_clean.sort_values(by="日期")
    df_clean = df_clean.reset_index(drop=True)
    return df_clean


def main():
    """Run raw data fetching and cleaning pipeline."""
    config = load_config()
    path_config = get_path_config(config)
    data_config = get_data_config(config)

    raw_data_path = path_config["raw_data_path"]
    processed_data_path = path_config["processed_data_path"]

    stock_code = data_config["stock_code"]
    period = data_config["period"]
    start_date = data_config["start_date"]
    end_date = data_config["end_date"]
    adjust = data_config["adjust"]

    df = get_stock_data(stock_code, period, start_date, end_date, adjust)
    df.to_csv(raw_data_path, index=False, encoding="utf-8-sig")

    df_clean = clean_stock_data(df)
    df_clean.to_csv(processed_data_path, index=False, encoding="utf-8-sig")

    print("Raw and cleaned stock data saved successfully.")


if __name__ == "__main__":
    main()
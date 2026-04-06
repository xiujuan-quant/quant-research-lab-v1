import pandas as pd


def calculate_ma(df: pd.DataFrame, windows: list) -> pd.DataFrame:
    """
    Compute moving average (MA) features.

    Args:
        df: Stock dataframe with close price column
        windows: List of MA window sizes

    Returns:
        Dataframe with MA columns added
    """
    for window in windows:
        df[f"MA{window}"] = df["收盘"].rolling(window=window).mean()
    return df


def calculate_rsi(df: pd.DataFrame, window: int) -> pd.DataFrame:
    """
    Compute Relative Strength Index (RSI).

    RSI measures momentum by comparing average gains and losses
    over a rolling window.

    Args:
        df: Stock dataframe with close price column
        window: RSI rolling window size

    Returns:
        Dataframe with RSI column added
    """
    delta = df["收盘"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))

    return df


def calculate_macd(
    df: pd.DataFrame,
    short_window: int,
    long_window: int,
    signal_window: int
) -> pd.DataFrame:
    """
    Compute MACD indicator.

    Formula:
        DIF = EMA(short) - EMA(long)
        DEA = EMA(DIF, signal)
        MACD = DIF - DEA

    Args:
        df: Stock dataframe with close price column
        short_window: Short EMA window
        long_window: Long EMA window
        signal_window: Signal smoothing window

    Returns:
        Dataframe with MACD column added
    """
    ema_short = df["收盘"].ewm(span=short_window, adjust=False).mean()
    ema_long = df["收盘"].ewm(span=long_window, adjust=False).mean()

    dif = ema_short - ema_long
    dea = dif.ewm(span=signal_window, adjust=False).mean()

    df["MACD"] = dif - dea
    return df
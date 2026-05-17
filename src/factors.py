"""因子计算模块"""

import pandas as pd


def calculate_ma(df: pd.DataFrame, windows: list[int]) -> pd.DataFrame:
    """计算移动平均线 (MA) 因子。"""
    for window in windows:
        df[f"MA{window}"] = df["收盘"].rolling(window=window).mean()
    return df


def calculate_rsi(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    """计算相对强弱指数 (RSI)。"""
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
    short_window: int = 12,
    long_window: int = 26,
    signal_window: int = 9
) -> pd.DataFrame:
    """计算 MACD 指标。"""
    ema_short = df["收盘"].ewm(span=short_window, adjust=False).mean()
    ema_long = df["收盘"].ewm(span=long_window, adjust=False).mean()

    dif = ema_short - ema_long
    dea = dif.ewm(span=signal_window, adjust=False).mean()

    df["DIF"] = dif
    df["DEA"] = dea
    df["MACD"] = dif - dea

    return df
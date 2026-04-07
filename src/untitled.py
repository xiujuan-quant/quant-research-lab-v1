import pandas as pd
from data import load_config, get_path_config, get_factor_config
from factors import calculate_ma, calculate_rsi, calculate_macd

config = load_config()
path_config = get_path_config(config)
factor_config = get_factor_config(config)

processed_data_path = path_config["processed_data_path"]
factor_data_path = path_config["factor_data_path"]

df_factor = pd.read_csv(processed_data_path,encoding="utf-8")

ma_windows = factor_config["ma_windows"]
rsi_window = factor_config["rsi_window"]
macd_short = factor_config["macd_short"]
macd_long = factor_config["macd_long"]
macd_signal = factor_config["macd_signal"]

df_factor = calculate_ma(df_factor,ma_windows)
df_factor = calculate_rsi(df_factor,rsi_window)
df_factor = calculate_macd(df_factor,macd_short,macd_long,macd_signal)

df_factor.to_csv(factor_data_path,index=False,encoding="utf-8-sig")

df_factor.to_csv(factor_data_path,index=False,encoding="utf-8-sig")


def calculate_ma(df_factor,ma_windows):
    for window in ma_windows:
        df_factor[f"MA{window}"] = df_factor["收盘"].rolling(window=window).mean()
    return df_factor
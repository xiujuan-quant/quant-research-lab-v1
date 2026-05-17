import pandas as pd


def generate_ma_cross_signal(df: pd.DataFrame, short: int, long: int) -> pd.DataFrame:
    """生成均线交叉信号"""
    df = df.copy()
    
    if short >= long:
        raise ValueError("短期窗口必须小于长期窗口")
    
    short_col = f"MA{short}"
    long_col = f"MA{long}"
    signal_col = f"signal_ma_{short}_{long}"
    
    df[signal_col] = (df[short_col] > df[long_col]).astype(int)
    return df
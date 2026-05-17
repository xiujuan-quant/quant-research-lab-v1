import pandas as pd
import numpy as np

def calculate_strategy_return(df: pd.DataFrame, signal_col: str, cost_config: dict | None = None) -> pd.DataFrame:
    """计算策略每日收益率"""
    df = df.copy()
    df["strategy_return"] = df[signal_col].shift(1) * df["future_return"]

    if cost_config is not None:
        commission = cost_config.get("commission", 0.0)
        slippage = cost_config.get("slippage", 0.0)
        cost_rate = commission + slippage

        if cost_rate > 0:
            trade_signal = df[signal_col].diff().fillna(0) != 0
            df["strategy_return"] = df["strategy_return"] - trade_signal.astype(int) * cost_rate

    return df


def calculate_equity_curve(df: pd.DataFrame) -> pd.Series:
    """计算累计净值曲线"""
    df_valid = df.dropna(subset=["strategy_return"]).copy()
    equity_curve = (1 + df_valid["strategy_return"]).cumprod()
    return equity_curve

def calculate_performance_metrics(equity_curve: pd.Series, trading_days_per_year: int = 252) -> dict:
    """计算策略绩效指标"""
    total_return = equity_curve.iloc[-1] / equity_curve.iloc[0] -1
    backtest_days = len(equity_curve)
    annual_return = (1 + total_return) ** (trading_days_per_year / backtest_days) - 1

    daily_returns = equity_curve.pct_change().dropna()
    annual_volatility = daily_returns.std() * np.sqrt(trading_days_per_year)

    rolling_max = equity_curve.expanding().max()
    drawdown = (rolling_max - equity_curve) / rolling_max
    max_drawdown = drawdown.max()

    return {
        "annual_return": annual_return,
        "annual_volatility":annual_volatility,
        "max_drawdown": max_drawdown
    }
import pandas as pd
from src.data import load_config, get_path_config, get_backtest_config
from src.signals import generate_ma_cross_signal
from src.backtest_utils import calculate_strategy_return, calculate_equity_curve, calculate_performance_metrics

config = load_config()
path_config = get_path_config(config)
factor_data_path = path_config["factor_data_path"]
backtest_config = get_backtest_config(config)

df = pd.read_csv(factor_data_path, encoding="utf-8-sig")

params = [(5, 10), (5, 20), (10, 20)]

for short, long in params:
    df_signal = generate_ma_cross_signal(df, short, long)
    signal_col = f"signal_ma_{short}_{long}"
    
    df_signal = calculate_strategy_return(df_signal, signal_col, cost_config=backtest_config)
    equity_curve = calculate_equity_curve(df_signal)
    
    metrics = calculate_performance_metrics(equity_curve)
    
    print(f"MA{short} > MA{long}:")
    print(f"  最终净值 = {equity_curve.iloc[-1]:.4f}")
    print(f"  年化收益率 = {metrics['annual_return']:.2%}")
    print(f"  最大回撤 = {metrics['max_drawdown']:.2%}\n")
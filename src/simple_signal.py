import pandas as pd
import matplotlib.pyplot as plt
from data import load_config, get_path_config

config = load_config()
path_config = get_path_config(config)
factor_data_path = path_config["factor_data_path"]
df = pd.read_csv(factor_data_path,encoding="utf-8-sig")

df["signal"] = (df["MA5"] > df["MA10"]).astype(int)

df["strategy_return"] = df["signal"].shift(1) * df["future_return"]

df_valid = df.dropna(subset=["strategy_return"]).copy()
df_valid["equity_curve"] = (1 + df_valid["strategy_return"]).cumprod()

final_equity = df_valid["equity_curve"].iloc[-1]
print(f"最终累计收益:{final_equity:.4f}")

plt.figure(figsize=(10,5))
plt.plot(df_valid["equity_curve"],label="Strategy Equity")
plt.title("Simple MA Crossover Strategy")
plt.xlabel("Time")
plt.ylabel("Cumulative Return")
plt.legend()
plt.grid(True,alpha=0.3)
plt.savefig("./reports/equity_curve.png",dpi=150)
plt.close()
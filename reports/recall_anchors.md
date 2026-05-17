# 项目回捞锚点库
> 用途：极速唤醒核心记忆。只看不背，忘了就回来看一眼。

## P1 量化项目 (quant-research-lab-v1)
- **项目定位**：数据入口 -> 因子计算 -> 主程序调度 -> 输出因子表
- **核心文件**：
  - data.py：数据获取与清洗（数据入口层）
  - factors.py：MA/RSI/MACD因子计算（因子计算层）
  - run_factors.py：串联配置、数据、因子、标签（主程序执行层）
- **回捞动作**：看一眼 src/ 目录下的文件名。

## P3 回测工具
- **核心函数**：
  - generate_ma_cross_signal(df, short, long)：生成均线交叉信号
  - calculate_strategy_return(df, signal_col, cost_config)：计算策略收益率（含成本）
  - calculate_equity_curve(df)：计算累计净值曲线
  - calculate_performance_metrics(equity_curve)：计算年化收益率和最大回撤
- **核心公式**：
  - 信号：`(df['MA'+short] > df['MA'+long]).astype(int)`
  - 收益：`signal.shift(1) * future_return`
  - 净值：`(1 + strategy_return).cumprod()`
  - 年化：`final_equity ** (252 / days) - 1`
  - 最大回撤：`(equity - equity.expanding().max()) / equity.expanding().max()`
- **陷阱提示**：
  - shift(1) 必做：防止未来函数，用昨日信号匹配今日收益。
  - dropna() 必做：首尾NaN会污染cumprod()，导致全为NaN。
  - 成本只在信号变化日扣除：用 `diff().fillna(0) != 0` 检测交易日。

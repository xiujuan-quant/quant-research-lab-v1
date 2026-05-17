"""因子生成主程序

执行顺序：读取配置 -> 加载数据 -> 计算因子 -> 构造标签 -> 保存结果 -> 相关性验证
"""

import pandas as pd
from data import load_config, get_path_config, get_factor_config
from factors import calculate_ma, calculate_rsi, calculate_macd


def main() -> None:
    """执行因子生成流程。"""
    # 1. 加载配置
    config = load_config()
    path_config = get_path_config(config)
    factor_config = get_factor_config(config)

    # 2. 获取路径
    processed_data_path = path_config["processed_data_path"]
    factor_data_path = path_config["factor_data_path"]

    # 3. 读取清洗后数据
    df_factor = pd.read_csv(processed_data_path, encoding="utf-8-sig")

    # 4. 依次计算因子（在原表上新增列）
    df_factor = calculate_ma(df_factor,factor_config["ma_windows"])
    df_factor = calculate_rsi(df_factor,factor_config["rsi_window"])
    df_factor = calculate_macd(
        df_factor,
        factor_config["macd_short"],
        factor_config["macd_long"],
        factor_config["macd_signal"],
    )

    # 5. 构造未来收益率标签（T+1 预测目标）
    # shift(-1) 将下一行收盘价上移，最后一行因无未来数据而为 NaN
    df_factor["future_return"] = (
        df_factor["收盘"].shift(-1) / df_factor["收盘"] - 1
    )

    # 6. 保存因子结果表
    df_factor.to_csv(factor_data_path, index=False, encoding="utf-8-sig")

    # 7. 因子与未来收益率相关性分析（探索性参考）
    ma_cols = [f"MA{w}" for w in factor_config["ma_windows"]]
    factor_cols = ma_cols + ["RSI", "MACD"]
    corr = df_factor[factor_cols + ["future_return"]].corr()["future_return"]

    print("\n=== 因子与未来收益率的相关性 ===")
    print(corr)
    print(f"\n因子生成完成，已保存至: {factor_data_path}")
    print(f"最终数据形状: {df_factor.shape}")


if __name__ == "__main__":
    main()
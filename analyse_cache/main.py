import os
import json
from datetime import datetime
import openai

# === 用户配置 ===
input_folder = "/home/hzt/sysinsight/analyse_cache/Pg_analysis_cache"  # 你要处理的文件夹路径
model_name = "gpt-4o"  # 也可以换成 "gpt-5" 或 "gpt-4o"

openai.base_url  = "https://api.vveai.com/v1/"
openai.api_key = "sk-rpITCSUVFqcE5fl28aDd0eB1Ca644a6a8c67876f5d08F8C1"
openai.default_headers = {"x-foo": "true"}

def translate_and_summarize(text):
    """
    调用 OpenAI 接口翻译并简化分析内容。
    """
    prompt = f"""
请将下面的内容翻译成英文，去掉所有类似 <需要提供函数>、<思考过程>、<火焰图采样分析与调优方向> 这样的标志。只输出翻译的结果

原文：
{text}
    """

    response = openai.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "你是一名专业的数据库性能分析助手。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


def process_json_file(file_path):
    """
    读取、翻译、更新 timestamp 并覆盖保存。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "analysis" in data:
        print(f"正在处理: {os.path.basename(file_path)}")
        translated_summary = translate_and_summarize(data["analysis"])
        data["analysis"] = translated_summary
        data["timestamp"] = datetime.now().isoformat()

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"已更新: {file_path}\n")
    else:
        print(f"跳过（未找到 analysis 字段）: {file_path}")


def main():
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(input_folder, filename)
            process_json_file(file_path)


if __name__ == "__main__":
    main()
from dotenv import load_dotenv
import sys
import os
import argparse
import random
from flute.Modules.PromptProcessorFactory import PromptProcessorFactory

def main():
    parser = argparse.ArgumentParser(description="Ponytail command-line interface")
    parser.add_argument("-f", "--file_path", required=True, help="Path to the input file")
    parser.add_argument("-g", "--goal", required=True, help="Goal or objective of the task")
    parser.add_argument("-m", "--model", default="random-fast", help="Name of the model to use")
    parser.add_argument("-r", "--result", default="", help="Additional result or output (optional)")

    args = parser.parse_args()

    file_path = args.file_path
    goal = args.goal
    model = args.model
    result = args.result

    # モデルの選択
    if model == "random-fast":
        fast_models = ["gpt-4o", "claude-3-haiku-20240307", "models/gemini-1.5-flash-latest"]
        selected_model = random.choice(fast_models)
    elif model == "random-accurate":
        accurate_models = ["gpt-4-turbo", "claude-3-opus-20240229", "models/gemini-1.5-pro-latest"]
        selected_model = random.choice(accurate_models)
    else:
        selected_model = model

    # PromptProcessorFactoryクラスを使用してプロンプトプロセッサを作成
    factory = PromptProcessorFactory()
    processor = factory.create_prompt_processor(selected_model)

    # ファイルからプロンプトを読み込む
    with open(file_path, "r") as file:
        prompt = file.read()

    # プロンプトプロセッサを使用してプロンプトを処理
    processed_prompt = processor.process_prompt(prompt, {"goal": goal, "result": result})

    # 処理結果を表示
    print(processed_prompt)

if __name__ == "__main__":
    main()
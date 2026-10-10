# 双语句子对齐工具
import pandas as pd

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines

if __name__ == "__main__":
    src_list = read_txt("input.txt")
    trans_list = read_txt("trans.txt")
    min_len = min(len(src_list), len(trans_list))
    data = {
        "原文": src_list[:min_len],
        "译文": trans_list[:min_len]
    }
    df = pd.DataFrame(data)
    df.to_excel("bilingual_result.xlsx", index=False)
    print("✅ 生成完成：bilingual_result.xlsx")
#（注：内容由AI生成）

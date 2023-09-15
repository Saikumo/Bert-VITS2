import os


def process_folder(folder_path):
    data = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith(".lab"):
            with open(file_path, "r") as f:
                text = f.read().strip()
                wav_file = file_name[:-4] + ".wav"
                wav_path = os.path.join(folder_path, wav_file)
                data.append({"wav_path": wav_path, "text": text})

    return data


def generate_text(wav_path, text):
    return f"{wav_path}|符玄|ZH|{text}"


def save_to_txt(data_list, file_path):
    with open(file_path, "w") as f:
        for data in data_list:
            f.write(data + "\n")


# 示例文件夹路径
folder_path = "raw/fuxuan"

file_data = process_folder(folder_path)

txtList = list()

# 打印每个文件的音频路径和文本
for file in file_data:
    txtList.append(generate_text(file["wav_path"], file["text"]))

file_path = "filelists/fuxuan.txt"
save_to_txt(txtList, file_path)

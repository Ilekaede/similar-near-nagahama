import os

def rename_files_in_folder(folder_path):
    # フォルダ内のファイル一覧を取得
    files = os.listdir(folder_path)
    
    # ファイル名のインデックスを初期化
    index = 1
    
    # 各ファイルに対して処理を実行
    for file_name in files:
        # ファイルのフルパスを取得
        old_file_path = os.path.join(folder_path, file_name)
        
        # ファイルであることを確認
        if os.path.isfile(old_file_path):
            # 新しいファイル名を生成
            new_file_name = f"{index}.jpg"
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # ファイル名を変更
            os.rename(old_file_path, new_file_path)
            
            # インデックスをインクリメント
            index += 1

    print(f"Renamed {index-1} files in '{folder_path}'.")

# フォルダのパスを指定
folder_path = "./img/nagahama-face"

# ファイル名を変更
rename_files_in_folder(folder_path)

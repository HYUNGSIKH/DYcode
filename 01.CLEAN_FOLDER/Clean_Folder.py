import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# 파일을 정리할 기준 폴더 설정
file_categories = {
    "01.PDF": [".pdf"],  
    "02.문서": [".hwp", ".hwpx", ".doc", ".docx", ".txt", ".rtf",
              ".odt", ".tex", ".md", ".log"],  
    "03.엑셀": [".xls", ".xlsx", ".csv", ".xlsm", ".ods", ".tsv"],  
    "04.PPT": [".ppt", ".pptx", ".pps", ".ppsx", ".odp"],  
    "05.ZIP": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz",
               ".tar.gz", ".tar.xz", ".tgz"],  
    "06.IMG": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif",
               ".tiff", ".webp", ".ico", ".heic", ".svg", ".raw", ".psd"],  
    "07.코드": [".for", ".f95", ".f", ".py", ".ipynb", ".exe", ".bat",
              ".sh", ".cpp", ".c", ".h", ".java", ".js", ".html", ".css",
              ".php", ".rb", ".swift", ".go", ".rs", ".kt", ".lua", ".pl",
              ".m", ".sql", ".r", ".scala", ".dart"],  
    "08.CAD": [".dwg", ".dxf", ".plt", ".step", ".stp", ".igs", ".iges"],  
    "09.기타": []
}

# 파일 정리 함수
def organize_files_and_folders(folder_path):
    if not os.path.exists(folder_path):
        messagebox.showerror("오류", "선택한 폴더가 존재하지 않습니다.")
        return
    
    items = os.listdir(folder_path)
    files = [f for f in items if os.path.isfile(os.path.join(folder_path, f))]
    folders = [d for d in items if os.path.isdir(os.path.join(folder_path, d))]

    for file in files:
        file_ext = os.path.splitext(file)[1].lower()
        dest_folder = None
        
        for category, extensions in file_categories.items():
            if file_ext in extensions:
                dest_folder = os.path.join(folder_path, category)
                break
        
        if dest_folder is None:
            dest_folder = os.path.join(folder_path, "09.기타")
        
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        
        shutil.move(os.path.join(folder_path, file), os.path.join(dest_folder, file))

    folders_destination = os.path.join(folder_path, "10.폴더")
    if not os.path.exists(folders_destination):
        os.makedirs(folders_destination)

    for folder in folders:
        folder_full_path = os.path.join(folder_path, folder)
        if folder not in file_categories.keys() and folder != "10.폴더":
            shutil.move(folder_full_path, os.path.join(folders_destination, folder))
    
    messagebox.showinfo("완료", "파일 정리가 완료되었습니다!")

# 폴더 선택 함수
def select_folder():
    folder_selected = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, folder_selected)

# 실행 함수
def start_organizing():
    folder_path = entry_path.get()
    if folder_path:
        organize_files_and_folders(folder_path)
    else:
        messagebox.showwarning("경고", "폴더를 선택하세요.")

# GUI 설정
root = tk.Tk()
root.title("파일 정리 프로그램")
root.geometry("400x120")
root.configure(bg="lightgray")

# UI 요소 생성
label = tk.Label(root, text="정리할 폴더를 선택하세요:", font=("Arial", 12), bg="lightgray")
label.pack(pady=5)

frame = tk.Frame(root, bg="lightgray")
frame.pack()

entry_path = tk.Entry(frame, width=40)
entry_path.pack(side=tk.LEFT, padx=5)

btn_select = tk.Button(frame, text="폴더 선택", command=select_folder, font=("Arial", 10))
btn_select.pack(side=tk.RIGHT)

btn_start = tk.Button(root, text="정리 실행", command=start_organizing, bg="green", fg="white", font=("Arial", 12, "bold"), width=15, height=1)
btn_start.pack(pady=10)

root.mainloop()

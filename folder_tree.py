#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
folder_tree_gui.py

带有简单 GUI 的文件夹树扫描工具，支持排除指定文件或文件模式。
使用 Tkinter 提供的对话框，选择要扫描的文件夹、输出文件路径，
并通过逗号分隔的 glob 模式输入来排除不需要显示的文件或文件夹名。
点击“Scan”按钮即可生成目录结构并保存到指定文件。
"""

import os
import fnmatch
import tkinter as tk
from tkinter import filedialog, messagebox

def scan_folder(path, exclude_patterns, prefix=''):
    """
    递归扫描目录，生成树状结构的每一行文本
    :param path: 要扫描的目录路径
    :param exclude_patterns: 要排除的 glob 模式列表
    :param prefix: 用于缩进和分支符号的前缀
    :return: list of str，每一项是一行输出
    """
    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        return []  # 如果没有权限就跳过

    lines = []
    for index, name in enumerate(entries):
        # 排除匹配任一模式的条目
        if any(fnmatch.fnmatch(name, pat) for pat in exclude_patterns):
            continue

        full_path = os.path.join(path, name)
        connector = '└── ' if index == len(entries) - 1 else '├── '
        lines.append(f"{prefix}{connector}{name}")

        if os.path.isdir(full_path):
            extension = '    ' if index == len(entries) - 1 else '│   '
            lines.extend(scan_folder(full_path, exclude_patterns, prefix + extension))

    return lines

class FolderTreeApp:
    def __init__(self, master):
        self.master = master
        master.title("Folder Tree Scanner")

        # 输入目录选择
        tk.Label(master, text="Source Folder:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.src_entry = tk.Entry(master, width=50)
        self.src_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(master, text="Browse…", command=self.browse_folder).grid(row=0, column=2, padx=5, pady=5)

        # 输出文件选择
        tk.Label(master, text="Output File:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.out_entry = tk.Entry(master, width=50)
        self.out_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(master, text="Browse…", command=self.browse_output).grid(row=1, column=2, padx=5, pady=5)

        # 排除模式输入
        tk.Label(master, text="Exclude Patterns:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.exclude_entry = tk.Entry(master, width=50)
        self.exclude_entry.insert(0, "*.hash,*.tmp")  # 默认示例
        self.exclude_entry.grid(row=2, column=1, padx=5, pady=5)
        tk.Label(master, text="(comma-separated globs)").grid(row=2, column=2, sticky="w")

        # 扫描按钮
        self.scan_button = tk.Button(master, text="Scan", width=15, command=self.scan_and_save)
        self.scan_button.grid(row=3, column=1, pady=10)

        master.columnconfigure(1, weight=1)

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Folder to Scan")
        if folder:
            self.src_entry.delete(0, tk.END)
            self.src_entry.insert(0, folder)

    def browse_output(self):
        file = filedialog.asksaveasfilename(
            title="Select Output TXT File",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file:
            self.out_entry.delete(0, tk.END)
            self.out_entry.insert(0, file)

    def scan_and_save(self):
        folder = self.src_entry.get().strip()
        output = self.out_entry.get().strip()
        patterns = [p.strip() for p in self.exclude_entry.get().split(',') if p.strip()]

        if not folder or not os.path.isdir(folder):
            messagebox.showerror("Error", "Please select a valid source folder.")
            return
        if not output:
            messagebox.showerror("Error", "Please select an output file path.")
            return

        try:
            lines = [folder]
            lines += scan_folder(folder, patterns)
            with open(output, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            messagebox.showinfo("Success", f"Directory tree written to:\n{output}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

def main():
    root = tk.Tk()
    app = FolderTreeApp(root)
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()

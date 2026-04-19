"""
任务一：模拟配置备份与过期清理
网络工程师经常需要定期备份设备配置，并清理过期的备份文件。请编写一个脚本，模拟这个过程：

在脚本同级目录下创建一个 backup/ 文件夹（如果不存在则创建）。
使用 while True: 循环，每隔 3秒 在 backup/ 目录下生成一个备份文件，文件名为 backup_YYYY-MM-DD_HH-MM-SS.txt。
每次生成新文件后，检查 backup/ 目录下所有的备份文件。
如果发现某个文件的生成时间距离当前时间 超过 15 秒，则将其删除（即只保留最近 15 秒内的备份，最多 5 个）。
每次循环打印出：新创建了哪个文件、删除了哪个文件（如果有）、以及当前保留的所有文件列表。
捕获 KeyboardInterrupt 异常，当用户按下 Ctrl+C 停止程序时，把 backup/ 目录下所有剩余的备份文件全部清理干净，并删除 backup/ 目录，优雅退出。
代码提示（可以参考以下框架）：
"""


import os
import time
from datetime import datetime, timedelta

def main():
    # 1. 确定备份目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    backup_dir = os.path.join(base_dir, 'backup')
    
    # 如果目录不存在则创建
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    print(f"开始模拟备份，目录: {backup_dir}")
    print("按 Ctrl+C 停止并清理...")
    
    try:
        while True:
            # 2. 获取当前时间并生成备份文件
            now = datetime.now()
            now_str = now.strftime('%Y-%m-%d_%H-%M-%S')
            filename = f"backup_{now_str}.txt"
            filepath = os.path.join(backup_dir, filename)
            
            # 使用 with open 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"备份时间: {now_str}\n")
                f.write(f"设备配置模拟数据...\n")
            print(f"\n[+] 创建备份: {filename}")
            
            # 3. 计算 15 秒前的时间基准
            expire_time = now - timedelta(seconds=15)
            
            # 4. 遍历备份目录，找出过期文件并删除
            current_files = []
            delete_files = []
            for file in os.listdir(backup_dir):
                if file.startswith('backup_') and file.endswith('.txt'):
                    # 从文件名提取时间字符串
                    time_str = file.replace('backup_', '').replace('.txt', '')
                    # 将字符串转换回 datetime 对象进行比较
                    file_time = datetime.strptime(time_str, '%Y-%m-%d_%H-%M-%S')
                    
                    # 比较时间，如果过期则删除，否则加入 current_files 列表
                    if file_time < expire_time:
                        delete_files.append(file)
                        os.remove(os.path.join(backup_dir, file))
                    else:
                        current_files.append(file)

            
            # 5. 打印当前保留的所有备份文件
            print(f"[*] 当前保留的备份 ({len(current_files)}个):")
            for f in sorted(current_files):
                print(f"    - {f}")
                
            # 6. 休眠 3 秒
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\n\n收到停止信号，正在清理所有备份文件...")
        # 遍历目录，删除所有 backup_ 开头的 txt 文件
        for file in os.listdir(backup_dir):
            if file.startswith('backup_') and file.endswith('.txt'):
                os.remove(os.path.join(backup_dir, file))
                print(f"[-] 已清理: {file}")
        # 最后删除 backup_dir 目录本身 (os.rmdir)
        os.rmdir(backup_dir)
        print("[-]已删除 backup 目录")

        print("清理完成，程序退出。")

if __name__ == '__main__':
    main()
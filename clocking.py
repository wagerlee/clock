import time

def focus_clock(minutes):
    print("专注模式开始")
    seconds = minutes * 60  # 将分钟转换为秒
    start_time = time.time()  # 记录开始时间
    end_time = start_time + seconds  # 计算结束时间
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())  # 计算剩余秒数
        minutes = remaining_seconds // 60  # 计算剩余分钟
        seconds = remaining_seconds % 60  # 计算剩余秒数
        
        # 显示剩余时间
        print(f"剩余时间: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)  # 暂停1秒
    
    print("专注模式结束")

# 使用示例：设置专注时间为25分钟
focus_clock(25)

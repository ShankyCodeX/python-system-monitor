from datetime import datetime
import psutil
utc = datetime.now()
stats_cpu= psutil.cpu_percent(interval=None)
memory = psutil.virtual_memory()
file_path ="system-log.txt"
with open(file_path, "w") as file:
     file.write(f'{utc} -Cpu:{stats_cpu} % -Ram:{memory.percent} %')



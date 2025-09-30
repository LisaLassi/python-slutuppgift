import psutil
import time

#Testar olika funktioner med psutil
'''
# CPU-användning
cpu_usage = psutil.cpu_percent(interval=1)
# RAM-användning
memory = psutil.virtual_memory()
# Antal processer
processes = len(psutil.pids())

print("=" * 40)
print(f"CPU-användning: {cpu_usage}%")
print(f"RAM-användning: {memory.percent}% {memory.used // (1024**2)} MB av {memory.total // (1024**2)} MB")
print(f"Aktiva processer: {processes}")
print("=" * 40)
'''
old_net = psutil.net_io_counters()
while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    # Diskanvändning
    disk = psutil.disk_usage('/')
    # Nätverk (bytes skickade/mottagna)
   #net = psutil.net_io_counters()
    processes = len(psutil.pids())
    # Nätverk (räkna ut skillnaden mellan nu och föregående loop)
    new_net = psutil.net_io_counters()
    sent_speed = (new_net.bytes_sent - old_net.bytes_sent) / (1024**2) # MB/s
    recv_speed = (new_net.bytes_recv - old_net.bytes_recv) / (1024**2) # MB/s
    old_net = new_net

    print("=" * 50)
    print(f"CPU-användning: {cpu_usage}%")
    print(f"RAM-användning: {memory.percent}% "
          f"{memory.used // (1024**2)} MB av {memory.total // (1024**2)} MB")
    print(f"Disk-användning: {disk.percent}"
          f"{disk.used // (1024**3)} GB av {disk.total // (1024**3)} GB")
    '''
    print(f"Nätverk - skickat: {net.bytes_sent // (1024**2)} MB, "
          f"mottaget: {net.bytes_recv // (1024**2)} MB")
    '''
    print(f"Nätverkshastighet - upp: {sent_speed:.2f} MB/s"
          f"ner: {recv_speed:.2f} MB/s")


    print(f"Aktiva processer: {processes}")
    print("=" * 50)

    # Vänta (x)antal sekunder innan nästa uppdatering
    time.sleep(2)
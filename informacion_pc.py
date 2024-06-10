import platform
import psutil
import os
def get_system_info():
    # Información del sistema operativo
    system = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    
    # Información de la CPU
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    cpu_usage = psutil.cpu_percent(interval=1)

    # Información de la memoria
    virtual_mem = psutil.virtual_memory()

    # Información del disco
    disk_partitions = psutil.disk_partitions()

    # Información de la red
    net_io = psutil.net_io_counters()

    # Información del usuario actual
    user = os.getlogin()
    
    # Imprimir la información obtenida
    print(f"Usuario: {user}")
    print(f"Sistema operativo: {system}")
    print(f"Nombre del equipo: {node}")
    print(f"Versión del SO: {release} ({version})")
    print(f"Arquitectura: {machine}")
    print(f"Procesador: {processor}")
    print(f"Núcleos físicos: {cpu_count}")
    print(f"Núcleos lógicos: {cpu_count_logical}")
    print(f"Frecuencia de la CPU: {cpu_freq.current} MHz")
    print(f"Uso de CPU: {cpu_usage}%")
    print(f"Memoria total: {virtual_mem.total / (1024 ** 3):.2f} GB")
    print(f"Memoria disponible: {virtual_mem.available / (1024 ** 3):.2f} GB")
    print(f"Uso de memoria: {virtual_mem.percent}%")
    print(f"Particiones de disco:")
    for partition in disk_partitions:
        print(f"  {partition.device}:")
        print(f"    Montado en: {partition.mountpoint}")
        print(f"    Tipo de sistema de archivos: {partition.fstype}")
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"    Tamaño total: {usage.total / (1024 ** 3):.2f} GB")
        print(f"    Espacio usado: {usage.used / (1024 ** 3):.2f} GB")
        print(f"    Espacio libre: {usage.free / (1024 ** 3):.2f} GB")
        print(f"    Uso: {usage.percent}%")
    print(f"Red:")
    print(f"  Bytes enviados: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
    print(f"  Bytes recibidos: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

if __name__ == "__main__":
    get_system_info()

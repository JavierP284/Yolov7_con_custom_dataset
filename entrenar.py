import subprocess

# Cambia las rutas según tu estructura local
subprocess.run([
    "python", "yolov7/train.py",
    "--batch", "16",
    "--epochs", "125",
    "--cfg", "yolov7/cfg/training/yolov7.yaml",
    "--data", "Resistencias/data.yaml",
    "--weights", "yolov7_training.pt",
    "--device", "0"
])
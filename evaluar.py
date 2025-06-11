import subprocess

# Ejecuta la evaluación
subprocess.run([
    "python", "yolov7/detect.py",
    "--weights", "runs/train/exp/weights/best.pt",
    "--conf", "0.1",
    "--source", "Resistencias/test/images"
])
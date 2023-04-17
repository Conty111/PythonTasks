"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os

sym = "ak;snfqwofjb124"

os.chdir(os.getcwd() + "/target")
for i in range(1, 11):
    os.rename(
        os.getcwd() + f"/{i}", os.getcwd() + f"/{sym[i - 1]}{i * 214}{sym[i + 1]}"
    )

@echo off
for /l %%x in (1, 1, 25) do (
mkdir "day%%x"
break>C:\Users\Sven\Documents\AoC\2024\"day%%x"\"data.txt"
break>C:\Users\Sven\Documents\AoC\2024\"day%%x"\"day%%x.py"
break>C:\Users\Sven\Documents\AoC\2024\"day%%x"\"day%%x_part2.py"
)
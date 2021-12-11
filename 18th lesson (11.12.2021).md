# 18th lesson (11.12.2021)

https://realpython.com/primer-on-python-decorators/ </p>
https://adventofcode.com/2021/day/2

def load_lines(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        commands = file.readlines()
    lst = []
    for i in commands:
        lst.append(i.rstrip("\n"))
    return lst
def load_lines_v2(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        lines = file.readlines()
        lst = [line.rstrip("\n") for line in lines]
        return lst
def load_lines_v3(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file.readlines()]
    
print(load_lines_v3("day2.txt"))

# 18th lesson (11.12.2021)

https://realpython.com/primer-on-python-decorators/ </p>
https://adventofcode.com/2021/day/2

```Py
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
```

```Py
lines = load_lines("day2.txt")
​
instruction_line = lines[0]
print(instruction_line)
​
​
def parse_line_as_tuple(line: str) -> tuple[str, int]:
    split_by_spaces = line.split()
    return (split_by_spaces[0], int(split_by_spaces[1]))
​
​
def parse_line_as_list(line: str) -> list:
    split_by_spaces = line.split()
    return [split_by_spaces[0], int(split_by_spaces[1])]
​
​
def parse_line_as_dict(line: str) -> dict:
    split_by_spaces = line.split()
    instruction = {"direction": split_by_spaces[0], "units": int(split_by_spaces[1])}
    return instruction
​
​
# print(parse_line_as_tuple(instruction_line))
# print(parse_line_as_list(instruction_line))
# print(parse_line_as_dict(instruction_line))
​
​
def load_and_parse(file_name: str) -> list[tuple]:
    return [parse_line_as_tuple(line) for line in load_lines(file_name)]
​
​
# print(load_and_parse("day2.txt"))
​
​
class Direction(enum.Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"
​
​
direction1 = Direction("forward")
​
print(direction1)
​
if direction1 is Direction.DOWN:
    print("Jdeme dolu!")
else:
    print("Jdeme dopredu nebo nahoru!")
​
# Enum tridy chrani pred spatnym vstupem - at uz umyslne nebo neumyslne zadanym!
try:
    direction2 = Direction("forwerd")
except ValueError:
    print("Spatny smer!")
​
​
def parse_line_as_tuple_with_enum(line: str) -> tuple[Direction, int]:
    split_by_spaces = line.split()
    return (Direction(split_by_spaces[0]), int(split_by_spaces[1]))
​
​
print(parse_line_as_tuple_with_enum(instruction_line))
```

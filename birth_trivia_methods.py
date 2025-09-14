import random
from dataclasses import dataclass

@dataclass
class ChildName:
    name: str
    sex: str
    count: int
    year: int

@dataclass
class TriviaQ:
    question: str
    answer: int


def get_random_record(file_path: str) -> ChildName:
    # get total lines
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line = random.choice(lines).strip()

    name, sex, count, year = line.split(",")
    return ChildName(
        name=name,
        sex=sex,
        count=int(count),
        year=int(year)
    )

def create_trivia_q(name: ChildName) -> TriviaQ:
    return TriviaQ(
        question=f"In the year {name.year}, how many {name.sex} children were given the name {name.name}?",
        answer=name.count
    )

if __name__ == "__main__":
    # probably use the method to pull trivia qs from
    record = get_random_record("all_yob.txt")
    print(record)
    question = create_trivia_q(record)
    print(question)

import re


from typing import Any, Callable, IO, List, Tuple, Union

TRow = List[Union[int, None]]
TBoard = List[TRow]
TBoards = List[TBoard]


def parse_called_numbers(input_file: IO) -> List[int]:
    return [int(x) for x in input_file.readline().split(",")]


def parse_board_row(input_file: IO) -> TRow:
    return [int(x) for x in re.findall(r"(\d{1,2})", input_file.readline())]


def parse_board(input_file: IO) -> TBoard:
    return [parse_board_row(input_file) for _ in range(5)]


def parse_boards(input_file: IO) -> TBoards:
    boards: TBoards = list()
    while True:
        if not input_file.readline():
            return boards
        boards.append(parse_board(input_file))


def parse(input_file: IO) -> Tuple[List[int], TBoards]:
    called_numbers = parse_called_numbers(input_file)
    return called_numbers, parse_boards(input_file)


def update_board(board: TBoard, called_number: int) -> None:
    for row in board:
        for col_idx, board_value in enumerate(row):
            if board_value == called_number:
                row[col_idx] = None


def is_winning_board(board: TBoard) -> bool:
    def _helper(board_accessor: Callable[[int, int], Union[int, None]]) -> bool:
        for x_1 in range(5):
            for x_2 in range(5):
                if board_accessor(x_1, x_2) is not None:
                    break
            else:
                return True
        return False

    return _helper(lambda x_1, x_2: board[x_1][x_2]) or _helper(
        lambda x_1, x_2: board[x_2][x_1]
    )


def board_score(board: TBoard) -> int:
    return sum(sum(x for x in row if x is not None) for row in board)


def pretty_print_board(board: TBoard) -> None:
    for row in board:
        mod_row = [str(x) if x is not None else "NA" for x in row]
        print("{:<2s} {:<2s} {:<2s} {:<2s} {:<2s}".format(*mod_row))


def p_1(input_file: IO, debug: bool = False) -> Any:
    called_numbers, boards = parse(input_file)
    for called_number in called_numbers:
        for board in boards:
            update_board(board, called_number)
            if is_winning_board(board):
                return called_number * board_score(board)


def p_2(input_file: IO, debug: bool = False) -> Any:
    called_numbers, boards = parse(input_file)
    winning_boards = set()
    for called_number in called_numbers:
        for board_idx, board in enumerate(boards):
            update_board(board, called_number)
            if is_winning_board(board):
                winning_boards.add(board_idx)
                if len(winning_boards) == len(boards):
                    return called_number * board_score(board)

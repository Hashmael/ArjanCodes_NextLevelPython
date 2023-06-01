import os
import io
import random
import string
import typing
import pathlib
import contextlib

RETAIN_TEST_FILE = False
TEST_FILE_PATH = pathlib.Path(__file__).with_name('context_manager_test.txt')
MODES = typing.Literal['r', 'w']
FILE_MANAGER_TYPE = typing.Callable[[os.PathLike, MODES], io.TextIOWrapper]

@contextlib.contextmanager
def utf8_text_file_manager(file_path: os.PathLike, mode: MODES = 'r') -> io.TextIOWrapper:
    file = None
    try:
        file = open(file_path, mode=mode, encoding='utf8', newline='\n')
        yield file
    finally:
        if file:
            file.close()

def random_printable_line() -> str:
    return ''.join(random.choices(string.printable, k=random.choice(range(50))))

def main() -> None:
    sample_text = '\n'.join(random_printable_line() for _ in range(random.choice(range(50))))
    with utf8_text_file_manager(TEST_FILE_PATH, mode='w') as text_file:
        text_file.write(sample_text)
    assert text_file.closed
    print('Context manager closes file after exiting from write context')
    with utf8_text_file_manager(TEST_FILE_PATH, mode='r') as text_file:
        read_sample_text = text_file.read()
    assert text_file.closed
    print('Context manager closes file after exiting from read context')
    assert sample_text == read_sample_text
    print('Context manager successfully re-reads sample text written to file without alteration')
    if not RETAIN_TEST_FILE:
        os.remove(TEST_FILE_PATH)

if __name__ == '__main__':
    main()
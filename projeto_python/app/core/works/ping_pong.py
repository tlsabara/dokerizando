def ping_get() -> str:
    return 'WANNA PLAY? THEN, PING ON POST!'


def ping_post(simple_word: str) -> str:
    return 'PONG POST' if simple_word.upper() == 'PING' else "???"

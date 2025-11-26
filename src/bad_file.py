def thisIsaBADFunction() -> dict:
    too_long_text = "THIS IS MY LONG TEXT -- THIS IS MY LONG TEXT --THIS IS MY LONG TEXT --THIS IS MY LONG TEXT --THIS IS MY LONG TEXT --THIS IS MY LONG TEXT --THIS IS MY LONG TEXT "

    return too_long_text.split("--")[0].strip().lower()

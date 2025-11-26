def thisIsaBADFunction() -> dict:
    unused_variable = 1234
    too_long_text = "THIS IS MY LONG TEXT -- THIS IS MY LONG TEXT --THIS IS MY LONG TEXT --THIS IS MY LONG TEXT --THIS IS MY LONG TEXT --THIS IS MY LONG TEXT --THIS IS MY LONG TEXT "

    return too_long_text.split("--")[0].strip().lower()




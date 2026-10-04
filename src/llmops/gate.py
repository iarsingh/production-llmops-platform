class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    for key in ("prompt_version", "eval_passed", "cost_ok"):
        if not body.get(key): failed.append(key)
    return {"passed": not failed, "failed": failed, "applied": False}

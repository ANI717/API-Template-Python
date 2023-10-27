def get_full_name(inputs):
    full_name = "{} {}".format(inputs.get("first_name"),
                               inputs.get("last_name"))
    return {"full_name": full_name}

"""Contains a function for returning the oldest billionaire under 80
and the youngest billionaire from Forbes' top 40 billionaires list."""


def find_billionaires(file_name="forbes.json"):
    """Return the name of the youngest billionaire and the oldest under 80
    from Forbes' list of top 40 billionaires."""
    import json
    with open(file_name, "r") as bills:
        lst = json.load(bills)
    valid = [bill for bill in lst if bill["age"] > 0 and bill["age"] < 80]
    if valid:
        youngest = min(valid, key=lambda x: x["age"])
    else:
        youngest = None
    under_80 = [bill for bill in valid if bill["age"] < 80]
    if under_80:
        oldest = max(under_80, key=lambda x: x["age"])
    else:
        oldest = None
    msg = ""
    if youngest:
        msg += "\nyoungest billionaire:\nname: {0}:\nnet worth: {1}\nindustry: {2}\n".format(
            youngest["name"],
            youngest["net_worth (USD)"],
            youngest["source"]
        )
    if oldest:
        msg += "\noldest billionaire under 80:\nname: {0}:\nnet worth: {1}\nindustry: {2}\n".format(
            oldest["name"],
            oldest["net_worth (USD)"],
            oldest["source"]
        )
    if msg:
        return msg
    else:
        return "There are no billionaires!"


if __name__ == "__main__":
    print(find_billionaires())

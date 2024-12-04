def inference_engine(knowledge_base, facts):
    """
    Inference engine: Returns all possible conclusions, sorted by match rate
    """
    mutually_exclusive_conditions = [
        ("The power indicator isn't working", "The power indicator is working")
    ]

    for condition_pair in mutually_exclusive_conditions:
        if all(condition in facts for condition in condition_pair):
            return ("Error：'The power indicator isn't working'\n&\n'The power indicator is working'\n"
                    "cannot show together！")

    results = []

    rules = knowledge_base.get("rules", [])

    for rule in rules:
        match_count = sum(1 for condition in rule["if"] if condition in facts)
        score = match_count / len(rule["if"])

        if score > 0:
            results.append({"conclusion": rule["then"], "score": score})

    if results:
        results.sort(key=lambda x: x["score"], reverse=True)

        for result in results:
            if result["score"] == 1.0:
                return f"Possibility: {result['conclusion']} (Match-degree: 100%)"

        output = []
        for result in results:
            output.append(f"Possibility: {result['conclusion']} (Match-degree: {result['score']:.0%})")
        return "\n".join(output)

    return "Infer Failed"
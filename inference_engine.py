def inference_engine(knowledge_base, facts):
    """
    推理引擎：返回所有可能的结论，按匹配率排序
    """
    mutually_exclusive_conditions = [
        ("电源指示灯亮", "电源指示灯不亮")
    ]

    for condition_pair in mutually_exclusive_conditions:
        if all(condition in facts for condition in condition_pair):
            return "错误：电源指示灯亮&电源指示灯不亮互斥\n不能同时出现！"

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
                return f"可能的原因: {result['conclusion']} (匹配率: 100%)"

        output = []
        for result in results:
            output.append(f"可能的原因: {result['conclusion']} (匹配率: {result['score']:.0%})")
        return "\n".join(output)

    return "推理失败"
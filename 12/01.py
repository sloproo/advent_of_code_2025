def pitkanimi(joo: str, hoo: list[int]):
    return joo + "".join(str(i) for i in hoo)
print(pitkanimi("jooasfasf", [4, 5, 6]))

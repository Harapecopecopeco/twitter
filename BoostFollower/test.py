def generate():
    print("Generate function")
    for n in range(1):
        yield n
        print("Yield")


gen = generate()

def parser():
    with open("logs.txt", 'r', encoding='utf-8') as file:
        text = file.readlines()
        result = []
        memory = 0
        for line in text:
            if "===" in line:
                result.append(memory)
                memory = 0
            if len(line) > 1 and line[11].isdigit():
                end = line.find("MiB")
                memory += float(line[11:end-1])
        result.append(memory)
        result.pop(0)
        return result

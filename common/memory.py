memory_store = []

def save_memory(entry):
    memory_store.append(entry)

def get_memory():
    return "\n".join(memory_store[-5:])
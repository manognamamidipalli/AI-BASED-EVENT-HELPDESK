def add_message(messages, role, content):
    messages.append({
        "role": role,
        "content": content
    })


def get_conversation(messages):
    conversation = ""

    for message in messages:
        role = message["role"].capitalize()
        content = message["content"]

        conversation += f"{role}: {content}\n"

    return conversation
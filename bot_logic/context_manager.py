
def update_context(context, user_input):
    if 'tech' in user_input.lower() or 'stack' in user_input.lower():
        context['stage'] = 'tech_questions'
    return context

def check_exit(user_input):
    exit_keywords = ['exit', 'quit', 'bye', 'stop', 'end']
    return any(keyword in user_input.lower() for keyword in exit_keywords)

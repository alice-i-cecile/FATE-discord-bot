# generates a validation function that checks if a message has the same author and channel as a given context
def same_author_channel(ctx): 
    def f(message):
        return ctx.author == message.author and ctx.channel == message.channel
    return f

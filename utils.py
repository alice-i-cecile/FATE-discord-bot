# generates a validation function that checks if a message has the same author and channel as a given context
def same_author_channel(ctx): 
    def f(message):
        return ctx.author == message.author and ctx.channel == message.channel
    return f
    
class Fillable:
    """
    Helper class for tracking all sorts of stats.
    For example, "your xp bar is at 50/80"
    """
    def __init__(self, max, current=0):
        self.max = max
        self.current = current    
        
    def increment(n=1):
        self.current = min(self.max, current+n)
        return self.max == self.current
        
    def decrement(n=1):
        self.current = max(0, current-n)
        return 0 == self.current
    

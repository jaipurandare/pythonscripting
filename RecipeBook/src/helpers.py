from functools import wraps

def log_recipe_action(action):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            recipe_name = args[0].name or None
            print(f"{action.upper()} Recipe {recipe_name} in {self.name} book")
            return result
        return wrapper
    return decorator


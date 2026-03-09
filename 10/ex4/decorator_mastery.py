from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()

        tracker = func(*args, **kwargs)

        end = time.time()
        print(f"Spell completed in {round(end - start, 3)} seconds")
        return tracker
    
    return wrapper


def power_validator(min_power: int) -> callable:
    def cast_spell(func):
        @wraps(func)
        def wrapper(self, spell_name, power):
            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(self, spell_name, power)
            
        return wrapper
        
    return cast_spell



def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            tries = 1
            try:
                return func(max_attempts)
            except:
                for tries in max_attempts:
                    if tries < max_attempts:
                        print(f"Spell failed, retrying... (attempt {tries}/{max_attempts})")
                    else:
                        return f"Spell casting failed after {max_attempts} attempts"
            return wrapper
        return decorator

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3 and name.isalpha():
            return True
        else:
            return False
    

    @staticmethod
    @cast_spell(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
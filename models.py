from utils import *

class Stunt:
    """
    Class representing a single stunt.
    Mostly just bundling information together.
    Theres an OOP word for that but I don't remember what it is.
    """
    def __init__(self, name, refresh_cost, activation_cost, recharge_period, description):
        self.name = name
        self.refresh_cost = ref
        self.activation_cost = activation_cost
        self.recharge_period = recharge_period
        self.description = description
        self.on_cooldown = False
        
class Game:
    """
    A parent class for holding characters and scenes to be used together,
    as well as storing the rule configuration for the game.
    """
    def __init__(self, name, current_issues, impending_issues, aspects, kill_cap, character_refresh, character_initial_stunts, stress_tracks, default_stress_boxes, default_consequence_slots, skill_list, character_initial_skill_points, initiative_skills, stress_skills):
        self.name = name # unique name
        self.characters = list() # Character
        self.scenes = list() # Scene
        self.current_issues = current_issues # list of strings
        self.impending_issues = impending_issues # list of strings
        self.aspects = aspects # list of strings
        self.skill_cap = skill_cap # int
        self.character_refresh = character_refresh # int
        self.character_initial_stunts = character_initial_stunts # int
        self.stress_tracks = stress_tracks # list of strings
        self.default_stress_boxes = default_stress_boxes # dictionary
        self.default_consequence_slots = default_consequence_slots
        self.skill_list = skill_list # list of strings
        self.character_initial_skill_points = character_initial_skill_points # int
        self.initiative_skills = initiative_skills # dictionary
        self.stress_skills = stress_skills # dictionary 
    
    @classmethod
    def create(cls, args):
        if isinstance(args, str): # assume game name, initiate interactive prompt
            print("Interactive prompt!") # TODO: write this later i guess
        elif isinstance(args, list):
            return cls(*args)
        elif isinstance(args, dictionary):
            return cls(**args)
        elif isinstance(args, Game):
            return args # TODO: check if this actually makes a copy- i feel like it doesn't
        else:
            print("Improper usage. Expected string, list, dictionary, or Game")
            
    @classmethod
    def load(cls, directory_name): # load an existing game from a directory 
        pass # TODO
    
    def same_uid(self, other):
        return self.name == other.name
    
    def __str__(self):
        # TODO: write this function. something to be called by !fields on game objects
        return 'name: ' + self.name

class Scene:
    """
    Class representing a Scene for a character to play in.
    """
    def __init__(self, name, aspects):
        self.name = name        # string
        self.aspects = aspects  # list of strings
        self.challenges = list()# list of Challenges
        self.contests = list()  # list of Contests
        self.conflicts = list() # list of Conflicts
        
    @classmethod
    def create(cls, args):
        if isinstance(args, list):
            return cls(*args)
        elif isinstance(args, dictionary):
            return cls(**args)
        elif isinstance(args, Scene):
            return args # TODO: check if this actually makes a copy- i feel like it doesn't
        else:
            print("Improper usage. Expected list, dictionary, or Scene")
            
    @classmethod
    def load(cls, filename): # load an existing scene from a file
        pass # TODO
        
    def same_uid(self, other):
        return self.name == other.name
        
class Characer:
    """
    Class representing a character, either playable or an npc.
    Requires a Game instance to get appropriate rules information.
    """
    def __init__(self, name, pc, description, aspepcts, skills, stunts, extras, current_refresh, game):
        # simple copies
        self.name = name                    # unique name
        self.player_characer = pc           # bool
        self.description = description      # string
        self.aspects = aspects              # list of strings
        self.skills = skills                # {Game.skill_list: int}
        self.extras = extras                # list of strings
        self.fate_points = current_refresh  # int
        
        # STZ is a powerful instruction for the 65816, allowing you to set a memory address to zero without having to first load zero to the accumulator
        self.boosts = 0
        self.invoke_count = 0 # this is only used behind the scenes for tracking invokes on upcoming rolls
        self.free_invocations = {}
        for aspect in aspects:
            self.free_invocations[aspect] = 0
        
        # parsing and conversion
        if isinstance(stunts, list): # if we get a list of stunts, convert to a dictionary
            self.stunts = {}
            for stunt in stunts:
                self.stunts[stunt.name] = stunt # i'm like 90% sure this will work
        else:
            self.stunts = stunts
        
        # stuff based on game rules
        self.refresh = Fillable(game.character_refresh, current_refresh)
        self.stress = {}
        for stress_type in game.stress_tracks:
            self.stress[stress_type] = Fillable(game.default_stress_boxes)
        self.consequence_slots = {}
        for slot in game.default_consequence_slots.keys():
            self.consequence_slots[slot] = ''    

    @classmethod
    def create(cls, args):
        if isinstance(args, list):
            return cls(*args)
        elif isinstance(args, dictionary):
            return cls(**args)
        elif isinstance(args, Character):
            return args # TODO: check if this actually makes a copy- i feel like it doesn't
        else:
            print("Improper usage. Expected string, list, dictionary, or Character")
            
    @classmethod
    def load(cls, filename): # load an existing scene from a file
        pass # TODO
        
    def same_uid(self, other):
        return self.name == other.name

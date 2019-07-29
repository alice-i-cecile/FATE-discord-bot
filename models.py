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
        if isinstance(args, str): # assume filename, parse file and generate
            pass # TODO: write this later i guess
        elif isinstance(args, (list, tuple)):
            return cls(*args)
        elif isinstance(args, dictionary):
            return cls(**args)
        elif isinstance(args, Game):
            return args # TODO: check if this actually makes a copy- i feel like it doesn't
        else:
            pass # TODO: interactive prompt here
            
    @classmethod
    def load(cls, directory_name): # load an existing game from a directory 
        pass # TODO
    
    def __str__(self):
        # TODO: write this function. something to be called by !fields on game objects
        return 'name: ' + self.name

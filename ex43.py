from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died, you suck at this!"

        "Such a loser"

        "Are you a theb?"

        "Are you even trying??"
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
            The Gothons of PP#25 have invaded your ship and destroyed your crew
            You are the last surviving member and you mission is to get a neuron destruct
            bomb onto the ship of the aliens to avenge your crew members.

            You're running down the central corridor to get to the weapons armory to obtain the bomb
            when you are cut off by an alien, he blocking the door. What do you do?"""))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you pull out your gun and fire towards the alien.
                He absorbs all of the bullets you fire. You get your phaser to stunself.
                You fire at the alien. The alien changes into a woman in an elegant sparkling ballgown
                with pincurls. Whoops! Looks like phaser was set to stunning!! The woman grabs you by the shoulders
                and bites your head off."""))
            return 'death'
        elif action =="dodge!":
            print(dedent("""
                You go to dodge the alien but they can presense the direction you're going to go in.
                They bite your head off"""))
            return 'death'
        elif action == "tell a joke!":
            print(dedent("""
                You tell a joke, it appears to be successful! As the alien laughs, the shaking causes it's liquid body
                to break down. The alien has laughed themseleves to death!"""))
            return 'laser_weapon_armory'
        else:
            print("Does not compute, try again!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the armory room. There are no aliens
            You begin to search frantically from the neutron bomb.
            You locate it in a box. There appears to be a digit pad and a screen.
            On the screen are three flashing stars and 10 dots. You quickly realise that the dots are the allowed attempts
            You begin to type in numbers
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZED!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open like a ringpull can and the seal breaks with a tsssh....
                You slowly lift the neutron bomb out of the container and run towards the bridge to plant itself.
                """))
            return 'the_bridge'

        else:
            print(dedent("""
                The lock buzzes one last time and you hear a melting sound
                as the container begins to weld itself shut. You have failed to avenge your comrades.
                You raise your gun to your head and it's not set to 'stun'. You stare
                at your reflection in the metal container before....
                *bang*
                """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You kick down the door with the ghost force of 100 comrades behind you.
            The neuron bomb is under your arm, you manage to take the aliens by surpise
            and they have no time to react as you take the bomb into the centre of the ropom. They pull the weapons and take aim at you and the bomb.
            """))

        action = input("> ")

        if action == 'dodge':
            print(dedent("""
                In a panic, you manage to dodge the oncoming fire and shut the door to the bridge.
                You hear the bomb explode within the control room, however you didn't account for the
                bridge doors exploding. They force you backwards within the ship and you
                end up becomming impaled on part of the skewed metal door.
                """ ))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                You point the blaster at the bomb
                blah blah blah this is all just storyline and text.
                I am just creating this to test myself
                Doesn't matter what gets typed here
                seashells
                she sells seashells
                on the
                sea whore
                theb
                blahhh more blahhh
                let's go to the ecape pods   """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            Rushing through the ship to make it to the escape pod before it explodes.
            There are 5 pods, which pod do you take??
            """ ))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The hull ruptures as you're projected into space.
                """  ))
            return 'death'
        else:
            print(dedent("""
                you jump into pod {guess} and hit the eject button.
                you manage to escape and view the alien ship explode as you fly away.
                You won!
                """ ))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job!!")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death': Death(),
        'finished' : Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

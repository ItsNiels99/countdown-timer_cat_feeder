def on_button_pressed_a():
    global Seconds
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    Seconds += 10
    basic.show_number(Seconds)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global Seconds
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    while Seconds > 0:
        basic.show_number(Seconds)
        basic.pause(1000)
        Seconds += -1
    if Seconds == 0:
        for index in range(5):
            music.play_tone(523, music.beat(BeatFraction.QUARTER))
            music.rest(music.beat(BeatFraction.EIGHTH))
            music.play_tone(523, music.beat(BeatFraction.QUARTER))
            music.rest(music.beat(BeatFraction.WHOLE))
            servos.P0.run(50)
            basic.show_icon(IconNames.SMALL_DIAMOND)
        servos.P0.set_angle(90)
        servos.P0.set_stop_on_neutral(False)
        basic.show_leds("""
            . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global Seconds
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    Seconds = 0
    basic.show_number(Seconds)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Seconds
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    Seconds += 1
    basic.show_number(Seconds)
input.on_button_pressed(Button.B, on_button_pressed_b)

Seconds = 0
basic.show_leds("""
    . . . . .
        . . # . .
        . . . . .
        . . . . .
        . . . . .
""")
Seconds = 0
servos.P0.set_angle(90)
servos.P0.set_stop_on_neutral(True)
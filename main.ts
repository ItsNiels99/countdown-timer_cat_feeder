input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    music.playTone(523, music.beat(BeatFraction.Quarter))
    Seconds += 10
    basic.showNumber(Seconds)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    music.playTone(523, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(523, music.beat(BeatFraction.Quarter))
    while (Seconds > 0) {
        basic.showNumber(Seconds)
        basic.pause(1000)
        Seconds += -1
    }
    if (Seconds == 0) {
        for (let index = 0; index < 5; index++) {
            music.playTone(523, music.beat(BeatFraction.Quarter))
            music.rest(music.beat(BeatFraction.Eighth))
            music.playTone(523, music.beat(BeatFraction.Quarter))
            music.rest(music.beat(BeatFraction.Whole))
            servos.P0.run(50)
            basic.showIcon(IconNames.SmallDiamond)
        }
        servos.P0.setAngle(90)
        servos.P0.setStopOnNeutral(false)
        basic.showLeds(`
            . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
                        . . . . .
        `)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    music.playTone(523, music.beat(BeatFraction.Quarter))
    Seconds = 0
    basic.showNumber(Seconds)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    music.playTone(523, music.beat(BeatFraction.Quarter))
    Seconds += 1
    basic.showNumber(Seconds)
})
let Seconds = 0
basic.showLeds(`
    . . . . .
        . . # . .
        . . . . .
        . . . . .
        . . . . .
`)
Seconds = 0
servos.P0.setAngle(90)
servos.P0.setStopOnNeutral(true)

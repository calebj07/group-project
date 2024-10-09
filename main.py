def on_logo_long_pressed():
    global tone
    if tone == 1000:
        music.ring_tone(tone)
        tone = 200
        basic.pause(200)
        music.rest(music.beat(BeatFraction.SIXTEENTH) / 4)
        music.play(music.create_sound_expression(WaveShape.TRIANGLE,
                960,
                200,
                255,
                255,
                1000,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH) / 4)
        music.ring_tone(tone)
        basic.pause(250)
        music.rest(music.beat(BeatFraction.SIXTEENTH) / 4)
    else:
        music.ring_tone(tone)
        tone = 1000
        basic.pause(200)
        music.rest(music.beat(BeatFraction.SIXTEENTH) / 4)
        music.play(music.create_sound_expression(WaveShape.TRIANGLE,
                200,
                960,
                255,
                255,
                1000,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH) / 4)
        music.ring_tone(tone)
        basic.pause(250)
        music.rest(music.beat(BeatFraction.SIXTEENTH) / 4)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    global count
    count += -1
    for index in range(count):
        music.ring_tone(tone)
        basic.pause(250)
        music.rest(music.beat(BeatFraction.SIXTEENTH) / 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    global count
    count += 1
    for index2 in range(count):
        music.ring_tone(tone)
        basic.pause(200)
        music.rest(music.beat(BeatFraction.SIXTEENTH) / 4)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

tone = 0
count = 0
count = 0
tone = 1000

def on_forever():
    basic.show_number(count)
basic.forever(on_forever)

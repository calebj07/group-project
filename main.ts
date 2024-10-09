input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    if (tone == 1000) {
        music.ringTone(tone)
        tone = 200
        basic.pause(200)
        music.rest(music.beat(BeatFraction.Sixteenth) / 10)
        music.play(music.createSoundExpression(WaveShape.Triangle, 960, 200, 255, 255, 1000, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
        music.rest(music.beat(BeatFraction.Sixteenth) / 10)
        music.ringTone(tone)
        basic.pause(250)
        music.rest(music.beat(BeatFraction.Sixteenth) / 10)
    } else {
        music.ringTone(tone)
        tone = 1000
        basic.pause(200)
        music.rest(music.beat(BeatFraction.Sixteenth) / 10)
        music.play(music.createSoundExpression(WaveShape.Triangle, 200, 960, 255, 255, 1000, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
        music.rest(music.beat(BeatFraction.Sixteenth) / 10)
        music.ringTone(tone)
        basic.pause(250)
        music.rest(music.beat(BeatFraction.Sixteenth) / 10)
    }
})
input.onButtonPressed(Button.A, function () {
    count += -1
    for (let index = 0; index < count; index++) {
        music.ringTone(tone)
        basic.pause(250)
        music.rest(music.beat(BeatFraction.Sixteenth) / 2)
    }
})
input.onButtonPressed(Button.B, function () {
    count = 0
    tone = 1000
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    count += 1
    for (let index = 0; index < count; index++) {
        music.ringTone(tone)
        basic.pause(250)
        music.rest(music.beat(BeatFraction.Sixteenth) / 2)
    }
})
let tone = 0
let count = 0
count = 0
tone = 1000
basic.forever(function () {
    basic.showNumber(count)
})

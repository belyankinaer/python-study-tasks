CLOCK_HOURS_COUNT = 12
CUCKOO_CLOCK_SOUND = 'ку'

for hour in range(1, CLOCK_HOURS_COUNT + 1):
    cuckoo_clock_sound_text = ""
    for _ in range(1, hour):
        cuckoo_clock_sound_text += CUCKOO_CLOCK_SOUND
    print(cuckoo_clock_sound_text)

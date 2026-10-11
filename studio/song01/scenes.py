"""Scene prompts and lyrics for Song 01 - Bunny ki Gaadi (Chintu Aur Dost)."""

STYLE = ("Cinematic 3D animated feature-film style children's cartoon, bright cheerful colours, "
         "warm sunlight, sunny Indian village, big expressive eyes, soft global illumination, "
         "high detail, no text, no words, no letters, no logos, no watermark")

BUNNY = ("Bunny, a funny friendly tan-brown cartoon rabbit with very long ears with pink insides, "
         "big shiny eyes, two big front teeth and a huge happy grin, wearing an olive-green vest and a small red scarf")
CAR = ("a small round bright-red open-top toy-like car with big yellow wheels, a rubber horn bulb "
       "and an orange marigold garland on the front")
CHINTU = ("Chintu, an 8-year-old Indian boy with messy thick black hair, big brown eyes, "
           "orange kurta, blue sleeveless vest, cream shorts, brown cloth satchel")
MEERA = ("Meera, an 8-year-old Indian girl with wavy black hair, a pink hairband with a pink flower, "
         "pink kurta with gold patterns, mustard-yellow pants, small school bag")
TOTO = ("Toto, a small cute white robot with royal-blue joints, round head with a black glass face "
        "screen showing two glowing cyan oval eyes, a small blue propeller on top of his head")
DADAJI = ("Dadaji, a kind Indian grandfather with white hair and neat white beard, round black glasses, "
          "cream kurta and olive-green Nehru jacket, wooden walking stick")

# id: prompt (16:9). The same seed is used for every scene so the look stays as close as possible.
SCENES = {
    "C1": f"{BUNNY} happily drives {CAR} along a colourful Indian village lane with painted houses, flowers and festive bunting, side view, camera at wheel height.",
    "C2": f"Close-up low angle of the big yellow wheels of {CAR} spinning on a dusty village road with dust puffs, {BUNNY} above bouncing in his seat and waving one paw.",
    "C3": f"Wide shot: {BUNNY} drives {CAR} slowly through a cheerful Indian village market; happy children, a smiling chai seller and a white goat clap and dance as it passes, bunting overhead.",
    "C4": f"Medium close-up: {BUNNY} sits in {CAR} and squeezes the shiny rubber horn bulb with a huge grin, long ears standing straight up, little colourful musical notes floating out of the horn, birds fluttering from a tree.",
    "V1a": f"{CHINTU} stands at a sunny village roadside waving happily as {CAR} driven by {BUNNY} approaches.",
    "V1b": f"{CHINTU} happily sits in the passenger seat of {CAR} next to {BUNNY} who is driving, both laughing, village lane behind them.",
    "V2a": f"{MEERA} waves cheerfully under a huge banyan tree in an Indian village as {CAR} arrives, {BUNNY} driving and {CHINTU} in the front seat.",
    "V2b": f"{MEERA} sits happily in the back seat of {CAR}, {CHINTU} in the front seat turning to smile at her, {BUNNY} driving, village road.",
    "V3a": f"{TOTO} flies down from a bright blue sky with his propeller spinning, waving, above {CAR} where {BUNNY}, {CHINTU} and {MEERA} look up excitedly.",
    "V3b": f"{TOTO} sits in the back seat of {CAR} next to {MEERA}, all friends laughing together, {CHINTU} in front, {BUNNY} driving.",
    "V4a": f"{CAR} is stopped at the foot of a steep green hill; {CHINTU}, {MEERA} and {TOTO} wear seat belts across their chests and give a big thumbs-up, {BUNNY} at the wheel smiling.",
    "V4b": f"Wide view: {CAR} with four happy friends wearing seat belts slowly climbs a winding road up a lush green hill in the Indian countryside.",
    "V4c": f"From the top of a green hill, {CAR} with {BUNNY} and friends looks down at a colourful Indian village fair with a Ferris wheel, balloons and stalls in a sunny valley.",
    "OUT": f"At a colourful Indian village fair with a Ferris wheel and balloons, {DADAJI} claps and cheers as {BUNNY}, {CHINTU}, {MEERA} and {TOTO} wave happily at the camera next to {CAR}.",
}

CHORUS = ["बनी की गाड़ी, चली रे चली,",
          "पों-पों करती गली-गली!",
          "गोल-गोल पहिए, घूमें गोल,",
          "सब मिलकर बोलो — पों! पों! पों!"]
VERSES = {
    "v1": ["रस्ते में खड़ा था चिंटू प्यारा,", "बोला, \"बनी, मुझे भी ले चलो यारा!\"",
           "एक सवारी बैठ गई,", "गाड़ी फिर से चल पड़ी!"],
    "v2": ["आगे मिली मीरा, बस्ता लेकर,", "बोली, \"मुझको भी ले चलो मेले पर!\"",
           "दो सवारी बैठ गईं,", "गाड़ी फिर से चल पड़ी!"],
    "v3": ["ऊपर से उड़ता आया टोटो,", "बोला, \"बीप-बूप! खींचो मेरी फ़ोटो!\"",
           "तीन सवारी बैठ गईं,", "गाड़ी फिर से चल पड़ी!"],
    "v4": ["आई चढ़ाई, ऊँची-ऊँची,", "बनी बोला, \"बेल्ट बाँधो सच्ची!\"",
           "धीरे-धीरे, संभल-संभल,", "पहुँच गए सब मेले में चल!"],
}
VERSE_SHOTS = {"v1": ["V1a", "V1a", "V1b", "V1b"], "v2": ["V2a", "V2a", "V2b", "V2b"],
               "v3": ["V3a", "V3a", "V3b", "V3b"], "v4": ["V4a", "V4a", "V4b", "V4c"]}
COUNT_AT = {"v1": 1, "v2": 2, "v3": 3}   # big number pops on line 3 of these verses
CHORUS_SHOTS = ["C1", "C2", "C3", "C4"]
FORM = [("intro", 4), ("chorus", 8), ("v1", 8), ("chorus", 8), ("v2", 8),
        ("v3", 8), ("v4", 8), ("chorus", 8), ("chorus", 8), ("outro", 4)]
BPM = 100

# Short, style-first prompts for the keyless fallback model (CLIP truncates after ~75 tokens).
S = "3D Pixar style cartoon render, cute, bright colours, sunny Indian village,"
BN = "cute fluffy tan cartoon bunny rabbit with long ears and red scarf"
RC = "small shiny red toy car with big yellow wheels"
KB = "cute cartoon Indian boy in orange kurta"
MG = "cute cartoon Indian girl in pink dress with pink flower hairband"
TR = "cute small white cartoon robot with blue joints and cyan eyes"
SHORT = {
    "C1": f"{S} {BN} driving a {RC}, side view, colourful houses and bunting",
    "C2": f"{S} close-up of big yellow wheels of a {RC} on a dusty road, {BN} waving",
    "C3": f"{S} {BN} driving a {RC} through a happy village market, children clapping, goat",
    "C4": f"{S} {BN} in a {RC} honking the horn, colourful music notes in the air",
    "V1a": f"{S} {KB} waving at roadside, a {RC} driven by a {BN} arrives",
    "V1b": f"{S} {KB} and a {BN} laughing together in a {RC}",
    "V2a": f"{S} {MG} waving under a big banyan tree, {RC} arriving",
    "V2b": f"{S} {MG} and {KB} smiling in the back of a {RC}",
    "V3a": f"{S} {TR} with a propeller on his head flying in blue sky, waving",
    "V3b": f"{S} {TR} sitting in a {RC} with happy cartoon kids, laughing",
    "V4a": f"{S} happy cartoon kids wearing seat belts in a {RC}, thumbs up, green hill behind",
    "V4b": f"{S} {RC} climbing a winding road up a lush green hill, wide view",
    "V4c": f"{S} view from a green hill top down to a colourful village fair with Ferris wheel and balloons",
    "OUT": f"{S} cartoon Indian grandfather with white beard and glasses cheering with {KB}, {MG} and a {BN} at a village fair, Ferris wheel",
}

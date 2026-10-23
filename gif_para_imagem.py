from PIL import Image
from pathlib import Path

gifs = sorted(Path(".").glob("*.gif"))

for gif in gifs:
    with Image.open(gif) as im:
        im.seek(im.n_frames//2)
        im.convert("RGB").save(gif.with_name(gif.stem + "_intermediario.png"), "PNG")
        im.seek(im.n_frames-1)
        im.convert("RGB").save(gif.with_name(gif.stem + "_fim.png"), "PNG")
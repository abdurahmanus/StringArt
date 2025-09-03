from types import SimpleNamespace

import io
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from generate import generate

app = FastAPI()


@app.post("/generate/")
def generate_string_art(
    input_file: UploadFile = File(...),
    side_len: int = Form(300),
    export_strength: float = Form(0.1),
    nail_step: int = Form(4),
    wb: bool = Form(False),
    rgb: bool = Form(False),
    rect: bool = Form(False),
):
    args = SimpleNamespace(
        input_file=input_file.file,
        side_len=side_len,
        export_strength=export_strength,
        radius1_multiplier=1,
        radius2_multiplier=1,
        nail_step=nail_step,
        wb=wb,
        rgb=rgb,
        rect=rect,
        pull_amount=None,
        random_nails=None,
    )

    result_img = generate(args)

    # TODO: how to handle it correctly?
    buf = io.BytesIO()
    result_img.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


app.mount("/", StaticFiles(directory="static", html=True), name="static")

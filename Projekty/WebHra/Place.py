def place(image : str, x : float, y : float, width : float, height : float):
    url = f"/Projekty/WebHra/Assets/{image}.png"

    style = ""
    style += "position:absolute;"
    style += f"left:{x}%;"
    style += f"top:{y}%;"
    style += f"width:{width}vw;"
    style += f"height:{height}vw;"
    style += f"background-image:url({url});"
    style += "background-size:contain;"
    style += "background-repeat:no-repeat;"
    style += "pointer-events:none;"
    style += "transform:translate(-50%, -50%);"

    return f'<div style="{style}"></div>'

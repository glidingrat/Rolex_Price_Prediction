from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from .models import predict_price

main = Blueprint("main", __name__)

steps = ["size", "bezel", "material", "bracelet", "dial", "papers", "prediction"]

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/step/<step>", methods=["GET", "POST"])
def step(step):
    if step not in steps:
        return redirect(url_for("main.home"))

    session.setdefault('size', '36')
    session.setdefault('material', 'Stainless Steel')
    session.setdefault('bezel', 'Fluted')
    session.setdefault('bracelet', 'Jubilee')
    session.setdefault('dial', 'Green')
    session.setdefault('papers', 'No')

    current_index = steps.index(step)

    if request.method == "POST":
        for key in request.form:
            session[key] = request.form[key]

        if step == "papers":
            return redirect(url_for("main.step", step="prediction"))
        else:
            return redirect(url_for("main.step", step=steps[current_index + 1]))

    context = {
        "current_step": step,
        "back_url": url_for("main.step", step=steps[current_index - 1]) if current_index > 0 else None,
        "next_button_text": steps[current_index + 1] if current_index + 1 < len(steps) else "prediction",
        "title": "Konfigurátor hodinek Rolex Datejust",
    }

    for field in ["size", "material", "bezel", "bracelet", "dial", "papers"]:
        context[field] = session.get(field)

    if step == "bracelet":
        material = session.get("material")
        bracelet = session.get("bracelet")
        if material and bracelet:
            if material == "Stainless Steel":
                image = f"{bracelet}.avif"
            else:
                image = f"{material}_{bracelet}.avif"


            context["bracelet_image"] = image

    if step == "prediction":
        cena = predict_price(
            size=session.get("size"),
            material=session.get("material"),
            bezel=session.get("bezel"),
            bracelet=session.get("bracelet"),
            dial=session.get("dial"),
            papers=session.get("papers")
        )
        context["cena"] = cena

    return render_template("index.html", **context)

@main.route("/get_bracelet_image/<material>/<bracelet>")
def get_bracelet_image(material, bracelet):
    if material == "Stainless Steel":
        image = f"{bracelet}.avif"
    else:
        image = f"{material}_{bracelet}.avif"
    return jsonify({"image": image})

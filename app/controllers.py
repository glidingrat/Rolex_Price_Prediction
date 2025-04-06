from flask import render_template, request, redirect, url_for, session
from .models import predict_price

def init_routes(app):
    steps = ["size", "bezel", "material", "bracelet", "dial", "papers", "prediction"]

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/step/<step>", methods=["GET", "POST"])
    def step(step):
        if step not in steps:
            return redirect(url_for("home"))

        session.setdefault('size', '36')
        session.setdefault('material', 'Stainless Steel')
        session.setdefault('bezel', 'Fluted')
        session.setdefault('bracelet', 'Jubilee')
        session.setdefault('dial', 'Green')
        session.setdefault('papers', 'No')

        current_index = steps.index(step)  # Pořadí aktuálního kroku v seznamu steps

        if request.method == "POST":
            for hodnota in request.form:
                session[hodnota] = request.form[hodnota]
                # Pro každý odeslaný prvek ve formuláři uloží jeho hodnotu do session

            if step == "papers":
                return redirect(url_for("step", step="prediction"))
            else:
                return redirect(url_for("step", step=steps[current_index + 1]))

        context = {
            "current_step": step,
            "back_url": url_for("step", step=steps[current_index - 1]) if current_index > 0 else None,
            "next_button_text": steps[current_index + 1] if current_index + 1 < len(steps) else "prediction",
            "title": "Rolex Datejust",
        }

        for field in ["size", "material", "bezel", "bracelet", "dial", "papers"]:
            context[field] = session.get(field)  # Ze sessionu vybere hodnotu a vloží ji do index.html

        if step == "bracelet":
            material = session.get("material")
            bracelet = session.get("bracelet")

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

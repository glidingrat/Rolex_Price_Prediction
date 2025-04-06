# Predikce ceny hodinek Rolex Datejust
Projekt predikuje cenu hodinek ná základě atributů: Size, Material, Bezel, Bracelet, Dial Color, With Papers

## Jak spustit program? 
Otevřte si soubor v `cmd` a poté pište:
1. `py -m venv venv`
2. `.\venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `py run.py`

## Nastavení config.json
Zde si můžete vytvořit vlastní `secret_key` pro session
1. Otevřte soubor `config.json`
2. Přejmenujte si `"your-secret-key"`

## Návrhový vzor
Projekt podle vzoru MVC (Model-View-Controller)
 - `models.py` Obsahuje model strojového učení a jeho načítání
 - `templates/` HTML stránky, kam uživatel zadává parametry
 - `controllers.py` Zpracovává vstupy z formuláře, připravuje predikci a pošle ji zpět do view

## Odkazy
- **YT link na Random Forest model**: [Random Forest](https://www.youtube.com/watch?v=ok2s1vV9XW0)
- **RandomForestRegressor** [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
- **Sběr dat a trénování modelu** [Google colab](https://colab.research.google.com/drive/1gDjfbGpYowpRuWRNh_Qa6G4zYLTLJ1QW?usp=sharing)
- **Jak získat ebay api** [yt link](https://youtu.be/i9A3zvuMWNc?si=Ukpy9Q4037IxKuW7)
- [GitHub](https://github.com/glidingrat/Rolex_Price_Prediction)


---
Krejčiřík Lukáš, C4a | Email: krejcirik@spsejecna.cz | 6.4.2025 | SPŠE Ječná | Školní projekt
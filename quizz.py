import marimo

__generated_with = "0.8.9"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md("""# AP Python Groupe 4 - Quizz #5""")
    return


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    q1 = mo.md("""
    ## Données binaires & texte

    En python, le litéral `"🎄"` désigne un objet de type

    {choice}
    """).batch(choice=mo.ui.radio(["str", "bytes", "text", "emoji", "🐒", "aucune de ces réponses"]))
    q1
    return q1,


@app.cell
def __(mo):
    q2 = mo.md("""
    ## Données binaires & texte

    ```python
    data = open(filename, **options)
    ```

    Quel est le type de `data` ?

    {choice}
    """).batch(choice=mo.ui.multiselect(["bytes", "str", "file", "ça dépend ..."], label="Réponses multiples"))
    q2
    return q2,


@app.cell
def __(mo):
    q3 = mo.md("""

    ### Zen

    Cocher le résultat s'il fait partie du "zen de Python" :

    {cb1} Beautiful is better than ugly.

    {cb2} Explicit is better than implicit.

    {cb3} Windows sucks.

    {cb4} Complex is better than complicated.

    """).batch(
        cb1=mo.ui.checkbox(),
        cb2=mo.ui.checkbox(),
        cb3=mo.ui.checkbox(),
        cb4=mo.ui.checkbox(),)
    q3
    return q3,


@app.cell
def __(mo):
    q4 = mo.md("""
    ## `*args` et `**kwargs`

    Supposons que l'on ait défini la fonction `f` de la façon suivante:

    ```python
    def f(*args, **kwargs):
        print(len(args), len(kwargs))
    ```

    Qu'est-ce qui s'affiche quand on execute le code `f(1, "Hello", None, verbose=False, sauce="mustard")
    ` ?

    {text}

    """).batch(text=mo.ui.text(label="Réponse"))
    q4
    return q4,


@app.cell
def __(mo):
    q5 = mo.md("""
    ## Flet

    Compléter le programme suivant (dans les zones où figurent les "...") afin que s'affiche 0, puis 1, puis 2, etc. dans le terminal quand on clique de façon répétée sur le bouton "+" de l'application flet.

    {answer}

    """).batch(answer=mo.ui.code_editor(value="""
    import flet as ft

    def main(page: ft.Page):
        ...

        def on_click(event):
           ...
           page.update()

        page.add(ft.IconButton(ft.icons.ADD, on_click=on_click))

    ft.app(target=main)
    """))
    q5
    return q5,


@app.cell
def __(mo):
    mo.md(
        """
        ## JSON


        Contenu du fichier `firefox.json`:

        ```json
        {
          "browsers": {
            "firefox": {
              "name": "Firefox",
              "type": "desktop",
              "preview_name": "Nightly",
              "pref_url": "about:config",
              "accepts_flags": true,
              "accepts_webextensions": true,
              "releases": {
                "1.5": {
                  "release_date": "2005-11-29",
                  "release_notes": "https://developer.mozilla.org/Firefox/Releases/1.5",
                  "status": "retired",
                  "engine": "Gecko",
                  "engine_version": "1.8"
                }
              }
            }
          }
        }
        ```
        """
    )
    return


@app.cell
def __(mo):
    q6 = mo.md("""
    ### JSON & open

    Comment obtenir le dictionnaire `firefox_data` Python représentant le contenu du fichier `firefox.json` ?

    {answer}

    Commentaires: {comments}
    """).batch(
        answer=mo.ui.code_editor(placeholder="Répondre ici sous forme de code"),
        comments=mo.ui.text_area()
    )
    q6
    return q6,


@app.cell
def __(mo):
    q7 = mo.md("""
    ### Accéder aux données

    Comment accéder à la date de publication (🇺🇸 release) de firefox 1.5 à partir du dictionnaire `firefox_data` ?

    {answer}

    Commentaires: {comments}
    """).batch(
        answer=mo.ui.code_editor(placeholder="Répondre ici sous forme de code"),
        comments=mo.ui.text_area()
    )
    q7
    return q7,


@app.cell
def __(mo, q1, q2, q3, q4, q5, q6, q7):
    import json
    qs = [q1, q2, q3, q4, q5, q6, q7]

    with open("answers.json", mode="tw", encoding="utf-8") as output:
        json.dump([q.value for q in qs], output)

    mo.md(f"""
    ## Synthèse des choix

    (Sauvegardés dans `answers.json`)

    {mo.tree([q.value for q in qs])}
    """)
    return json, output, qs


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()

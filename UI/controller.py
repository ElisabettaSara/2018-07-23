import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        for n in self._model.getAnni():
            self._view.ddyear.options.append(ft.dropdown.Option(n))


    def handle_graph(self, e):
        self._view.txt_result.clean()
        giorni = self._view.txtGiorni.value
        try:
            intGiorni = int(giorni)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico intero"))

        if (intGiorni)<1 or intGiorni>180:
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico intero compreso fra 1 e 180"))
        anno = int(self._view.ddyear.value)

        self._model.creaGrafo(anno, intGiorni)

        sommaPesi=self._model.getSommaPesi()

        for n in sommaPesi:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {n[0]} somma pesi = {n[1]}"))

        self._view.update_page()

    def handle_path(self, e):
        pass
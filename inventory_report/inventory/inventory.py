from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xmltodict
import json
import csv


class Inventory:
    @staticmethod
    def import_data(path, type):
        if type == "simples":
            return SimpleReport.generate(Inventory.file_reader(path))
        elif type == "completo":
            return CompleteReport.generate(Inventory.file_reader(path))
        else:
            raise ValueError("Tipo inválido")

    @staticmethod
    def file_reader(path):
        if path.endswith(".csv"):
            with open(path, "r") as csv_file:
                return list(csv.DictReader(csv_file))
        elif path.endswith(".json"):
            with open(path, "r") as json_file:
                return json.load(json_file)
        elif path.endswith(".xml"):
            with open(path, "r") as xml_file:
                return xmltodict.parse(xml_file.read())["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")

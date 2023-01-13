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
                csv_reader = csv.DictReader(csv_file)
                return [line for line in csv_reader]
        elif path.endswith(".json"):
            with open(path, "r") as json_file:
                json_reader = json.load(json_file)
                return [line for line in json_reader]
        elif path.endswith(".xml"):
            with open(path, "r") as xml_file:
                xml_reader = xmltodict.parse(xml_file.read())
                return [line for line in xml_reader["dataset"]["record"]]
        else:
            raise ValueError("Arquivo inválido")
